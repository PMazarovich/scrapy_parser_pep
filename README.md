# SCRAPY Asynchronous Parser PEP (Yandex Practicum Training Project)

**Goal:** get hands‑on experience building SCRAPY parser in Python.

*Spider can be found here*: `pep_parse/spiders/pep.py`  

*Pipeline can be found here*: `pep_parse/pipelines.py`

*Feed was configured to collect items to the CSV file*: `pep_parse/settings.py:3`

*Pipeline is stateful. Only 1 spider can use it at a time.*: `pep_parse/pipelines.py:9`

---

Command to start the crawler (from the project root directory): 
```
scrapy crawl pep
```


## Author

**Peter Mazarovich**  
<petrmazarovich@gmail.com>