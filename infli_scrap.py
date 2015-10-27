#scrapping the inflibnet.ac.in jobs page

from bs4 import BeautifulSoup
from lxml import html
import requests

page = requests.get('http://inflibnet.ac.in/jobs/')
tree = html.fromstring(page.text)

#node you want to scrap, using xpath syntax 
notifs = tree.xpath('//font[@class="text"]/text()')

for noti in notifs:
    s = noti.strip()
    if not s:
        continue
    else:    
        print(">"),s
        
