

f = open('airlines.csv','rU')

data = f.read()
f.close()

with open('airlines.csv','rU') as f:
    data = f.read()
    for row in f:
        data.append(row)
        
        
with open('airlines.csv','rU') as f:
    data = []
    for row in f:
        data.append(row)
        
##as list comprehension
with open('airlines.csv','rU') as f:
    data = [row for row in f]      
    
##uses split for parsing
with open('airlines.csv','rU') as f:
    data = [row.split(',') for row in f]      
    
##this uses the csv module
import csv
with open('airlines.csv','rU') as f:
        data = [row for row in csv.reader(f)]

#separate the header from the data
header = data[0]
data = data[1:]

##average incidents per airline per year

i = [(float(incident[2]) + float(incident[5])) / 30 for incident in data]

##create list of airline names without star

name = [airline[0].split('*') for airline in data]
[airline[0] for airline in name]


airlines2 = []
for row in data:
    if row[0][1] == '*':
        airlines2.append(row[0][:-1])
    else:
        airlines2.append(row[0])
##list of 1 if there is a star, 0 if there is not
    
star = [len(airline[0].split('*')) - 1 for airline in data]
