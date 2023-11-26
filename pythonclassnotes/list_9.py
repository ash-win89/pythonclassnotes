#data structures--there are five types of data structures are there list, tuple, dictionary,set,range
#byte arrays also there
#Lists are used to store multiple items in a single variable.
#list--If we want to represent a group of individual objects as a single entity where
# insertion order preserved and duplicates are allowed, then we should go for List.
#insertion order preserved.,heterogeneous objects are allowed.
'''Ordered
When we say that lists are ordered, it means that the items have a defined order, and that
order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
Since lists are indexed, lists can have items with the same value:
List items can be of any data type:
'''

l = [] #creating empty list
print(type(l))
#we can create list with elements

l = [45,34,23,98,76,True,'helloworld']
print(l)

#using list keyword

a = list(range(2,34))
print(a)

#converting a string into a list it will split each letter as a element

a = 'hello world'
l = list(a)
print(l)

#using split operation against a string to use to break on white space

b = 'hello everyone how are you'
l = b.split()
print(l)


#nested lists -- a list inside of another list
c = [30,20,50,[4,2,8]]

print(c[3][2])  #way of accessing nested elements
#normally using indexing  we can access all the elements in list
print(c[2])


#using slice operator
n = [18,16,14,12,10,8,6,4,2,6]
print(n[2:8:2])  #accessing based on steps
print(n[3:9])
print(n[1:100]) #end boundary out of range it will give till end

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Note: The length of the list will change when the number of items inserted does not match the number of items replaced.
#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)




#we can modify the list content based on indexing
n = [18,16,14,12,10,8,6,4,2,6]
n[4] = 99
print(n)

#we can traverse through a sequence using loops

#for i in n:
    #print(i +2)


#important functions of list:

n = [18,16,14,12,10,8,6,4,2,6]
#len()-- used to find the how many values are there in that list
print(len(n))

#count() --It returns the number of occurrences of specified item in the list
print(n.count(6))

#index() -- returns the index of first occurrence of the specified item.

print(n.index(12))

#we can use membership operators
print(4 in n)


#manipulating list:

#append() --to add item at the end of the list.

l = [1,4,7]
l.append(9)
print(l)

#insert() --To insert item at specified index position

l.insert(1,33)#the 1 is position and 3 is the value
print(l)

#if you give out of range the value will  be added into end of the list
l.insert(100,4)
print(l)

#extend() --To add all items of one list to another list
l1 = [55,44]
l1.extend(l)
print(l1)

#The extend() method does not have to append lists, you can add any iterable
# object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove()--to remove specified item from the list.If the item present
#multiple times then only first occurrence will be removed.
l1.remove(44)
print(l1)

#pop()--It removes and returns the last element of the list.

a =[4,2,9,6,7]
#the position we can pass to remove the data
a.pop(2)
print(a)
a.pop()
print(a)
#ordering elements of list

a =[4,2,9,6,7]
#reverse()--to reverse() order of elements of list.
a.reverse()
print(a)


#sort() --For numbers ==>default natural sorting order is Ascending Order
#For Strings ==> default natural sorting order is Alphabetical Order
#1st way
a.sort()
print(a)
a.reverse()
print(a)

#2nd way

#Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#You can also customize your own function by using the keyword argument key = function.
#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Luckily we can use built-in functions as key functions when sorting a list.
#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#if it is hetrogeneous we will get error

#aliasing and cloning will affect to the original

x = [7,3,5,9]
y = x   #renaming or aliasing
y.pop()
print(x,y)

#copying will affect the duplicates only

y = x.copy()
y.pop()
print(x,y)

#method2 for copying:
#Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#using operators on list

a = [4,2,8,5]
b = [5,3,2]

c = a+b
print(c)

#if we try to add a int we will get error
#c+45 #this will be error
d=c+[45] #this is valid
print(d)

#repetition operator
a = [5,3,2,1]
d = a*2
print(d)

#alphabetical order comparison
x = ['dog','cat','rat']
y = ['Dog','Cat','Rat']

print(x ==y)
print(x != y)



#first element based
x = [30,50,2,3]
y = [25,45,33,1,3]

print(x>y)
print(x<y)


#clear() --to remove all elements of List.
x.clear()
print(x)


#list comprehensions

s = [i*2 for i in y]
print(s)

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]

#Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

#Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

#You can set the outcome to whatever you like:
newlist = ['hello' for x in fruits]

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

newlist = [x if x != "banana" else "orange" for x in fruits]




#arrays:for extra assignment use numpy:;
'''
1.add items to and numpy array:

my_array = array('i', [1,2,3,4,5])
c=[11,12,13]
my_array.fromlist(c)

2.we can add different types of datas its a hetrogeneous:
# Append an element of a different type, as list elements do not need to have the same type
a = [1, 2, 3, 4, 5]
b = [8, 9]
a.append(b)

my_string = "hello world"
a.append(my_string)
ans:
# a: [1, 2, 3, 4, 5,  [8, 9], "hello world"]

3.index keyword validation 
a= [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
#to check the 7th index values is 7:which is first one is indexing value second one is actual value
a.index(7, 7)#ans :7
a.index(7, 8) # ValueError

4.we can use 'pop()' to remove the particular item by passing the index of the particular item:
a= [0, 1, 5, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
a.pop(2)
# Returns: 5
# a: [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

5.we can sort a list in descending order:
a= [1, 2, 3, 4, 5, 6]
a.sort(reverse=True)
print(a)

6.how to print reverse format a list without using 'reverse' keyword:
a= [1, 2, 3, 4, 5, 6]
print(a[::-1])

7.one more method for reverse a list:
a= [1, 2, 3, 4, 5, 6]
b = list(reversed(a))
print(b)

8.advance slicing:
data = 'chandan purohit22 2000'

name_slice = slice(0,19)
age_slice = slice(19,21)
salary_slice = slice(22,None)
#assuming data fields of fixed length
#now we can have more readable slices
print(data[name_slice]) #chandan purohit
print(data[age_slice]) #'22'
print(data[salary_slice]) #'2000'

9.reading multiple non equal length sequence using for loop:
import itertools

alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']
for a,b,c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)
10.while using comparison operators on two sequence it will check the first two values if both
values are equal it will next values

11. how we can intialize a list with fixed numbers:
my_list=[{1}] * 10

print(my_list)
my_list[0].add(2)
print(my_list)

12.#simple program to convert a nested loop to normal loop:

data = [[1,2],[3,4],[5,6]]

formal = []
for l in data:
    for e in l:
        formal.append(e)

print(formal)    

13.#adding two lists using for loop- basically  we can concatenate two lists but using for loop we can add them:

a = [233,344,455,655]
b = [234,123,456,987]

add = []
for i,j in zip(a,b):
    add.append(i+j) #here we can use whatever operator we want to use

print(add)

13. matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# s = [[row[i] for row in matrix] for i in range(len(matrix))]
# print(s)
#elaborate version
for i in range(len(matrix)):
    for row in matrix:
        print(row[i],end='')
    print()
    
14.groupby operation:

a)from itertools import groupby

things = [["animal", "bear"], ["animal", "duck"], ["vehicle", "harley"], ["plant", "cactus"], \
["vehicle", "speed boat"], ["vehicle", "school bus"]]
dic = {}
f = lambda x: x[0]
for key, group in groupby(sorted(things, key=f), f):
    dic[key] = list(group)
print(dic)
#{'animal': [['animal', 'bear'], ['animal', 'duck']], 'plant': [['plant', 'cactus']], 'vehicle': [['vehicle', 'harley'], ['vehicle', 'speed boat'], ['vehicle', 'school bus']]}
  
  
b)
from itertools import groupby

list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), \
'wombat', 'mongoose', 'malloo', 'camel']
c = groupby(list_things, key=lambda x: x[0])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)    

15.how to find the small elements,large elements in a list and how to delete small element from a list:

import heapq
numbers = [1, 4, 2, 100, 20, 50,1111, 32, 200, 150, 8]
print(heapq.nlargest(4, numbers))
import heapq
numbers = [1, 4, 2, 100, 20, 50,1111, 32, 200, 150, 8]
print(heapq.nlargest(4, numbers))
print(heapq.nsmallest(2,numbers))

16.how to apply heapq on list of dictionaries:
import heapq

people = [
{'firstname':'John', 'lastname': 'Doe', 'age': 30},
{'firstname':'Jane', 'lastname': 'Doe', 'age': 25},
{'firstname':'Janie', 'lastname': 'Doe', 'age': 10},
{'firstname':'Jane', 'lastname': 'Roe', 'age': 22},
{'firstname':'Johnny', 'lastname': 'Doe', 'age': 12},
{'firstname':'John', 'lastname': 'Roe', 'age': 45}
]

oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
print(oldest)
# Output: [{'firstname': 'John', 'age': 45, 'lastname': 'Roe'}, {'firstname': 'John', 'age': 30,'lastname': 'Doe'}]
youngest = heapq.nsmallest(2, people, key=lambda s: s['age'])
print(youngest)

16.poping up small elements from a list using heapq:

import heapq
numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8]
heapq.heapify(numbers)
heapq.heappop(numbers) # 2
print(numbers)

17.list comprehension with conditions:

s = [1,2,3,4,5,6,7,7]
ans = [a * 2 for a in s if a > 4]
print(ans)
'''


