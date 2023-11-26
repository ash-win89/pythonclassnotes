#Combinations method in Itertools Module
import itertools
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 2))
print(b) #ans --[(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

#You can also ﬁnd all the 3-combinations:
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 3))
print(b)

def is_even(x):
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.dropwhile(is_even, lst))
print(result)   #[13, 14, 22, 23, 44]

#instead of using 'zip' to put multiple sequence in a for loop we can use 'itertools' -zip longest

from itertools import *

a = [i for i in range(5)] # Length is 5
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # Length is 7
for i in zip_longest(a, b):
    x, y = i # Note that zip longest returns the values as a tuple
print(x, y)

#itertools.takewhile enables you to take items from a sequence until a condition
# ﬁrst becomes False .

def is_even(x):
    return x % 2 == 0
lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.takewhile(is_even, lst))
print(result)

#ans--[0, 2, 4, 12, 18] .


#Repeat something n times:
for i in itertools.repeat('over-and-over', 3):
    print(i)

#cycle is an inﬁnite iterator
itertools.cycle('ABCD')

#multiplication with itertools:

a=[1,2,3,4]
b=['a','b','c']
product(a,b)

for i in product(a,b):
    print(i)


#Use itertools.chain to create a single generator
# which will yield the values from several generators in sequence.

from itertools import chain
a = (x for x in ['1', '2', '3', '4'])
b = (x for x in ['x', 'y', 'z'])
' '.join(chain(a, b)) # ans --'1 2 3 4 x y z'