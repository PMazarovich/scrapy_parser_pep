import csv
import os
from datetime import datetime

from pep_parse.constants import RESULTS_FOLDER_NAME, PEP_RESULTS_FILE


def create_csv_file(results: dict):
    """Method for pep."""

    os.makedirs(RESULTS_FOLDER_NAME, exist_ok=True)
    total = 0
    for i in results.values():
        total+=i
    data = (("State", "Amount"), *results.items(), ('Total', total))
    with open(
            os.path.join(RESULTS_FOLDER_NAME, f'{PEP_RESULTS_FILE}_{datetime.now():%Y-%m-%d_%H-%M-%S}.csv'),
            "w",
            newline="",
            encoding="utf-8",
    ) as file:
        writer = csv.writer(file)
        writer.writerows(data)
