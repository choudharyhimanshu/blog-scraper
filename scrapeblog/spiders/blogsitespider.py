# -*- coding: utf-8 -*-
import scrapy

from ..items import BlogSiteItem


class BlogSiteSpider(scrapy.Spider):

    name = 'blogsite'

    def parse(self, response):
    	url = response.url
    	blogs_link = response.xpath('//h2/a/@href|//h1/a/@href').extract()
    	blogs_title = response.xpath('//h2/a/text()|//h1/a/text()').extract()
        return BlogSiteItem(author=None,site_url=url,blogs_title=blogs_title,blogs_link=blogs_link)
