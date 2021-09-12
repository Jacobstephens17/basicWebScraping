from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
tableRows = tbody.contents



prices = {}

for tableRow in tableRows[:10]:
    name, price = tableRow.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

    print(fixed_name + ' is currently valued at ' + fixed_price)
    
print(prices)
