import h11
import requests
from bs4 import BeautifulSoup



r = requests.get('https://apexlegendsstatus.com/current-map/battle_royale/pubs')
print(r)

doc = BeautifulSoup(r.text, 'html.parser')

mapList = doc.find("div", class_="row")
mapRow = mapList.contents

current, next, next2 = mapRow[3:6]
print(current.h3.string)
print(next.h3.string, next.p.contents)
print(next2.h3.string, next2.p.contents)