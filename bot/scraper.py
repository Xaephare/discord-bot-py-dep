import requests
from bs4 import BeautifulSoup


r = requests.get('https://apexlegendsstatus.com/current-map/battle_royale/pubs')
print(r)

doc = BeautifulSoup(r.text, 'html.parser')

mapList = doc.find("div", class_="row")
mapRow = mapList.contents

map = list((mapRow[3:6]))
time = []
time.append(map[1].p.text.rsplit('starts', 1)[1])
time.append(map[2].p.text.rsplit('starts', 1)[1])
print(map[0].h3.string)
print(map[1].h3.string, "starts"+time[0])
print(map[2].h3.string, "starts"+time[1])