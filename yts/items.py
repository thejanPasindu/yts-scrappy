# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YtsItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    movie_idmb = scrapy.Field()
    movie_year = scrapy.Field()
    
