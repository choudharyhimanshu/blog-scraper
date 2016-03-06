# -*- coding: utf-8 -*-
import scrapy

from ..items import BlogItem


class BlogSpider(scrapy.Spider):

    name = 'blog'

    def parse(self, response):
    	title = response.xpath('//div[contains(@class, "post")]/h1/text()').extract()
        headings = response.xpath('//div[contains(@class, "post")]/h2/text()').extract()
        descp = response.xpath('//div[contains(@class, "post")]/p/text()').extract()
        img = response.xpath('//div[contains(@class, "post")]//img/@src').extract()
        return BlogItem(title=title,headings=headings,description=descp,photos=img)
