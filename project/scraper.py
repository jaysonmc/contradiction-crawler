import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import logging
import settings
import time


class Scraper(CrawlSpider):

    name = 'IT Strategy'
    allowed_domains = ['sara-sabr.github.io']

    rules = (
        # To-do doesnt parse presentations well atm, should be able to remove the ending '\.html$' part of the regex
        Rule(LinkExtractor(allow=r'.*\/ITStrategy\/.*\.html$'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        filename = settings.OUTPUT_FOLDER + \
            str(time.time()) + "_" + response.url.split("/")[-1]

        parsers = ["html.parser", "html5", "lxml"]
        parseSuccessful = False

        with open(filename, 'wb') as f:
            for parser in parsers:
                try:
                    if not parseSuccessful:
                        cleanedHTML = BeautifulSoup(response.body, parser).text
                        if cleanedHTML.isspace():
                            print(parser + " resulted in " +
                                  filename + " being empty")
                            continue
                        else:
                            f.write(cleanedHTML.encode())
                            parseSuccessful = True
                            print("Cleaned " + filename + " using " + parser)
                except Exception as e:
                    print("Unable to parse with " + parser + ": " + filename)
                    logging.info('filename: \t' + str(e))

            if not parseSuccessful:
                print("Unable to parse " + filename + ". Dumping raw HTML.")
                f.write(response.body)
