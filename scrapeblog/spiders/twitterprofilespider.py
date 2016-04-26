# -*- coding: utf-8 -*-
import scrapy
import tweepy

from ..items import TwitterProfileItem


class BlogSiteSpider(scrapy.Spider):

    name = 'twitterprofile'

    consumer_key = 'GpkJNZ7GFPGVJwgJn8a7x2YC1'
    consumer_secret = 'CQ9JeolvyvMgzmb6b3XAxCnO25FYZldZqct8AV8UiAOzpbNl8H'
    access_token = '3080055000-zLYMf65KrGXUDRj1G3G8CqFRoTtVOuC2r26Vyzz'
    access_token_secret = '8Pz7bWof0cDI5RKvUp6ea0p7rnOcpgvXuHrhuDgFRCUdS'

    def parse(self, response):
    	
    	auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
    	auth.set_access_token(self.access_token, self.access_token_secret)

    	api = tweepy.API(auth)

    	url = response.url

    	screen_name = (url.split('/'))[3]
    	screen_name = screen_name.strip()

    	user = api.get_user(screen_name)

    	try:
    		website = user.entities['url']['urls'][0]['expanded_url']
    	except KeyError:
    		website = None

        return TwitterProfileItem(username=screen_name,fullname=user.name,website=website,location=user.location,photo=(user.profile_image_url).replace("_normal",""))
