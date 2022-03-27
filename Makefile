init:
	python3 -m venv env
	#!/bin/bash source env/bin/activate
	pip install -r requirements.txt


update:
	#!/bin/bash source env/bin/activate
	pip install -U -r requirements.txt

run:
	#!/bin/bash source env/bin/activate
	python pipelines/transformations.py --input_file_paths "['1_day.jsonl', '30_days.jsonl']"
