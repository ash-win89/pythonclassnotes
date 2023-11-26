#a loop used to go through or iterate over a sequence -- for loop
#
'''
a = (23,45,76,89)

for i in a:#fetch each elements and print them into next lines
    print(i)



#if case inside of for loop
a = (23, 45, 76, 89)

for i in a:
  if i%2 == 0:
    print(i)


#break operation inside of for loop:

fruits = ['kiwi','lemon','cherry','guaua','orange']

for fruit in fruits:
    if fruit == 'guauas':
        break
    print(fruit)
else:
    print('end of the loop')


#continue operation inside of for loop:

fruits = ['kiwi','lemon','cherry','guaua','orange']

for fruit in fruits:
    if fruit == 'guaua':
        continue
    print(fruit)



#else with for loop-- when the for loop get closes then else case will execute

fruits = ['kiwi','lemon','cherry','guaua','orange']

for fruit in fruits:
    print(fruit)
else:
    print('end of the loop')





# a loop inside of a loop is a nested loop
fruits = ['apple','orange','kiwi','grapes']
colors = ['red','green','yellow']

for i in fruits:
    for j in colors:
        print('the fruit color is {} and the fruit name is {}'.format(j,i))




for  i in range(10):
    for j in range(10-i,10+i):
        print(j,end=' ')

    print()


#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


for i in range(10):
    for j in range(i):
        print(i, end='')
    print()

for i in range(12):
    if i ==11:
        print('helloworld')
    else:
        print(i)



fruits = ['apple','orange','kiwi','grapes']
colors = ['red','green','yellow']

for i,j in enumerate(colors):
    print(i,j)

'''
fruits = ['apple','orange','kiwi','grapes']
colors = ['red','green','yellow']

for i,j in zip(fruits,colors):
    print(j,i)

'''

#extra notes for assignments:
"""
1.'enumerate" If you want to loop though both the elements of a list and have an index for the elements as well, you can use
Python's enumerate function:
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)

enumerate will generate tuples, which are unpacked into index (an integer) and item (the actual value from the list).
The above loop will print
(0,'::', 'one')
(1,'::', 'two')
(2,'::', 'three')
(3,'::', 'four')

2.type checking with for loops
The main use case for the for...else construct is a concise implementation of search as for instance:
a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("no exception")

3.directly accessing a dictionary values using for loops:
for value in d.values():
    print(value)
or:
for key, value in d.items():
    print(key, "::", value) 
    
4.unicode using to traverse through an array as 'i':

from array import *
my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i)     
  
5.printing indexes and values at a time:

x = (10,20,30,40,50)
for var in x:
    print("index "+ str(x.index(var)) + ":",var)
    
6. for loop for nested sequences:

x = [(1,2), (3,4), (5,6)]

for a, b in x:
    print(a, "plus", b, "equals", a+b)
    
7. printing all the dictionary values  with for loop:

stocks = {
        'AAPL': 187.31,
        'MSFT': 124.06,
        'FB': 183.50
    }

for key, value in stocks.items() :
    print(key + " : " + str(value))
    
    
8.using randint to give numbers and add them into a nested sequence handle them with for loop:

import numpy as np
#print(np.random.seed(0))  # seed for reproducibility
x = np.random.randint(10, size=6)
y = np.random.randint(10, size=6)

#printing each sequence values:
for val in x:
    print(val)


for val in y:
    print(val)
    

#handling two dimensional arrays:
z = np.array([x, y])

for val in z:
    print(val)                  


#printing two dimensional array values as normal each values in the next lines using '.editor'

#9.reading a csv values using pandas and printing the rows and it labels:

import pandas as pd
df = pd.read_csv('category.csv')
df = pd.DataFrame(df)
#formal reading:
for val in df['445110']:
    print(val)

#finding the labels and rows:

# for label, row in df.iterrows():
#     print(label)
#     print(row)
    
#to explore more about for loop check: "https://www.dataquest.io/blog/tutorial-advanced-for-loops-python-pandas/"    
10.to check all the files inside of an directory and print them name using for loop

import os
for root, folders, files in os.walk(root_dir):
    for filename in files:
        print root, filename        #still some more options also there like
or:
#formally used one:
for files in os.listdir(dir):
     f = os.path.join(dir, files)

     if os.path.isfile(f):
        filelist.append(files)        

'''
