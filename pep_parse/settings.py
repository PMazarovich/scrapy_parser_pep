from pathlib import Path

from pep_parse.constants import RESULTS_FOLDER_NAME

BASE_DIR = Path(__file__).parent.parent
BOT_NAME = "pep_parse"
LOG_LEVEL = 'INFO'
FEEDS = {
    f"{RESULTS_FOLDER_NAME}/pep_%(time)s.csv": {
        "format": "csv",
        "fields": ["number", "name", "status"],
    }
}
SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}
