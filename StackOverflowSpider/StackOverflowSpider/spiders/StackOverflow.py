# -*- coding: utf-8 -*-
import scrapy


class StackoverflowSpider(scrapy.Spider):
    name = 'StackOverflowSpider'
    # allowed_domains = ['stackoverflow.com']
    count = 0

    def start_requests(self):
        urls = [
            'https://stackoverflow.com/',
            'https://www.csdn.net/',
            'https://segmentfault.com/',
            ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        filename = 'stackoverflow-%s.html' % str(self.count)
        self.count += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
