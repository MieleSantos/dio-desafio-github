import requests
from bs4 import BeautifulSoup

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, "html.parser")

temperatura = soup.find("span", class_="_block margin-b-5 -gray")

# print(soup.prettify())
print(temperatura.string)
