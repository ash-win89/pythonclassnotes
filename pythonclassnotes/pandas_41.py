#pandas is a python library used to analyze data used to work data sets
#used to clean data way faster to read data comparison, merge,describe,dtypes,correlation
#average,min,max
#creating a dataset
import pandas as p
import pandas as pd
'''
dict = {
    'actors':['rdj','chris','ryan'],'movies':['ironman','thor','grayman']
}#dataset

df = p.DataFrame(dict)#this line will convert the dataset as dataframe
print(df)

#series in pandas -- it is a column in a table one dimensional array

l = [34,23,67,89]# inttype
l1 = [34,23,67,89,'hello']#object
ser = pd.Series(l1)#it will form a column and it will show the data types as well
print(ser)

#indexing with pandas
ind = pd.Series(l, index=['x','y','x1','y1'])
print(ind['x1'])# ans=67
print(ind)

#key/value object as series

dic = {'apple':34,'orange':56,'cherry':45}#forming a dataframe (table)
ans = pd.Series(dic)
print(ans)
#passing index
ans = pd.Series(dic,index=['apple','cherry'])#filtering
print(ans)

#what is a dataframe --a table with rows and columns or a 2 dimensional data
dict = {
    'actors':['rdj','chris','ryan'],'movies':['ironman','thor','grayman']
}
df = pd.DataFrame(dict)
#print(df)

#locating a row
#print(df.loc[1])#return that row as a column with titles
#print(df.loc[[0,0,1]])#how many times we are passing row value it will that many times


#indexing two sequences

dict = {
    'actors':['rdj','chris','ryan'],'movies':['ironman','thor','grayman']
}

ans = pd.DataFrame(dict, index=['marvel','dc','hollywood'])#forming row title
print(ans)

#locating indexes based name
print(ans.loc['marvel'])#title of the row as a name title columns, values

df = pd.read_csv('category.csv')
#print(df)#return entire csv into terminal
df = pd.DataFrame(df)
#print(df)
# #converting dataframe  as string
#print(df.to_string())#it will form pretty table space along with count
#
#print(pd.options.display.max_rows)#the maximum data it will print terminal
# #printing required columns setting to max
#pd.options.display.max_rows = 300000

df = pd.read_json('csvjson.json')
print(df)

#first datas
df = pd.read_csv('category.csv')
#print(df.head())
#last datas
#print(df.tail())
#printing the entire details about the csv
#print(df.info())
print(df.describe())
'''
#data cleaning- fixing a bad data to formal ,emptycells,wrong format,duplicate
#removing empty cells
df = pd.read_csv('category.csv')
#df1 = df.dropna()#it will remove all the null values
#print(df1)
#creating csv
# df = pd.read_json('csvjson.json')
# df1 = pd.DataFrame(df)
# df1.to_csv('sample.csv')
#replacing null values
df1 = df.fillna(0)
print(df1)
print(df1.to_csv('sample.csv'))
