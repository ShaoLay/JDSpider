# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    big_name = scrapy.Field()
    samll_name = scrapy.Field()
    small_url = scrapy.Field()
    book_image = scrapy.Field()
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_store = scrapy.Field()
    book_id = scrapy.Field()
    book_time = scrapy.Field()
    book_price = scrapy.Field()

