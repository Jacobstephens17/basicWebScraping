from bs4 import BeautifulSoup
import requests
import re

searchTerm = input("What product are you looking for?")

url = "https://unsplash.com/s/photos/{searchTerm}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

image = doc.body.contents

