import requests
from bs4 import BeautifulSoup as bs
import os

os.system('cls')
URL = "https://coinmarketcap.com/"
page = requests.get(URL)

soup = bs(page.content, "html.parser")
results = soup.find(class_="h7vnx2-2 czTsgW cmc-table")  # table of cryp
# rows of the table by rate
rows = results.find_all("tr")
n = 1
for row in rows:
    cryp = row.find("a", class_="cmc-link")
    if cryp == None:
        n += 1
        continue
    crypname = cryp.find('p', class_="sc-1eb5slv-0 iworPT")
    pric = row.find('div', class_="sc-131di3y-0 cLgOOr")
    if pric == None:
        n += 1
        continue
    price = pric.find('span')
    print(f'{crypname.text} : {price.text}', "\n")
    n += 1
    if n == 22:
        break
