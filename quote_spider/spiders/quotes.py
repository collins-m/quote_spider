# -*- coding: utf-8 -*-
from scrapy import Spider, Request


class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            keywords = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            yield{
                'Text': text,
                'Author': author,
                'Keywords': keywords,
                }

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)

        yield Request(absolute_next_page_url)
