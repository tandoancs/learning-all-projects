import scrapy


class CompanyDetailsSpider(scrapy.Spider):
    name = "company_details"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/sectors/technology/"]

    def parse(self, response):
        company_names_list = response.xpath(
            '//*[@id="nimbus-app"]/td[1]/span/div/a/div/span[2]').extract()
        company_price_list = response.xpath(
            '//*[@id="nimbus-app"]/td[2]/span').extract()
        
        count = len(company_names_list)
        
        for i in rang(0, count):
            print(company_names_list[i], company_price_list[i])