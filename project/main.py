from crawler import Crawler
import sys
import fire


def crawl(url='https://sara-sabr.github.io/ITStrategy/home.html'):
    Crawler([url])


def process():
    print("Process things")


if __name__ == '__main__':
    fire.Fire()
