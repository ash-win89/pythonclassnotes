'''
lambda --use to define a anonymous (or) nameless function using the lambda we can declare a function
in a line it can take any number of arguments it have only one expression or
 only one result or you can have only one return statement

lambda arguments:expression
 power of lambda function use them as an anonymous function inside another function
'''
'''
a = lambda: print('hello world')
a()

add = lambda x: 6754+x
print(add(5))

sub = lambda a,b,c: a-b-c
print(sub(77,44,22))

#arbitrary arguments function
arbit = lambda *tuple: print(tuple)
arbit('a','b',7,2)

#arbitrary keyword argument function
karbit = lambda **dict: print(dict)
karbit(a=54,b=67,c=12)

#keyword argument function
simplkey = lambda a,x: print(x+a)
simplkey(x=6,a=89)

#we cannot perform local scope with lambda
x =90
loc = lambda: print(x)
loc()

def hello(n):
    return  lambda a:a *n

mul = hello(8)
print(mul(4))
square = hello(5)
print(square(5))

#comprehensions:
#list
a = [6,2,4,9,1]
re = [x*2 for x in a]
#print(re)

#for loop with lambda function: default parameter function

ans = [lambda arg = x: arg*10 for x in range(1,5)]

# for i in ans:
#     print(i())#we need to call i with parenthesis

#lambda function with multiple statements: usually lambda will not allow the multiple function

l = [[2,3,4],[1,4,161,64],[3,6,19,12]]

sortList = lambda x:(sorted(i) for i in x)
ans = sortList(l)
for i in ans:
    print(i)
#f is sortlist function ans x is the l --list means f(x)
secondBiglist = lambda x,f: [y[len(y)-2] for y in f(x)]
res = secondBiglist(l,sortList)
print(res)



#using the filter keyword in a lambda function:

l = [4,2,7,9,6,8,1,3]

#using the filter giving the condition:
filter_list = list(filter(lambda x: x%2 ==0, l))
filter_list1 = list(filter(lambda x:x%2 !=0,l))
print(filter_list)
print(filter_list1)


l1 = [40000,30000,25000,10000,20000,15000]
ans = list(filter(lambda sal: sal<=20000,l1 ))
print(ans)

l1 = [40000,30000,25000,10000,20000,15000]
#map --takes the function list of arguments apply some operation on every elemet
incre = list(map(lambda x:x+1000,l1))
print(incre)

animals = ['kitty','shepard','bengal tiger','african cat','africa lion']
uppercasing = list(map(lambda x: x.upper(),animals))
print(uppercasing)
'''
#reduce --- used to reduce sequce

l1 = [40000, 30000, 25000, 10000, 20000, 15000]

from  functools import reduce
total_salary = reduce(lambda x,y: x+y,l1)
print(total_salary)

from functools import reduce
l = [3,2,8,5,4,9,7,1]

#finding the maximum value inside of the list:
max = reduce(lambda a,b:a if a>b else b, l)
print(max)

