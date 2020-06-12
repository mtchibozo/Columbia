# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:31:01 2019

@author: Max Tchibozo
"""


import requests
from bs4 import BeautifulSoup
import re
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

#We manually add the missing Rotten Tomatoes links

fin_dict["Spider-Man: Far From Home"]["rt"] = "https://www.rottentomatoes.com/m/spider_man_far_from_home"
fin_dict["Daredevil"]["rt"] = "https://www.rottentomatoes.com/m/daredevil"
fin_dict["Hulk"]["rt"] = "https://www.rottentomatoes.com/m/hulk"
fin_dict["Elektra"]["rt"] = "https://www.rottentomatoes.com/m/elektra"
fin_dict["X-Men: The Last Stand"]["rt"] = "https://www.rottentomatoes.com/m/x_men_3_the_last_stand"
fin_dict["Iron Man"]["rt"] = "https://www.rottentomatoes.com/m/iron_man"
fin_dict["The Incredible Hulk"]["rt"] = "https://www.rottentomatoes.com/m/the_incredible_hulk"
fin_dict["Iron Man 2"]["rt"] = "https://www.rottentomatoes.com/m/iron_man_2"
fin_dict["X-Men: First Class"]["rt"] = "https://www.rottentomatoes.com/m/x_men_first_class"
fin_dict["Guardians of the Galaxy"]["rt"] = "https://www.rottentomatoes.com/m/guardians_of_the_galaxy"
fin_dict["Ant-Man"]["rt"] = "https://www.rottentomatoes.com/m/antman"
fin_dict["Captain America: Civil War"]["rt"] = "https://www.rottentomatoes.com/m/captain_america_civil_war"
fin_dict["Superman"]["rt"] = "https://www.rottentomatoes.com/m/superman_the_movie"
fin_dict["Spider-Man"]["rt"] = "https://www.rottentomatoes.com/m/spiderman"
fin_dict["Batman Begins"]["rt"] = "https://www.rottentomatoes.com/m/batman_begins"
fin_dict["The Dark Knight"]["rt"] = "https://www.rottentomatoes.com/m/the_dark_knight"
fin_dict["The Dark Knight Rises"]["rt"] = "https://www.rottentomatoes.com/m/the_dark_knight_rises"
fin_dict["Man of Steel"]["rt"] = "https://www.rottentomatoes.com/m/superman_man_of_steel"
fin_dict["Suicide Squad"]["rt"] = "https://www.rottentomatoes.com/m/suicide_squad_2016"

#We manually add the missing Box Office Mojo links

fin_dict["Captain America"]["bm"] = "https://www.boxofficemojo.com/release/rl1900578305/"
fin_dict["The Punisher"]["bm"] = "https://www.boxofficemojo.com/release/rl1768588801/"
fin_dict["Fantastic Four"]["bm"] = "https://www.boxofficemojo.com/release/rl3864036865/"
fin_dict["Daredevil"]["bm"] = "https://www.boxofficemojo.com/release/rl424445441/"
fin_dict["Elektra"]["bm"] = "https://www.boxofficemojo.com/release/rl1582401025/"
fin_dict["X-Men: The Last Stand"]["bm"] = "https://www.boxofficemojo.com/release/rl1484424705/"
fin_dict["Ghost Rider"]["bm"] = "https://www.boxofficemojo.com/release/rl3579151873/"
fin_dict["Fantastic Four: Rise of the Silver Surfer"]["bm"] = "https://www.boxofficemojo.com/release/rl3679487489/"
fin_dict["Iron Man"]["bm"] = "https://www.boxofficemojo.com/release/rl1482327553/"
fin_dict["The Incredible Hulk"]["bm"] = "https://www.boxofficemojo.com/release/rl2791015937/"
fin_dict["Iron Man 2"]["bm"] = "https://www.boxofficemojo.com/release/rl1515881985/"
fin_dict["X-Men: First Class"]["bm"] = "https://www.boxofficemojo.com/release/rl1434093057/"
fin_dict["Ghost Rider: Spirit of Vengeance"]["bm"] = "https://www.boxofficemojo.com/release/rl3595929089/"
fin_dict["The Avengers"]["bm"] = "https://www.boxofficemojo.com/release/rl709199361/?ref_=bo_shs_sd"
fin_dict["Thor: The Dark World"]["bm"] = "https://www.boxofficemojo.com/release/rl3111421441/"
fin_dict["Captain America: The Winter Soldier"]["bm"] = "https://www.boxofficemojo.com/release/rl3194193409/"
fin_dict["X-Men: Days of Future Past"]["bm"] = "https://www.boxofficemojo.com/release/rl1400538625/"
fin_dict["Guardians of the Galaxy Vol. 2"]["bm"] = "https://www.boxofficemojo.com/release/rl2976089601/"
fin_dict["Avengers: Age of Ultron"]["bm"] = "https://www.boxofficemojo.com/release/rl675644929/"
fin_dict["Ant-Man"]["bm"] = "https://www.boxofficemojo.com/release/rl88245761/?ref_=bo_shs_sd"
fin_dict["Deadpool"]["bm"] = "https://www.boxofficemojo.com/release/rl2588706305/?ref_=bo_shs_sd"
fin_dict["Captain America: Civil War"]["bm"] = "https://www.boxofficemojo.com/release/rl2563409665/weekend/"
fin_dict["Doctor Strange"]["bm"] = "https://www.boxofficemojo.com/release/rl3076752897/"
fin_dict["Spider-Man: Homecoming"]["bm"] = "https://www.boxofficemojo.com/release/rl863208961/"
fin_dict["Thor: Ragnarok"]["bm"] = "https://www.boxofficemojo.com/release/rl2959312385/"
fin_dict["Black Panther"]["bm"] = "https://www.boxofficemojo.com/release/rl2992866817"
fin_dict["Avengers: Infinity War"]["bm"] = "https://www.boxofficemojo.com/release/rl3043198465/?ref_=bo_at_a"
fin_dict["Deadpool 2"]["bm"] = "https://www.boxofficemojo.com/release/rl2488436225/?ref_=bo_sh_tx"
fin_dict["Once Upon a Deadpool"]["bm"] = "https://www.boxofficemojo.com/release/rl4110910977/?ref_=bo_cso_table_7"
fin_dict["Ant-Man and the Wasp"]["bm"] = "https://www.boxofficemojo.com/release/rl2088535553/"
fin_dict["Superman"]["bm"] = "https://www.boxofficemojo.com/release/rl4050814465/weekend/"
fin_dict["Batman & Robin"]["bm"] = "https://www.boxofficemojo.com/release/rl3561326081/"
fin_dict["Constantine"]["bm"] = "https://www.boxofficemojo.com/release/rl3511322113/"
fin_dict["Batman Begins"]["bm"] = "https://www.boxofficemojo.com/release/rl3510994433/"
fin_dict["The Dark Knight Rises"]["bm"] = "https://www.boxofficemojo.com/release/rl3745875457/?ref_=bo_at_a"
fin_dict["Man of Steel"]["bm"] = "https://www.boxofficemojo.com/release/rl4034037249/?ref_=bo_shs_sd"
fin_dict["Wonder Woman"]["bm"] = "https://www.boxofficemojo.com/release/rl578455041/"
fin_dict["Suicide Squad"]["bm"] = "https://www.boxofficemojo.com/release/rl1267172865/"
fin_dict["Guardians of the Galaxy"]["bm"] = "https://www.boxofficemojo.com/release/rl3177416193/"
fin_dict["The Dark Knight"]["bm"] = "https://www.boxofficemojo.com/release/rl3729098241/"




rt_count = 0
imdb_count = 0
bm_count = 0

print("nb movies : "+str(len(fin_dict)))


for i in fin_dict.keys():
    if "rt" in fin_dict[i].keys():
        rt_count += 1
    if "imdb" in fin_dict[i].keys():
        imdb_count += 1
    if "bm" in fin_dict[i].keys():
        bm_count += 1

print("rt : "+str(rt_count))
print("imdb : "+str(imdb_count))
print("bm : "+str(bm_count))

#We have all movie pages from imdb
for movie in fin_dict.keys():
    
    #We first scrape the data from imdb
    url_imdb = fin_dict[movie]['imdb']
    res = requests.get(url_imdb).text
    soup = BeautifulSoup(res,'lxml')
    
    try:
        #Extracting rating (IMDB user rating)
        imdb_rating = soup.find("div","ratingValue").find(itemprop="ratingValue").text
        fin_dict[movie]["imdb_rating"] = imdb_rating
        print("imdb rating : ",imdb_rating)
    except: #movie has no rating
        print(movie)
    
    try:
        tmp = soup.findAll("div","txt-block")
        for k in range(len(tmp)):
    
        #Extracting Release Date
            if "Release Date:" in tmp[k].select("h4")[0].text:
                release_date = str(tmp[k]).split("Release Date:</h4>")[1].split("\n")[0]
                fin_dict[movie]["release_date"] = release_date
                print("Release Date:",release_date)
    
        #Extracting budget        
            if "Budget:" in tmp[k].select("h4")[0].text:
                budget = str(tmp[k]).split("Budget:</h4>")[1].split(" ")[0][:-1]
                fin_dict[movie]["budget"] = budget
                print("Budget : ",budget)
                
        #Extracting Opening weekend USA    
            if "Opening Weekend USA:" in tmp[k].select("h4")[0].text:
                opening_weekend_usa = str(tmp[k]).split("Opening Weekend USA:</h4>")[1].split("\n")[0][:-1]
                fin_dict[movie]["opening_weekend_usa"] = opening_weekend_usa
                print("Opening Weekend USA:",opening_weekend_usa)
                
        #Extracting Domestic Gross
            if "Gross USA:" in tmp[k].select("h4")[0].text:
                gross_usa = str(tmp[k]).split("Gross USA:</h4>")[1].split(" ")[1]
                fin_dict[movie]["gross_usa"] = gross_usa
                print("Gross USA:",gross_usa)
        
        #Extracting Worldwide Gross
            if "Cumulative Worldwide Gross:" in tmp[k].select("h4")[0].text:
                gross_worldwide = str(tmp[k]).split("Cumulative Worldwide Gross:</h4>")[1].split(" ")[1]
                fin_dict[movie]["gross_worldwide"] = gross_worldwide 
                print("Gross worldwide:",gross_worldwide)
    except: #when we have passed the k which contained the above info
        pass
            
    #We then scrape the critic score and audience score from rotten tomatoes
    if "rt" in fin_dict[movie].keys():
        url_rt = fin_dict[movie]['rt']
        res = requests.get(url_rt).text
        soup = BeautifulSoup(res,'lxml')
        try:
            #Extracting critic score from RT
            for item in soup.find("span","mop-ratings-wrap__percentage").text.split(" "):
                if "%" in str(item):
                    critic_score_rt = str(item)[:-1]
                    fin_dict[movie]["critic_score_rt"] = critic_score_rt
                    print("Critic score RT: ",critic_score_rt)
            
            for item in soup.findAll("span","mop-ratings-wrap__percentage")[1].text.split(" "):
                if "%" in str(item):
                    audience_score_rt = str(item)[:-1]
                    fin_dict[movie]["audience_score_rt"] = audience_score_rt
                    print("Audience score RT : ",audience_score_rt)
            
        except:
            pass
        #We then scrape the number of theaters from box office mojo

    if "bm" in fin_dict[movie].keys():
        url_bm = fin_dict[movie]["bm"]
        res = requests.get(url_bm).text
        soup = BeautifulSoup(res,'lxml')    
        
        for items in soup.find_all('span'):
            if "theaters" in items.text:
                theater_string = items.text
                fin_dict[movie]["theaters"] = theater_string.split(" ")[0]
        if "theaters" in fin_dict[movie].keys():
            theaters = fin_dict[movie]["theaters"].replace(",","")
            fin_dict[movie]["theaters"]= float(theaters)
            print("Theaters nb : ",float(theaters))
        
#We add a studio (Marvel, DC) to each movie in fin_dict
start_of_DC_movies = list(fin_dict.keys()).index("Superman and the Mole Men")

for i in range(len(list(fin_dict.keys()))):
    if i < start_of_DC_movies:
        fin_dict[list(fin_dict.keys())[i]]["studio"] = "Marvel"
    else:
        fin_dict[list(fin_dict.keys())[i]]["studio"] = "DC"    
    
def string_to_float(value): #By default, budget has format $xx,xxx,xxx . We want a float instead
    if type(value) == str:
        new_value = value.replace(",","")
        new_value = new_value.replace("$","")
        new_value = float(new_value)
        return new_value
    else: #value is an NA
        return value

           
def find_2020(string): # The movies that were released in 2020 should be removed
    if "2020" in string:
        return True
    if "2021" in string:
        return True
    else:
        return False 
    
for movie in fin_dict.keys():
    fin_dict[movie]["year"] = fin_dict[movie]["release_date"].split(" ")[-2]

df = pd.DataFrame.from_dict(fin_dict, orient='index')
df['budget'] = df['budget'].apply(lambda x: string_to_float(x))
df['opening_weekend_usa'] = df['opening_weekend_usa'].apply(lambda x: string_to_float(x))
df['gross_usa'] = df['gross_usa'].apply(lambda x: string_to_float(x))
df['gross_worldwide'] = df['gross_worldwide'].apply(lambda x: string_to_float(x))

df = df[df['release_date'].map(find_2020) == False]


df.to_csv('superhero_movie_dataframe.csv')





"""
Critic score (RT - DONE)
Audience score (imdb - DONE)
Revenue (imdb - DONE)
Budget (imdb - DONE)
Year produced/released (imdb - DONE)
Number of theaters allocated for the first week after release
Domestic gross (imdb - DONE)
Worldwide gross (imdb - DONE)
Revenue in first weekend (imdb - DONE)
"""