# -*- coding: utf-8 -*-
import scrapy


class QuoteTagsSpider(scrapy.Spider):
    name = 'quote_tags'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
