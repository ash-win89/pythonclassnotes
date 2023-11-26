'''
it is a mutable data structure once defined  we can change the data
will allow duplicates, hetrogeneous , to declare a list use []
'''

a = [5,9,2,3,'hello world']
print(type(a))
print(len(a))
print(a)
#constructor
b = list([6,3,1])
print(type(b))

#inserting datas:
b.insert(1,99)
print(b)

#to add the items to the end of the list
b.append(8)
print(b)

#appending the entire list to another list
a= [4,3,2]
b = [8,9,7]
a.extend(b)
print(a)
a.remove(9)
print(a)

#pop used remove specified element based on position
a.pop(3)
print(a)
a.pop()
print(a)

#used remove the specified elements
del a[0]
print(a)
del a
#print(a)

#to empty the list use 'clear()'
a = [6,4,3,9]
a.clear()
print(a)

a = [6,4,3,9]
a.sort()
print(a)

a.reverse()
print(a)
#if we want to convert a list into a descending orde use first sort then apply reverse on the
#sorted list
a = [1,2,[3,4]]
print(a[2][1])