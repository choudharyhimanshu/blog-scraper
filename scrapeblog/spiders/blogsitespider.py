# -*- coding: utf-8 -*-
import scrapy

from ..items import BlogSiteItem
from difflib import SequenceMatcher

class BlogSiteSpider(scrapy.Spider):

    name = 'blogsite'

    def similar(self,a, b):
    	return SequenceMatcher(None, a, b).ratio()

    def parse(self, response):
    	url = response.url
    	blogs_link = response.xpath('//h2/a/@href|//h1/a/@href').extract()
    	blogs_title = response.xpath('//h2/a/text()|//h1/a/text()').extract()
    	i = 0
    	while i < len(blogs_link):
    		if not blogs_link[i].startswith(url):
    			blogs_link.pop(i)
    			blogs_title.pop(i)
    			continue
    		if url == blogs_link[i]:
    			blogs_link.pop(i)
    			blogs_title.pop(i)
    			continue
    		if self.similar(blogs_link[i],blogs_title[i]) < .3:
    			blogs_link.pop(i)
    			blogs_title.pop(i)
    			continue
    		if len(blogs_title[i]) < 20:
    			blogs_link.pop(i)
    			blogs_title.pop(i)
    			continue
    		i+=1
        return BlogSiteItem(author=None,site_url=url,blogs_title=blogs_title,blogs_link=blogs_link)
