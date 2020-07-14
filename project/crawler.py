from scraper import Scraper
from scrapy.crawler import CrawlerProcess


class Crawler:

    def __init__(self, url):
        self.url = url
        self.crawl()

    def crawl(self):
        print("Crawling %s" % self.url)

        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        process.crawl(
            Scraper, start_urls=self.url)
        process.start()

        print("Done")
