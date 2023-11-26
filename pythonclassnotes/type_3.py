#to find what kind of data type we can use type keyword

a =3
b=0b01
c = 0o654
d= 0x98ad
e='hello world' #string is a sequence
f = True
g = 5+7j
i = None
j = 8.976523

#type keyword will return that given data types falls under which category
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(i))
print(type(j))


'''
#Extra notes for assignment
1.if we have a float value in between the quotes  we can convert it using 'float' value cant use int
a='123.456' # ValueError: invalid literal for int() with base 10: '123.456'
b=float(a)
c=int(a)
d = int(b)# 123

2. using "\n" kind of special chars used to break the lines it will only break the string into next
line '\t' will give 4 spaces in between the strings
ans = json.dumps(entries)
#print(entries)
print(ans)
file = open('result.json','w')
file.write(ans)

3.if we want to add only member we can define that like as follows that would be not string 

one_member_tuple = 'Only member',
print(type(one_member_tuple))

'''