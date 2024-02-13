# Barcode generation service
This service can generate barcodes as `.png` images based on any string

## Stack/Main Tools used
- Python
- Flask
- python-barcode
- pillow
- Cerberus
- pytest

## How to run
> I am using `virtualenv` here, feel free to not... Just remove it from `requirements.txt`
- Once you have cloned the repo, run `python3 -m venv .venv`
- To activate the virtual env, run `source .venv/bin/activate`
- To install all the dependecies, run `pip3 install -r requirements.txt` (Feel free to use `pip` instead of `pip3` if you want)
- In your terminal with the virtual env active, run `python3 run.py`, and thats it!

> [!NOTE]
> `validator_raw.py` is just some raw tests with Cerberus, you can delete that if you want tho
