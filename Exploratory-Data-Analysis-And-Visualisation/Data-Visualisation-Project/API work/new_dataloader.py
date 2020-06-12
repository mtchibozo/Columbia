#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:09:21 2019

@author: ap
"""

import config
import requests
import locale 
import time
import getkey
import tmdbsimple as tmdb

api_key = getkey.mykey()
file = open("dataset1.csv", 'w')

mid=[]
dire=[]

tmdb.API_KEY = getkey.mykey()
discover = tmdb.Discover()

for year in range(1980,2020):
    for i in range(1,6):
        response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' +  api_key + '&primary_release_year='+str(year)+'&sort_by=revenue.desc&page='+str(i)+'&language=en-US')
        hr = response.json()
        for i in range(0,len(hr['results'])):
            mid.append(hr['results'][i]['id'])
        time.sleep(0.25)

for mov_id in mid:
    r1=requests.get('https://api.themoviedb.org/3/movie/'+str(mov_id)+'/credits?api_key='+api_key)
    if r1.status_code == 200:
        dr=r1.json()
        name="NA"
        if 'crew' in dr:
            for i in dr['crew']:
                if i['job']=='Director':
                    name=i['name']
                    break
                else:
                    continue
            dire.append(name)
        else:
            print(mid)
            print(dr)
            dire.append(name)
    else:
        dire.append('NA')
        print(r1.status_code)
        
    time.sleep(0.3)


columns = ['id', 'original_title', 'popularity', 'budget', 'revenue', 'genres', 'vote_count', 'vote_average', 'runtime', 'release_date']

line = ';'.join(cat for cat in columns) + '\n'
line='director;'+line
file.write(line)

k=0
for mov_id in mid:
    time.sleep(0.3)
    line1=""

    try:
        mov = tmdb.Movies(mov_id).info()
    except:
        continue
    
    line1 = dire[k]+';'
    for cat in columns:
        if cat == 'genres':
            line1 += '|'.join(x['name'] for x in mov[cat]) + ';'
        else:
            to_write = str(mov[cat]).split(";")
            line1 += ','.join(str(v) for v in to_write) + ';'
    line1 = line1[:-1] + '\n'
    file.write(line1)
    k=k+1