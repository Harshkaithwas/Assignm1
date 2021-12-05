
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh;'
                         ' Intel Mac OS X 10_15_4)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/83.0.4103.97 Safari/537.36'}

url = "https://www.zomato.com/mumbai"

r=requests.get(url,headers=headers)
soup = BeautifulSoup(r.content, "html.parser")


restroName= soup.find_all('h4',class_='sc-1hp8d8a-0')
print(restroName)

avgPrOne= soup.find_all(class_='sc-1hez2tp-0')
print(avgPrOne)

rating = soup.find_all(class_ = 'sc-1q7bklc-1 cILgox')
print(rating)

url = soup.find_all(class_ = 'sc-fgrSAo ctkAaV')
print(url)

with open("sample.json", "w") as outfile:
    json.dump(restroName, outfile)
    # json.dump( avgPrOne, outfile)
    # json.dump(rating, outfile)
