# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:02:43 2015

@author: andyacs
"""

with open('chipotle.tsv', 'rU') as f:
    data = f.read()
    
with open('chipotle.tsv', 'rU') as f:
    data = []
    for row in f:
        data.append(row)
        
##create header and footer
        
header = data[0]
footer = data[1:]