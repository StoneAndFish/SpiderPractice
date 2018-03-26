# -*- coding: utf-8 -*-
import scrapy


class StackoverflowV11Spider(scrapy.Spider):
    name = 'StackOverflow_v1_1'
    # allowed_domains = ['https://stackoverflow.com/']
    start_urls = ['https://stackoverflow.com//']

    def parse(self, response):
        for stackOverflow in response.css('div.question-summary.narrow'):
            realAnswerCounts = ''
            if stackOverflow.css('div.status.answered div.mini-counts span::text').extract_first() != None:
                realAnswerCounts = stackOverflow.css('div.status.answered div.mini-counts span::text').extract_first()
            elif stackOverflow.css('div.status.unanswered div.mini-counts span::text').extract_first() != None:
                realAnswerCounts = stackOverflow.css('div.status.unanswered div.mini-counts span::text').extract_first()
            else :
                realAnswerCounts = stackOverflow.css('div.status.answered-accepted div.mini-counts span::text').extract_first()

            yield {
                'Title': stackOverflow.css('div.summary a.question-hyperlink::text').extract_first(),
                'KeyWords': stackOverflow.css('div.summary a.post-tag::text').extract_first(),
                'UpdateMsg': \
                        stackOverflow.css('div.summary a.started-link::text').extract_first() \
                      + stackOverflow.css('div.summary span.relativetime::text').extract_first(),
                'Votes': stackOverflow.css('div.votes div.mini-counts span::text').extract_first(),
                'Answers': realAnswerCounts,
                'Views': stackOverflow.css('div.views div.mini-counts span::text').extract_first(),
                }
