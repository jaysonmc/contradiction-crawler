from crawler import Crawler
from processtext import ProcessText
import sys
import fire


def crawl(url='https://sara-sabr.github.io/ITStrategy/home.html'):
    Crawler([url])


def process():
    ProcessText()


if __name__ == '__main__':
    fire.Fire()
