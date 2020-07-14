from scraper import Scraper
from scrapy.crawler import CrawlerProcess


class Crawler():

    def crawl(self, url):
        print("Crawling %s" % url)

        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        process.crawl(
            Scraper, start_urls=url)
        process.start()

        print("Done")
