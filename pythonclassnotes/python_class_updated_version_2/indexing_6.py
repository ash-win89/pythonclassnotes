
'''
indexing used to  find the position of an element in a sequence
'''

#string indexing
a = 'hello world this is sunday'
#retriving the index position of a word
x = a.index('world')#index-- will find the first occurance of the specified value
print(x)
#to fetch a indexing of a element with in a boundary
y = a.index('l',6,12)
print(y)
#x = a.index('z')# if the particular element is not found 'index()' will throw  error
#print(x)
y = a.find('is')
print(y)
y = a.find('z')
print(y)

#if we pass index number we can retrive data
a = 'los angeles covered by snow'
print(a[20])
print(a[-1])
#slicing is about  getting a sub-string from the given string by using [] or 'slice()'
b = a[4:12]
print(b)

#without giving a starting to slice
print(a[:12])

#without giving a endiong point slice
print(a[12:])

#negative slicing:
print(a[-8:-1])

a= 'london is the capital england'
#skipping steps:
print(a[0:20:3])

#slice(stop),slice(start,stop),slice(start,stop,step)
x = slice(9)
y = slice(-1,-12,-2)
print(a[x])
print(a[y])

#tuple indexing
a = (4,5,8,2,7)
print(a.index(2))

print(a[3])
print(a[-4:-1])
print(a[0:4:2])

