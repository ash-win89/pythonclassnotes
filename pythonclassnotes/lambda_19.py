#lambda-- it is small and nameless or anonymous function

#if we dont have any name we can assign that anonyomous function with an object using that object we can access the function
add = lambda a:a+10
print(add(50))


#using multiple parameters

y = lambda a,b:a-b
print(y(93256,657893))

#using a lamda function inside of a normal function

def func(para):
    return  lambda a:a*para

obj = func(56)
print(obj(4))
obj1 = func(45)
print(obj(7))


#filter -- used filter particular values based on given conditions

l1 = [34,65,78,9,0,11,23,44]
re = list(filter(lambda x: x%2 == 0,l1))
print(re)


#map -- using map we can apply some operation to all elements which is available in the sequence
l1 = [34,65,78,9,0,11,23,44]
re = list(map(lambda x:x*2,l1))
print(re)


#reduce -- it will by doing some operation it will turn all the sequence elements into a single value

from  functools import reduce

l1 = [34,65,78,9,0,11,23,44]
re = reduce(lambda x,y:x+y,l1)
print(re)

'''
#extra notes for assignments:
'''

'''
1.using lambda converting lowercase value into uppercase
x = map(lambda e :e.upper(), ['one', 'two', 'three', 'four'])
print(x)

2.calling a funcion using lambda function:
def fun(a):
    print(a)

t = (lambda x= 'hello world': fun(x))
t()

3.recursive function with lambda:
lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
print(lambda_factorial(4)) # 4 * 3 * 2 * 1 = 12 * 2 = 24

4.startswith in lambda:

alist = ['wolf', 'sheep', 'duck']
list(filter(lambda x: x.startswith('d'), alist))# Output: ['duck']

5.
h = map(str, [1, 2, 3, 4, 5])
print(list(h))

6.round:
round(1.5) # Out: 2
round(0.5) # Out: 0
'''
