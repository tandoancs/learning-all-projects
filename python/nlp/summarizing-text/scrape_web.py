import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the price element
price_element = soup.find("div", class_="price")

# Extract the price
price = price_element.text

print(price)
