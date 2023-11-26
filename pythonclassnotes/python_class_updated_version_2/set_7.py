'''
it is unordered, it will not allow the duplicates, collections of element in a {}

unordered:
    the items which is declared inside of the set do not have the defined order
'''

a = {2,3,6,7,8,2,3,7.5}
print(a)
#print(a.index(7))
#print(a[4])
print(type(a))
#creating a set using the constructor
b = set(('apple','orange','kiwi'))
print(b)
print(type(b))
b= {45,55,75}
b.add(65)
print(b)

#update operation does not require all the sequence to be set
a = {5,3,4}
b = [9,3,4]
c= {4,3}
a.update(b,c)
print(a)

#a.pop()
#remove if the value not found inside of the set it will throw error
a.remove(9)
print(a)

#mentioned value not present in that set it will not throw error
a.discard(6)
print(a)

#clear()--it will emptty the sequence

a.clear()
print(a)


#
a = {5,3,8,9,1,2}
b = {2,3,1,7,4,11}
print(a.union(b))#  |
print(a.intersection(b))#  &
print(a.difference(b))#  -
print(a.symmetric_difference(b))#  ^

a={7,6,3,8,1,3,4,11,5}
b={7,3,4,5}
print(a.issuperset(b))
print(b.issubset(a))
print(b.isdisjoint(a))

c= frozenset(a)
c.remove(3)
