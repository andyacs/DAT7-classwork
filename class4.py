
import pandas as pd

##read table in pandas

pd.read_table('u.user')

##can also read from a url if it is a .txt file

pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT7/master/data/u.user')

##add separator
pd.read_table('u.user', sep='|')

##specify no header, should not be in quotes otherwise it will set none to a column name
pd.read_table('u.user', sep='|', header=None)

##specify column names and add to data set
user_cols = ['user_id','age','gender','occupation','zip_code']
pd.read_table('u.user', sep='|', header=None, names=user_cols)

##specify index column, you'll see the default disappear and user_id become named index
pd.read_table('u.user', sep='|', header=None, names=user_cols, index_col='user_id')

##create table and save
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('u.user', sep='|', header=None, names=user_cols, index_col='user_id', dtype={'zip_code':str})

#data frame functions
type(users)
users.head()
users.head(10)
users.tail()
users.index ## does not have parantheses because this is an attribute rather than method
users.columns
users.dtypes ##shows data types within table
users.shape ##number of rows and columns as a tuple
users.values ##underlying numpy array

####SELECTING COLUMNS -- in python a column is called a Series
users['gender'] #select single column
users.gender #this is a shortcut, same as above
users.describe()    #quick stat output for all numeric columns
users.describe(include=['object']) ##pulls in all objects into table summary
users.describe(include='all') #all types
users.gender.describe() ##drill down to a specified column
users.age.mean() ##aggregate functions on to a specific series

#####VALUE COUNTS
users.gender.value_counts() ##count per each object
users.age.value_counts() ##creates a histograpm

##ACTITY WITH DRINKS.CSV
import pandas as pd
pd.read_table('drinks.csv')
drinks = pd.read_table('drinks.csv',sep=',')
drinks.columns
drinks.index
drinks.dtypes
drinks.shape
drinks.beer_servinvgs
drinks.beer_servings.mean()
drinks.continent.value_counts()

##FILTERING AND SORTING
users.age < 20 #RETURNS A BOOLEAN FOR EACH VALUE IN THE SERIES
users[users.age <20] ##FILTERED DATA FRAME
young_bool = users.age < 20
users[young_bool] ##returns dataframe referring to young_bool
users[young_bool].occupation #selects filtered column
users[young_bool].occupation.value_counts()
users[(young_bool) & (users.gender=='M')] ##use ampersand and parentheses for OrderOfOps
users[users.occupation.isin(['doctor','lawyer'])]
users[(users.occupation == 'doctor') | (users.occupation == 'lawyer')] ## SAME AS ABOVE ^^

## sorting
users.sort('age') #sort by age, default ASC
users.sort('age', ascending=False)
users.sort(['occupation','age']) ##sort of multiple

##ACTIVITY
drinks[drinks.continent == 'EU']
drinks[(drinks.continent=='EU') & (drinks.wine_servings > 300)].head()
drinks[drinks.continent == 'EU'].beer_servings.mean()
drinks.sort('total_litres_of_pure_alcohol',ascending=False).head(10)
drinks.sort('total_litres_of_pure_alcohol',ascending=False)['country']
drinks.sort('total_litres_of_pure_alcohol',ascending=False)[['country','total_litres_of_pure_alcohol']]

##RENAME COLUMNS
drinks.rename(columns={'beer_servings':'beer', 'wine_servings':'wine'}) #temporarily renames columns
drinks.rename(columns={'beer_servings':'beer', 'wine_servings':'wine'}, inplace=True) ##permanently renames

#RENAME ALL COLUMNS
drink_cols = ['country','beer','spirit','wine','liters','continent']
drinks = pd.read_csv('drinks.csv', header=0, names=drink_cols)
drinks.columns = drink_cols ##permanently changes col's once altered

##HANDLING MISSING VALUES
drinks.continent.value_counts() 
drinks.continent.value_counts(dropna=False) ##removes NA as null-value
drinks.continent.isnull()
drinks[drinks.continent.isnull()] ##RETURNS NULL USE NOTNULL() FOR INVERSE
drinks.continent.isnull().sum() ##CONVERTS TRUES TO 1, COUNTS NULL VALUES
drinks.isnull() ##COVERTS TO DATAFRAME FOR ALL SERIES
drinks.isnull().sum() ##COUNT NULLS FOR EACH SERIES IN DATAFRAME
drinks.isnull().sum(axis=0) ##SUM DOWN THE COLUMN (DEFAULT)
drinks.isnull().sum(axis=1) ##SUM ACROSS THE ROW

##DROP MISSING VALUEw
drinks.dropna() ##drops row if ANY value is missing
drinks.dropna(how='all') ##drops a row only if ALL values are missing
drinks.dropna(inplace=True) ##permanently drops from dataframe

##FILL IN MISSING VALUE
drinks.continent.fillna(value='NA') ##Replaces null value with NA
drinks.continent.fillna(value='NA', inplace=True) ##permanently replaces null

##UFO EXCERCISES
import pandas
ufo = pd.read_csv('ufo.csv')
ufo.shape
ufo['Colors Reported'].value_counts()

#REPLACE SPACES IN COLUMN NAMES
[col.replace(' ','_') for col in ufo.columns] #write list comprehension to programatically remove spaces
#for reports in VA, what is the the most common city
ufo[ufo.State == 'VA'].City.value_counts().head(1)
#print dataframe from all reports in alexandria, va
ufo[(ufo.City == 'Alexandria') & (ufo.State == 'VA')]

#count number of null values from each column
ufo.isnull().sum()

#how many rows will dropping null leave?
ufo.isnull().shape