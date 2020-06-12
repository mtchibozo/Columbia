import requests
import imdb as imdb
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_films_based_on_Marvel_Comics_publications"

res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
links={}
for items in soup.find('table', class_='wikitable sortable').find_all('i'):
    links[items.a.text]="https://en.wikipedia.org"+items.a['href']
    

URL1 =  "https://en.wikipedia.org/wiki/List_of_films_based_on_DC_Comics_publications"

res1 = requests.get(URL1).text
soup1 = BeautifulSoup(res1,'lxml')

for items in soup1.find('table', class_='wikitable sortable').find_all('tr'):
    if len(items.find_all('i')) != 0:
        links[items.find_all('i')[0].text]= "https://en.wikipedia.org"+items.find_all('i')[0].a['href']
fin_dict={}

for i in links:
    fin_dict[i]={}

for j in links:
    res1 = requests.get(links[j]).text
    soup1 = BeautifulSoup(res1,'lxml')
    for items in soup1.find_all('a'):
        if items.has_attr('href'):
            if items['href'].startswith("https://www.rottentomatoes.com/m/"):
                fin_dict[j]['rt']=items['href']
            if re.match("^https://www.imdb.com/title/tt[^/]+/$",items['href'])!=None:
                fin_dict[j]['imdb']=items['href']
            if items['href'].startswith("https://www.boxofficemojo.com/movies/?id="):
                fin_dict[j]['bm']=items['href']
                

