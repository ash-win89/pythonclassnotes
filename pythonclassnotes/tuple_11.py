#tuple datastructure --exactly same as list data type except that it is immutable

a = (4,7,1)
#a[0] = 98 # this will throw you error

#and it will not support any append(), remove(),

#addition operations
b= (7,6,2,'apple')
c = a+b
print(c)


d = a*2
print(d)

#len and count
print(len(b))
print(b.count(2))

#sorting and reversing

#e = b.reverse()
#e = b.sort()
print(b[1])
print(b[0:2])

#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Unpack Tuples:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#extra notes for assignment:
'''
1.how to create tuple using keyword or '(':
t1 = 'a',
print(type(t1))

2.how to create a str inside of an '(':
t2 = ('a',)
print(type(t2))

3.how to create a tuple with integer without using keywords or"(" 
a = 1, 2, 3 (or) a=1,
print(type(a))

4.how to unpack a tuple:
x, y, z = (1, 2, 3)

5.comparing multiple tuples: (not only tuple all sequences will support this)
tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1','2','3')
tuple3 = ('a', 'b', 'c', 'd', 'e')

#the condition is true it will take it as 1 or else false
def cmp(a, b):
    return (a > b) - (a < b)#(1-0)
#using 'cmp' keyword to compare sequences:
print(cmp(tuple1,tuple2))#1

6.finding the maximum and minimum values inside of a sequence;
tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1','2','3')
print(max(tuple1))
print(min(tuple2))

7.The hash() method returns the hash value of an object if it has one. tuple can be hashable but
lists and sets or cannot 
print(hash( (1, 2) ))#ans - -3550055125485641917

8.sorted we can use with tuple and all other data structures:

sorted((7, 2, 1, 5))
# Output: [1, 2, 5, 7]

'''
