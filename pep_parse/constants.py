from datetime import datetime
from pathlib import Path

RESULTS_FOLDER_NAME = "results"
CURRENT_DATE = f"{datetime.now():%Y-%m-%d_%H-%M-%S}"
PEP_SUMMARY_FILE = f"status_summary_{CURRENT_DATE}.csv"
PEP_RESULTS_FILE = f"pep_{CURRENT_DATE}.csv"
BASE_DIR = Path(__file__).parent.parent
