# -*- coding: utf-8 -*-
import scrapy
import urllib


class StackoverflowV12Spider(scrapy.Spider):
    name = 'StackOverflow_v1_2'
    ori_search_str_list = [
        'csharp',
        'c++',
        'how to use openframeworks',
        'Tensorflow',
        ]
    count = 0

    def start_requests(self):
        urls = []
        for istr in self.ori_search_str_list:
            urls.append('https://stackoverflow.com/search?q=' \
                        + urllib.parse.quote(istr))
        print(urls)
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
        

    def parse(self, response):
        filename = self.ori_search_str_list[self.count]
        self.count += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
