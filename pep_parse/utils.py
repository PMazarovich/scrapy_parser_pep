import csv
import os

from pep_parse.constants import PEP_SUMMARY_FILE, RESULTS_FOLDER_NAME
from pep_parse.settings import BASE_DIR


def create_csv_file(results: dict):
    """Method for pep."""

    total = sum(results.values())
    data = (("State", "Amount"), *results.items(), ("Total", total))

    with open(
        os.path.join(BASE_DIR, RESULTS_FOLDER_NAME, PEP_SUMMARY_FILE),
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)
        writer.writerows(data)
