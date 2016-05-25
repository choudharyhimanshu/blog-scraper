# -*- coding: utf-8 -*-
import scrapy


class BlogItem(scrapy.Item):
    title = scrapy.Field()
    headings = scrapy.Field()
    description = scrapy.Field()
    photos = scrapy.Field()

class BlogMetaItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()
    published_on = scrapy.Field()
    tags = scrapy.Field()

class BlogSiteItem(scrapy.Item):
    author = scrapy.Field()
    site_url = scrapy.Field()
    blogs_title = scrapy.Field()
    blogs_link = scrapy.Field()

class TwitterProfileItem(scrapy.Item):
    username = scrapy.Field()
    fullname = scrapy.Field()
    website = scrapy.Field()
    location = scrapy.Field()
    photo = scrapy.Field()
