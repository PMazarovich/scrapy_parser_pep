from pep_parse.utils import create_csv_file


class PepParsePipeline:
    """In this pipeline we will collect some info inside the pipeline state."""

    def __init__(self):
        self.pep_status = None

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
