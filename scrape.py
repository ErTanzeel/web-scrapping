from xml.sax.xmlreader import AttributesImpl
from bs4 import BeautifulSoup
import requests
from csv import writer

url="https://opentender.eu/start"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
div = soup.find('ul', class_="portal-links")

with open('scrap.csv','w',encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['country', 'tender']
    thewriter.writerow(header)
    
    country=div.findAll('a',class_=False)
    tender=div.findAll('div', class_=False)
    
    attrs = {k.text: v.text for k, v, in zip(country,tender)}
    print(attrs)
    thewriter.writerow([attrs])

