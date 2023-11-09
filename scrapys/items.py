# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubTrendingItem(scrapy.Item):
    # define the fields for your item here like:
    href = scrapy.Field()
    # org = scrapy.Field()
    # repo = scrapy.Field()
    description = scrapy.Field()
    language = scrapy.Field()
    total_start = scrapy.Field()
    fork_start = scrapy.Field()
    today_start = scrapy.Field()


class TgChannelItem(scrapy.Item):
    # define the fields for your item here like:
    description = scrapy.Field(serializer=str)
    url = scrapy.Field(serializer=str)
