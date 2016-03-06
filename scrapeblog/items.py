# -*- coding: utf-8 -*-
import scrapy


class BlogItem(scrapy.Item):
    title = scrapy.Field()
    headings = scrapy.Field()
    description = scrapy.Field()
    photos = scrapy.Field()
