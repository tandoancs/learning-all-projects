# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


def full_link(company_symbol_link):
    url = "https://finance.yahoo.com/sectors/technology/"
    return url + company_symbol_link

class CompanyDetailsItem(scrapy.Item):
    company_name = scrapy.Field()
    company_symbol_link = scrapy.Field(input_processor = MapCompose(full_link))
    company_price_interaday = scrapy.Field()
    

# class ItemloaderspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
