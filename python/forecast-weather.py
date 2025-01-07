import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


import requests

response = requests.get('https://www.wunderground.com/weather/vn/ho-chi-minh-city')

html = response.text

# parse the HTML
soup = BeautifulSoup(html, "html.parser")

# print the HTML as text
# print(soup.body.get_text().strip())
# print(soup.prettify())

print(soup.find(id="__WxMap_Style"))