#collections library in python different types containers like built in containers tuple,set
#container is an object that is used to store diffrent objects we can iterate over them

import collections as c

#Counters -- taking each elements and find how many times that is available in that sequence
# finally it will result as or sub class dictionary because it will return result as dictionary format

#dictionary format
'''
l = [1,3,2,5,6,87,9,2,3,4,5,1,2,1,6,8]
print(c.Counter(l))


#ordered_dictionary --unlike formal dictionary ordered dictionary it remembers the order in which keys were inserted

dic = c.OrderedDict()
dic['a'] =4
dic['b'] =5
dic['c'] =6
dic['d'] =43
dic['e'] =47

# for k,v in dic.items():
#     print(k,v)

dic.pop('a')

dic['a'] =89


for k,v in dic.items():
     print(k,v)


#Defauldict --if we are try to get a key which is not available inside the dictionary it will default value
#defaultdictionary never raises errors
def default():
    return 89

d = c.defaultdict(default)
d['a'] =3
d['b'] =7

print(d['a'])
print(d['b'])
print(d['c'])


d = c.defaultdict(lambda :95)
d['a'] =3
d['b'] =7

print(d['a'])
print(d['b'])
print(d['c'])
print(d['r'])
print(d['z'])


d = c.defaultdict(lambda :95)
d['a'] =3
d['b'] =7


print(d.__missing__('a'))
print(d.__missing__('w'))


#chainmap-- a chain map encapsulates or concatenates many dictionaries into a single unit and it will return
# a list which contains all the dictionaries

d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}
d3 = {'e':5,'f':6}
re = c.ChainMap(d1,d2,d3)
print(re)

#re1 = d1+d2


#namedtuple-- a named tuple returns a tuple object with names for each position

student = c.namedtuple('student',['name','age','classes'])#dont use any keywords as a key
s1 = student('rdj','23','first')

print('the student name is',s1[0])
print('the stude class is',s1.age)

#deque--is optimized list for append and pop operations from both sides

d1 =c.deque([23,45,67,89,21])
d1.popleft()
d1.appendleft(56)
print(d1)

#userdict--we want to control some attributes from dictionary we can do that through 'userdict'

d1 = {'apple':54,'kiwi':34,'orange':25}

class cd(c.UserDict):

    #stop pop operations from dictionary
    def pop(self,s = None):
        raise RuntimeError('you are not authorised remove elements')

    def popitem(self, s= None):
        raise RuntimeError('popitem cannot be done')

d = cd({'a':3,'b':5,'c':8})
#d.pop('a')
d.popitem()
d['e'] = 76
#print(d)
'''

class cl(c.UserList):

    def append(self, s = None):
        raise RuntimeError('you should not add any elements to my list')

    def insert(self,s= None,t =None):
        raise RuntimeError('insert operation being prohibited')

ob = cl([5,3,9,7,6])
#ob.append(9)
ob.insert(3,7)
ob.sort()
print(ob)
#extra notes for assignment:


'''
1.using string and split with counters
import collections

ans = collections.Counter('I am Sam Sam I am That Sam-I-am That Sam-I-am! I do not like that Sam-I-am'.split())
print(ans)

2.if we insert some values in a normal dictionary it will take it as in alphabetical order but in
the orderdictionary always follows FIFO

3.we can set the maxlength in deque if it crosses length of it will remove the first element it will
add the last element:

from collections import deque
d = deque(maxlen=3) # only holds 3 items
d.append(1) # deque([1])
d.append(2) # deque([1, 2])
d.append(3) # deque([1, 2, 3])
d.append(4)
print(d) #ans --(2,3,4)


5.counting on a dictionary values:

from collections import Counter
adict = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5}
Counter(adict.values())
# Out: Counter({2: 2, 3: 1, 5: 3})

# Sorting them from most-common to least-common value:
Counter(adict.values()).most_common()
# Out: [(5, 3), (2, 2), (3, 1)]
# Getting the most common value
Counter(adict.values()).most_common(1)
# Out: [(5, 3)]
# Getting the two most common values
Counter(adict.values()).most_common(2)
# Out: [(5, 3), (2, 2)]

6.we can use it on string as well

astring = 'thisisashorttext'
astring.count('t')
# Out: 4

from collections import Counter
Counter(astring)
# Out: Counter({'a': 1, 'e': 1, 'h': 2, 'i': 2, 'o': 1, 'r': 1, 's': 3, 't': 4, 'x': 1})

'''