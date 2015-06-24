# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:33:39 2015

@author: andyacs
"""

import pandas as pd
movies = pd.read_csv('imdb_1000.csv')
movies.head

import requests
r = requests.get('http://www.omdbapi.com/?t=shawshank+redemption&y=&plot=short&r=json&type=movie') #optional parameters can be deleted
r.status_code
#view raw response text
r.text
#convert to JSON
r.json()['Year']
d = r.json()
d['Year']

##define a function to return the year

def get_movie_year(title):
    r = requests.get('http://www.omdbapi.com/?t='+title+'&y=&plot=short&r=json&type=movie')
    info = r.json()
    if info['Response']=='True':
        return int(info['Year'])
    else:
        return 0
        
##create a samller data frame for testing
        
top_movies = movies.head().copy()

#write a for loop to build a list of years
from time import sleep ##allows you to put a pause on requests
years = []
for title in top_movies.title:
    years.append(get_movie_year(title))
    sleep(1) ##adds 1 sec delay in between requests to API