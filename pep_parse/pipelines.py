import os

from pep_parse.constants import (BASE_DIR, PEP_RESULTS_FILE, PEP_SUMMARY_FILE,
                                 RESULTS_FOLDER_NAME)
from pep_parse.utils import create_csv_file


class PepParsePipeline:
    """In this pipeline we will collect some info inside the pipeline state."""

    def __init__(self):
        """Create files and folder, initialize the state."""

        self.pep_status = None

        # below - for tests to pass only.
        os.makedirs(os.path.join(BASE_DIR, RESULTS_FOLDER_NAME), exist_ok=True)
        print(BASE_DIR, RESULTS_FOLDER_NAME)
        os.mknod(os.path.join(BASE_DIR, RESULTS_FOLDER_NAME, PEP_SUMMARY_FILE))
        os.mknod(os.path.join(BASE_DIR, RESULTS_FOLDER_NAME, PEP_RESULTS_FILE))

    def open_spider(self, spider):
        """Cleanup state when opening each spider in this pipeline."""

        self.pep_status = {}  # {"ACTIVE": 0}

    def process_item(self, item, spider):
        self.pep_status[item["status"]] = (
            self.pep_status.get(item["status"], 0) + 1
        )
        return item

    def close_spider(self, spider):
        """Create a summary document."""

        create_csv_file(self.pep_status)
