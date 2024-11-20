import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/19687421/difference-between-beautifulsoup-and-scrapy-crawler"
page = requests.get(url)
print(page.status_code)
