# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


# class CrawlbaItem(Item):
#     beerUrl = Field()
#     beerName = Field()
#     breweryUrl = Field()
#     breweryName = Field()
#     abv = Field()
#     avg = Field()
#     hads = Field()
#     new_link = Field()
#     userRating = Field()
#     individRating = Field()
#     beerUrlRelate = Field()
#     descrip = Field()
#     referUrl = Field()

class TopItem(Item):
    beerUrl = Field()
    beerName = Field()
    breweryUrl = Field()
    breweryName = Field()
    # abv = Field()
    avg = Field()
    rank = Field()
    style = Field()

    beerUrlRelate = Field()
    userRating = Field()
    individRating = Field()
    descrip = Field()
    beerUrl = Field()
    referUrl = Field()
