from collections import defaultdict
from pathlib import Path

from pep_parse.constants import RESULTS_FOLDER_NAME
from pep_parse.settings import BASE_DIR
from pep_parse.utils import create_csv_file


class PepParsePipeline:
    """In this pipeline we will collect some info inside the pipeline state."""

    def __init__(self):
        """Create a results folder, initialize the state."""

        (Path(BASE_DIR) / RESULTS_FOLDER_NAME).mkdir(
            parents=True,
            exist_ok=True
        )
        self.pep_status = None

    def open_spider(self, spider):
        """Cleanup state when opening each spider in this pipeline."""

        self.pep_status = defaultdict(int)

    def process_item(self, item, spider):
        self.pep_status[item["status"]] += 1
        return item

    def close_spider(self, spider):
        """Create a summary document."""

        create_csv_file(self.pep_status)
