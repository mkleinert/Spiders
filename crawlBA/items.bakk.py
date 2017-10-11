# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy


#class BaTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
 #   pass
from scrapy.item import Item, Field


class Website(Item):
    beerUrl = Field()
    beerName = Field()
    breweryUrl = Field()
    breweryName = Field()
    abv = Field()
    avg = Field()
    hads = Field()
    new_link = Field()
    userRating = Field()
    individRating = Field()
    beerUrlRelate = Field()
    descrip = Field()
    referUrl = Field()

    #description = Field()



