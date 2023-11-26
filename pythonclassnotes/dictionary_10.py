#dictionary comprehensions --If we want to represent a group of objects as key-value pairs then we should go for
#Dictionary.

#to create empty dictionary

a = {}
print(type(a))
b = dict()

#adding elements to a dictionary

a[1] = 'apple'
a[2] = 'cherry'
a[3] = 'kiwi'
a[999] = 'orange'

print(a)

#to access a value from a dictionary
print(a[3])

del a[2]
print(a)

a.clear()  # used to remove all elements
print(a)

del a # to delete the entire dictionary
#print(a)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#to create a empty dictionary
a = dict()
dic = {'a':3,'b':7,'c':9}

#Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

print(len(dic))  #used to find the number of items

#get()-- used to get value associated with that key

print(dic.get('c'))

#using pop in dictionary use the key as well
dic.pop('b')

print(dic)

#popitem used to remove the last item of the dictionary
dic.popitem()

print(dic)

b={'a':5,'b':56,'c':34}
#keys():--It returns all keys associated eith dictionary

print(b.keys())
#values() --It returns all values associated with the dictionary

print(b.values())

#items() --It returns list of tuples representing key-value pairs.
print(b.items())


#copy():--To create exactly duplicate dictionary(cloned copy)

b = {'a':3,'b':7,'c':9}

c = b.copy()
c.popitem()
print(b,c) # b will remain same for copy

#aliasing -renaming

d = b
d.pop('a')
print(d,b)


#comprehend a dictionary

a = {'apple':5,'kiwi':45,'orange':46}
print(a)

s = [a[x] for x in a]
print(s)

#another way of filtering values from dictionary:
#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)


#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

#Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)


#extra notes for assignment:
'''
1.if we dont have  values or keys in our dictionary we can set default values that time it will not
 any key error
dic = {}

print(dic.get('foo','bar'))
the first one is the key second is the default value even if you call 
dic you will get and emptydictionary only

print(mydict.setdefault("foo", "bar"))
#using the above line after if call 'mydict' we might get the answers

2.doing append operation with an dictionary:

d = {}
print(d)
#appending value
d.setdefault('Another_key', []).append("This worked!")
print(d)#ans:{'Another_key': ['This worked!']}

3.merging two dictionaries: using **:

fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
#to merge two dictionaries

fishdog = {**fish, **dog}
print(fishdog)# ans:{'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}

With this technique the foremost value takes precedence for a given key rather than the last ("Cliﬀord" is thrown
out in favor of "Nemo").


4.Getting the minimum or maximum or using sorted depends on iterations over the object. In the case of dict , the
iteration is only over the keys:

adict = {'a': 3, 'b': 5, 'c': 1}
min(adict)
# Output: 'a'
max(adict)
# Output: 'c'
sorted(adict)
# Output: ['a', 'b', 'c']
#To keep the dictionary structure, you have to iterate over the .items() :

min(adict.items())
# Output: ('a', 3)
max(adict.items())
# Output: ('c', 1)
sorted(adict.items())
# Output: [('a', 3), ('b', 5), ('c', 1)]
'''
