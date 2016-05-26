# -*- coding: utf-8 -*-
import scrapy
import re

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
    		if type(title) is list:
    			if len(title)>0:
    				title = title[0]
    			else:
    				title = None 
    	elif len(title)>0:
    		title = title[0]

    	if not descp:
    		paragraphs = response.xpath('//p/text()').extract()
    		for i in range(len(paragraphs)):
    			if(len(paragraphs[i])>50):
    				descp = paragraphs[i]
    				break
    	elif len(descp)>0:
    		max_descp = ''
    		for val in descp:
    			if(len(max_descp)<len(val)):
    				max_descp=val
    		descp = max_descp

    	if not img:
    		photos = response.xpath('//img/@src').extract()
    		for val in photos:
    			if '.jpg' in val:
    				img = val
    				break
    		else:
    			img = None
    	elif len(img)>0:
    		for val in img:
    			if 'http' in val or 'https' in val:
    				img = val
    				break

    	if not time:
    		pass
    	elif len(time)>0:
    		time=time[0]

    	stopwords_file = open("StopWord.txt", "r")
    	STOPWORDS = stopwords_file.read().split(',')

    	tags_title = [re.sub('[^a-zA-Z\']', '', word) for word in title.split() if re.sub('[^a-zA-Z\']', '', word).lower() not in STOPWORDS]
    	tags_desc = [re.sub('[^a-zA-Z\']', '', word) for word in descp.split() if re.sub('[^a-zA-Z\']', '', word).lower() not in STOPWORDS]
    	tags = tags_title+tags_desc

        return BlogMetaItem(url=url,title=title,description=descp,image=img,published_on=time,tags=tags)
