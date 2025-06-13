# SCRAPY Asynchronous Parser for PEPs (Yandex Practicum Training Project)

## Goal

Gain hands-on experience working with an asynchronous Scrapy parser in Python.

This project was developed as part of the Yandex Practicum course. The main goal is to gain practical skills in developing a parser using Scrapy. The PEP (Python Enhancement Proposals) site is used as the target for scraping to test how Scrapy works.

## Key Features

- Uses the Feed mechanism to write Items directly to a file.
- Custom handler and state implemented to generate a summary file at the end of the scraping process.
- The parser is asynchronous and uses an event loop, so execution is not blocked during I/O operations.

## Project Structure

- **Spider**: `pep_parse/spiders/pep.py`
- **Pipeline**: `pep_parse/pipelines.py`
- **Feed (CSV output)**: `pep_parse/settings.py:3`
- **Pipeline is stateful**: Only one spider can run at a time. See `pep_parse/pipelines.py:9`

## Running the Parser

From the project root:

```bash
# Create a virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the spider
scrapy crawl pep
```

Wait a bit — Scrapy is asynchronous and doesn't block execution on I/O. Results will appear in the `/results` folder.

## Author

**Peter Mazarovich**\
[petrmazarovich@gmail.com](mailto\:petrmazarovich@gmail.com)

