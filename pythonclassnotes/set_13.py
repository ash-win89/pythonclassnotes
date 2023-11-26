#set data type --If we want to represent a group of unique values as a single entity then we
#should go for set.  Duplicates are not allowed.  Insertion order is not preserved.But
a = {4,2,8,9,23}
print(type(a))

'''
#another way to define a set

b = set(range(12))
print(b)
#print(b[4])
#but s = {} this will treat as empty dictionary not a set

#add() --Adds items to the set
a.add(67)
print(a)

#update --To add multiple items to the set.unlike 'extend' operation 'update' operation will do remove duplicates
#each value it will only once

c = {5,2,8,98}
a.update(c, range(3))
print(a)

#copy and clown will work same as list like in set as well

#pop also will remove the random element of the sequence
a.pop()
print(a)

#remove
a.remove(98)
print(a)

#discard --It removes the specified element from the set.
a.discard(67)
print(a)

#clear()
b = {5,3}
b.clear()
print(b)

#mathematical operations that we can perform
a = {4,3,9,8,6}
b= {3,9,1,5,13}

#1.union():--==>We can use this function to return all elements present in both sets
print(a.union(b))
#or
print(a|b)

#intersection():--Returns common elements present in both x and y
print(a.intersection(b))

#or
print(a&b)

#difference(): --returns the elements present in x but not in y
print(a.difference(b))

#or
print(a-b)

#4.symmetric_difference(): --Returns elements present in either x or y but not in both or it will return all values
#except the common vallues
print(a.symmetric_difference(b))
#or
print(a^b)

#to check a set is a superset of another set:
#which is a superset is containing all the elements and more with the comparing set
print({1, 2,3}.issuperset({1, 2}))

#to check a set is a subset of another set:
#which is a subset should has to contain all the elements to which set we are doing comparison
print({1, 2}.issubset({1, 2, 3}))

#to check if both sets are totally different we can use disjoint
print({1, 2}.isdisjoint({3, 4}))



#using membership operators
s = set('hello')
print('h' in s)
print('x' in s)
print(s)

'''

#extra nots for assignment
'''
1.in set we cannot perform nested operations it will lead to the type error
"{{1,2}, {3,4}}
leads to:
TypeError: unhashable type: 'set'"
2.instead of that we can use frozen set 
"
{frozenset({1, 2}), frozenset({3, 4})}"-- this can be possible
'''