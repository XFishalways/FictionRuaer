# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FictionruaerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # created for FandomAM_Name
    fandomAMName = scrapy.Field()

    # created for Work
    fictionRating = scrapy.Field()
    fictionArchiveWarning = scrapy.Field()
    fictionCategories = scrapy.Field()
    fictionName = scrapy.Field()
    fictionLanguage = scrapy.Field()
    fictionPublishDate = scrapy.Field()
    fictionWords = scrapy.Field()
    fictionHits = scrapy.Field()
    fictionTitle = scrapy.Field()
    fictionPreface = scrapy.Field()
    fictionContent = scrapy.Field()
