"""
"""
import click
from tqdm import tqdm
from typing import List
import pandas as pd
from pipelines import DIR_DATA
from pipelines.utils import PythonLiteralOption


class Transformations:
    def __init__(self, input_file_paths: List[str]) -> None:
        """Initlized the input and output file names. 

        Parameters
        ..........

        input_file_paths (list): recieves the input file names place in data directory (../data_engineering_challenge/data)
        """
        self.input_file_paths = input_file_paths
        self.output_file_paths = [f'output_{file.split(".")[0]}.csv' for file in input_file_paths]

    def load_and_process_data_set(self, file_path: str) -> pd.DataFrame:
        df = pd.read_json(file_path, lines=True)
        df = df.join(pd.json_normalize(df['data']))
        df = df.drop('data', axis=1)

        # sum all electricity produdctions  
        df_production = df[df['kind'] == 'ElectricityProduction']
        df_production['total'] = df_production.apply(lambda row: sum([0 if pd.isna(row[c]) else row[c] for c in df.columns if c.split('.')[0] == 'production']), axis=1)
        df_production = df_production.groupby(['zone_key', pd.Grouper(key = 'datetime', freq='1H')])['total'].sum().reset_index()

        # Arrange all import and export zone-wise 
        df_exchange = df[df['kind'] == 'ElectricityExchange']
        df_exchange = df_exchange.assign(zone_key=df_exchange['zone_key'].str.split('->'))
        df_exchange = pd.concat([
            df_exchange.assign(zone_key=df_exchange['zone_key'].str[0], netFlow=df_exchange['netFlow'] * -1),
            df_exchange.assign(zone_key=df_exchange['zone_key'].str[1])
        ])
        df_exchange = df_exchange.groupby(['zone_key', pd.Grouper(key = 'datetime', freq='1H')])['netFlow'].sum().reset_index()

        # join proudction and exchange and add/subtract netFlow
        df = pd.merge(df_production, df_exchange, how='outer', on=['zone_key', 'datetime'])
        df[['total', 'netFlow']] = df[['total', 'netFlow']].fillna(0)
        df['total'] = df['total'] + df['netFlow']
        
        df = df.rename(columns={'zone_key': 'zone', 'datetime': 'hour'})
        return df[['zone', 'hour', 'total']].reset_index(drop=True)

    def run(self) -> None:
        for input_file_path, output_file_path in tqdm(zip(self.input_file_paths, self.output_file_paths), desc='Files to process'):
            in_file = DIR_DATA.joinpath(input_file_path)
            out_file = DIR_DATA.joinpath(output_file_path)
            df = self.load_and_process_data_set(file_path=in_file)

            # write data back to csv
            df.to_csv(out_file, index=False)
        

@click.command()
@click.option('-l', '--input_file_paths', cls=PythonLiteralOption, prompt='Provide file names placed in data directory')
def main(input_file_paths: List[str]) -> None:
    transformation = Transformations(input_file_paths=input_file_paths)
    transformation.run()


if __name__ == '__main__':
    main()

