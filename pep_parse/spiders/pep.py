import logging

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """
        Find all links to pep on the start page.

        Provide then links one by one to the parse_pep method,
        so it will extract the data and create items for pipeline.
        """

        tr_selectors = response.xpath('//tr')[1:]
        for tr_selector in tr_selectors:
            try:
                link = tr_selector.xpath('(.//td)[2]/a').attrib['href']
                yield response.follow(link,
                                      callback=self.parse_pep)
            except KeyError:
                continue

    def parse_pep(self, response):
        """Find data for PepParseItem to pass to pipeline."""

        number = int(response.xpath('/html/body/section/header/ul/li[3]/text()').get().split(' ')[1])
        dl_selector = response.xpath('//dl')
        status = dl_selector.xpath('(.//abbr)[1]/text()').get()
        name = response.xpath('//h1/text()')[1].get().split('– ')[1]
        yield PepParseItem(
            status=status,
            number=number,
            name=name
        )
