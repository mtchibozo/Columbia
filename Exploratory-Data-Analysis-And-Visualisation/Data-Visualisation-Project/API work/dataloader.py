import tmdbsimple as tmdb
import pandas as pd
import time

tmdb.API_KEY = '86700e89f7f8b6cd05366d1e74405f1c'

fichier = open("dataset.csv", 'w')



discover = tmdb.Discover()

#print(discover.movie(page = 3))

movies_id = []

for year in range(1980,2020):
    for i in range(1,14):
        print(i)
        for mov in discover.movie(sort_by='revenue.desc', year=str(year), page = i)['results']:
            movies_id.append(mov['id'])
        
        time.sleep(0.25)


columns = ['id', 'original_title', 'popularity', 'budget', 'revenue', 'genres', 'vote_count', 'vote_average', 'tagline', 'runtime', 'release_date']

line = ';'.join(cat for cat in columns) + '\n'
fichier.write(line)

i = 1

for mov_id in movies_id:
    time.sleep(0.3)

    try:
        mov = tmdb.Movies(mov_id).info()
    except:
        continue
    if mov['adult']:
        continue

    line = ''
    for cat in columns:
        if cat == 'genres':
            line += '|'.join(x['name'] for x in mov[cat]) + ';'
        else:
            to_write = str(mov[cat]).split(";")
            line += ','.join(str(v) for v in to_write) + ';'

    line = line[:-1] + '\n'
    fichier.write(line)
    print(i)
    i += 1

    


#identity = tmdb.Movies(2501)
#print(identity.info().keys())
#print(identity.info()['production_companies'])
#print(identity.keywords())
#print(identity.keywords().keys())