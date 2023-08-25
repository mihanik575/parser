
import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0"
}

resp = requests.get(url, headers=headers).text
soup = BeautifulSoup(resp, "lxml")
# print(resp.encode("utf-8"))

tbody = soup.find("tbody")
coins = tbody.find_all("tr")

print(coins)
for coin in coins:
    name = coin.find(class_ = "crypto-symbol")
    price = coin.find_all("td")[-2]
    if  name:
        print(f'{name.text}: {price.text}')
