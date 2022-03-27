# QUICK START

## PROJECT STRUCTURE

```bash

├── data_engineering_challenge
├── data
├── env
├── pipelines
│   │   │── transformations.py
│   │   │── utils.py
│   │   │
│   │   │
└── README.md
└── Makefile
└── requirements.txt
```

## Installation & Setup

Run the following commands to clone the project and then create virtual enviroment

```bash
git clone git@github.com:AwaishK/data_engineering_challenge.git
cd data_engineering_challenge
make init
```

## Please run below command to run pipeline

```bash
make run
```

## Explanation
    Step 1: electricty mix means electricity produced by different sources of energy like coal, biomass, gas.
    So total product at a point in time is sum of all sources of energy. 

    Step 2: Sum total production by hourly interval for each zone

    Step 3: For each zone find total import and export by hourly interval

    Step 4: add the import and subtract the export for each zone and hour from total production 

    Step 5: Load the output to csv

## Improvements (Even that was not part of task)
    1) I could add unit tests 
    2) Data quality checks
    3) Add exception handling 
    4) Logging 
    5) Schedule it to run periodically at certain period of time using crontab and apache airflow
    6) Visualization to see production and consumption in each zone using apache superset or metaplotlib or plotly
    7) click application as a separate module
            