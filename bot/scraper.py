import requests
from bs4 import BeautifulSoup



def scraper():
    
    r = requests.get('https://apexlegendsstatus.com/current-map/battle_royale/pubs')
    #prints response code 200 is success
    #print(r)

    doc = BeautifulSoup(r.text, 'html.parser')

    mapList = doc.find("div", class_="row")
    mapRow = mapList.contents

    map = list((mapRow[3:6]))
    time = []
    time.append(map[1].p.text.rsplit('starts in', 1)[1])
    time.append(map[2].p.text.rsplit('starts in', 1)[1])

    current = [map[0].h3.string, map[1].h3.string, map[2].h3.string]
    currentTime = [time[0],time[1]]


    # print(current)
    # print(currentTime)

    return current,currentTime