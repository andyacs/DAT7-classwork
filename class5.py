# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:54:49 2015

@author: andyacs
"""

drink_cols = ['country','beer','spirit','wine','liters','continent']
drinks = pd.read_csv('drinks.csv',header=0,names=drink_cols,na_filter=False)

#for each continent, calculate the mean beer servings
drinks.groupby('continent').beer.mean()

#all columns
drinks.groupby('continent').mean()

#calculate statistics for beer by continent
drinks.groupby('continent').beer.describe()

#created dataframe with the statistics using agg

drinks.groupby('continent').beer.agg(['count','mean','median','min','max'])

#dataframe for all columns
drinks.groupby('continent').describe()

"""ACTIVITY """

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('u.user', sep='|', header=None, names=user_cols, index_col='user_id', dtype={'zip_code':str})

##COUNT EACH OCCUPATIONS
users.groupby('occupation').occupation.count()

##calculate mean age for each occupation

users.groupby('occupation').age.mean()

##for each occupation, calculate the min and max age

users.groupby('occupation').age.agg(['min','max'])

##for each combination of occupation and gender calulate the mean age

users.groupby(['occupation','gender']).age.mean()