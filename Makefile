init:
	python3 -m venv env
	source env/bin/activate
	pip install -r requirements.txt


update:
	source env/bin/activate
	pip install -U -r requirements.txt

run:
	source env/bin/activate
	python pipelines/transformations.py --input_file_paths "['1_day.jsonl', '30_days.jsonl']"
