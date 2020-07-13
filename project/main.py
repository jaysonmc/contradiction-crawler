#import contradiction
import sys
from scraper import Crawler
from extracttext import ExtractText
from scrapy.crawler import CrawlerProcess


def main():

    def crawl(url):
        print("Crawling %s" % url)

        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        process.crawl(
            Crawler, start_urls=url)
        process.start()

        print("Done")

    def getUrl():
        url = sys.argv[1:]
        if not url:
            url = ['https://sara-sabr.github.io/ITStrategy/home.html']
            print('Defaulting to ' + url[0])
        return url

    # Run
    crawl(getUrl())


if __name__ == "__main__":
    main()
