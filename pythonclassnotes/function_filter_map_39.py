#with lambda:
#filter:

l = [5,3,4,8,9,2,1]
l1 = list(filter(lambda x:x%2==0,l))
print(l1)

'''
#with normal function:
l = [5,3,4,8,9,2,1]

def find_even(x):
    if x%2 ==0:
        return  True
    else:
        return  False
even = list(filter(find_even,l))
print(even)

for i in even:
    print(i)

#with lambda map function
l = [5,3,4,8,9,2,1]

l1 = list(map(lambda x:x*2,l))
print(l1)

l = [5,3,4,8,9,2,1]

def mapping(x):
    return x *x

squared = map(mapping,l)
for i in squared:
    print(i)

'''
#reduce --only return the final value
from functools import reduce

l = [5,3,4,8,9,2,1]
print(reduce(lambda a,b:a+b,l))

#accumulate --will return each steps and also final value
from  itertools import accumulate
print(list(accumulate(l,lambda x,y:x+y)))


