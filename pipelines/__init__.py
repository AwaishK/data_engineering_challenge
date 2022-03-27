"""
"""
from pathlib import Path


def create_directory_if_not_exists(path: Path) -> None:
    if not path.is_dir():
        try:
            path.mkdir()
        except Exception as e:
            print(e)


DIR_PACKAGE = Path(__file__).resolve().parent  # ../data_engineering_challenge/pipelines
DIR_BASE = DIR_PACKAGE.parent # ../data_engineering_challenge

# ../data_engineering_challenge/data
DIR_DATA = DIR_BASE.joinpath("data")
