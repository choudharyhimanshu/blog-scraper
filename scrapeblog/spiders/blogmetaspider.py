# -*- coding: utf-8 -*-
import scrapy

from ..items import BlogMetaItem


class BlogSpider(scrapy.Spider):

    name = 'blogmeta'

    def parse(self, response):
    	url = response.url
    	title = response.xpath('//meta[contains(@property,"title")]/@content').extract()
    	descp = response.xpath('//meta[contains(@property,"description")]/@content').extract()
    	img = response.xpath('//meta[contains(@property,"image")]/@content').extract()
    	time = response.xpath('//meta[contains(@property,"time")]/@content').extract()

    	if not title:
    		title = response.xpath('//title/text()').extract()
    	elif len(title)>1:
    		title = title[0]

    	if not descp:
    		pass
    	elif len(descp)>1:
    		max_descp = ''
    		for val in descp:
    			if(len(max_descp)<len(val)):
    				max_descp=val
    		descp = max_descp

    	if not img:
    		pass
    	elif len(img)>1:
    		for val in img:
    			if 'http' in val or 'https' in val:
    				img = val
    				break

    	if not time:
    		pass
    	elif len(time)>1:
    		time=time[0]

        return BlogMetaItem(url=url,title=title,description=descp,image=img,published_on=time)
