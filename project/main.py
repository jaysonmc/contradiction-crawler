from crawler import Crawler
import sys


def main():

    crawler = Crawler()

    def getUrl():
        url = sys.argv[1:]
        if not url:
            url = ['https://sara-sabr.github.io/ITStrategy/home.html']
            print('Defaulting to ' + url[0])
        return url

    # Run
    crawler.crawl(getUrl())


if __name__ == "__main__":
    main()
