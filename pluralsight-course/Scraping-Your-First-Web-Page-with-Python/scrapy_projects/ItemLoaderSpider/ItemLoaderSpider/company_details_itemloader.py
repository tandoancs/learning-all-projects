# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from ItemLoaderSpider.items import CompanyDetailsItem
from scrapy.loader import ItemLoader

class CompanyDetailsItemLoaderSpider(scrapy.Spider):
    name = "company_details"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/research-hub/screener/most_actives/"]
