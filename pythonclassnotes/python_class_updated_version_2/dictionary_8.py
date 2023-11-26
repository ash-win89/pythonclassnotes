'''
dictionary in python  is a collection of key value pair using those keys to map we can retrive
the value
'''

a = dict()
print(type(a))
b = {}
print(type(b))
a[1] = 'one'
a[2] = 'two'
print(a)

print(len(a))
print(a[1])
b = {'a':'apple','b':'ball','c':{1:'car',2:'cat'}}
print(b['c'][2])

c = {'i':'carrot','j':'banana','k':'cherry','l':'watermelon','c':'cat'}

#clear()
#c.clear()
print(c)

dup = c.copy()
print(dup)
dup.pop('c')
print(dup)
dup.popitem()
print(dup,c)
#rename
d = c
d.pop('j')
print(d)
print(c)

print(b.get('c'))
print(b.items())
print(b.keys())
print(b.values())

#overriding 'b' already nested dictionary associated with 'c'-key and dictionary 'c' also
#having key called 'c' this 'c' key override b dictionary's 'c' key
b.update(c)
print(b)