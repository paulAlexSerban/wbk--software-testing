import csv
from pathlib import Path

DATA_FILE = "data.csv"
CFG_FILE_DIR = "config"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(CFG_FILE_DIR).joinpath(DATA_FILE)


def get_data():
    with open(DATA_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        data = [tuple(row) for row in reader]
    return data

print(get_data())