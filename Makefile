PY ?= python3

.PHONY: test lint deck models clean

test:
	$(PY) -m pytest tests/ -o addopts=""

lint:
	$(PY) -m compileall -q whisperdeck/

deck:
	$(PY) -m whisperdeck.deck list

models:
	$(PY) models/download.py --model base.en

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache/
