#build in functions --print,for,if
#user defined functions -- types function,parmeter,arbitrarys, kwagrs,default,keywords,local, global

#it is a reusable code, and it will only executes when its being called while calling it will return the data
#def-- we have to use 'def' keyword to define a function in python
#1.normal
#while defining a function if we pass any data - its known as parameters
#while calling a function if we pass any data --its known as arguments

def hello():
    #print('say hello to everyone!! to using print')
    #return 'this message is coming from return'
    print('hello')
#print(hello())
#hello()

#parameters-- we can pass datas using parameters inside of a function assign variables in the function is parameters
#parameters-- while defining a function giving variable names consider as parameters
#arguments -- the datas the we are assigning with parameters while calliing the function that is arguments
#parameters are acts like a variables to the function and arguments are the values which assign to the variables
def add(x):
    print('the value inserted is',x,'addion with 5',x+5)

#add(6)
# add(5)
# add(55)
# add(34)

def sub(x,y):
    print(x)

#sub(4556,566)
#sub(56)

#arbitrary functions-- while calling a function we are not sure how many arguments that being passed inside of our
#function we have to add '*' before the parameter that function is a arbitrary function it will convert the parmeter as a sequence
#so that parameter will act as a sequence and it will store all datas
#arbitrary -not preplanned in this scenario we dont know how much arguments
a = ['hello','world']
def channels(*name):
    print('the name of channel position is',name[1]+name[5])
    print(type(name))

#channels('e','star','zee','k','sun','maa')

#keyword arguments--we can pass arguments with key=value format
'''
def hero(darkknight,thor,superman):
    print('the hero name of  movie superman',superman)

hero(superman='henry cavil',darkknight='chritianbale',thor='chris hemsworth')





#kwargs functions-- it store the values like a dictionary we can access those values based on keys:

def dictfunc(**a):
    print('the second element of the passed values',a['batman'])
    print(type(a))
dictfunc(thor='marvel',batman = 'dc', f7= 'wb')


#default parameter-- a function which has it own value if user passes any values it will override the default
#if user passes nothing it will return the default value

def city(cap = 'newyork'):
    print('the capital of united states',cap)

city('los angeles')
city()
city('san francisco')


#passing a list as an argument:

def listcall(a):
    for i in a:
        print(i)

l1 = [3,6,9,1,3]
listcall(l1)


#pass--if we dont have anything to define we can use pass keyword inside of a function.it will return nothing
def nothing():
    pass

nothing()

#recursive funtion -- a function which is calling itself. it is a recursive function

def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))
print(fact(5))


#scope of  a fucntion
#local variable function -- a variable that belongs to a particular which is we cant call outside of the function
#that variable called local variable

def lf():
    x=54    # this variable declared as local
    print(x)

lf()
#print(x)

#print(x)

#global variable function-- a variable which can callable even inside and outside of a function that variable known
#as global variable

x=98 #this variable declared as global
def gf():
    print(x)

print(x)
gf()

#to convert a local variable into a global variable use 'global'

def cgf():
    global y
    y =89
    print(y)


cgf()
print(y)

#naming variable --global,local varibles will not override each other
x=45

def call():
    x=34
    print(x)

print(x)
call()

'''

#function documentation:

#def doc():
    # '''
    # a fucntion which is a short way
    #  to execute an operation multiple
    #  times by just calling it name
    # '''

#    print('hello')
    #this single line comment will not execute


#print(doc.__doc__)
#help(doc)
'''

def outer(x):
    print('this is outer function data',x)
    def inner(y):
        print('inner functiondata',y)
    return  inner
a = outer(5)
#a(8)

#abs() Function--Return the absolute value of a number
x = abs(-7.25)

#Return the absolute value of a complex number:
x = abs(3+5j)

#help key word
class Helper:
	

help(Helper)
help(Helper.print_help)

#dir()--Display the content of an object:
class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

#eval() Function--Evaluate the expression 'print(55)':

x = 'print(55)'
eval(x)
#exec() function is used for the dynamic execution of Python programs which can either be a string or object code.
prog = 'print("The sum of 5 and 10 is", (5+10))'
exec(prog)

# The math class is used to include all the
# math functions
from math import *
exec("print(dir())")

# factorial() will be executed
from math import *
exec("print(factorial(5))", {"factorial":factorial})



'''

#extra notes about functions for assignments
'''
1. how we can pass a list inside of an arbitrary functions:

def func(*a):
    for i in a:
        print(i)

l1 = [2,4,5,6,73,2,421,4,3]
func(*l1)

2.how we can ppass a dicttionary inside of an kwargs function:

def func(**a):
    for i in a:
        print(i)

l1 = {'2':3,'4':16,'5':25,'6':36,'3':9}
func(**l1)

3. how we can put normal and kwargs parameters together:

def func(b,c,**a):
    print(b+c+a['2'])
l1 = {'2':3,'4':16,'5':25,'6':36,'3':9}
func(54,23,**l1)

4.to find all the default parameter values from a function:

def f(a, b=42, c=[]):
    pass
print(f.__defaults__)

5.using mutable sequences inside of a function:

def append(elem, to=[]):
    to.append(elem)
    # This call to append() mutates the default variable "to"
    return to
append(1)

6.always keep default elements  (or) converting an element into an integer:

def append(elem, to=None):
    if to is None:
        to = []
    to.append(elem)
    return to

a = append(3)
print(a)

7.how to change a element in lists using a function:

def foo(x):
    x[0] = 9
    print(x)
y = [4, 5, 6]
foo(y)
# Out: [9, 5, 6]
print(y)

8. adding a value from the return value of a function:
def val1():
    return 56
print(val1() + 44)

9.if we added any statments after 'return' in a fucntion that will not execute ever:

def give_me_another_five():

    print('This statement will  be printed.')
    return 5
    print('This statement will not be printed. Ever.')
print(give_me_another_five())

10.storing multiple values in a function and getting it and store them into different variables

def give_me_two_fives():
    return 5, 555 # Returns two 5
first, second = give_me_two_fives()
print(first)

print(second)

11.inner function and how to call it:

def makeInc(x):
    def inc(y):
# x is "attached" in the definition of inc
        return y + x
    return inc

incOne = makeInc(1)
incFive = makeInc(5)

print(incOne(5))  # returns 6
print(incFive(5))  # returns 10

12.it's possible to put a single asterisk in the function signature to ensure that the after coming
arguments may only be passed using keyword arguments.:

def f(a, b, *, c):
    pass
#f(1, 2, 3)# error

f(1, 2, c=3)
# No error

13.in function the default parameter always comes to the end only if we declare it in the first
place it will throw error:

#wrong format:
def df(a=3,b,c):
    pass
#right format:

def df(b,c,a=3):
    pass
    
14.unpacking a function with all types parameters:

def unpack(a,b,c=45,d=34,*e,**f):
    print(a,b,c,d,a,f)
unpack(1,2)
unpack(1,2,3)
unpack(1,2,3,d=54)
unpack(1,2,3,4,5,6,7,8)
unpack(1,2,3,4,5,g=5,s=45)
unpack(1,23,3,4,5,3,6,7,4,3,45,r=6)
unpack(1,3,g=6)

15.To indicate that we only want to allow int types we can change our function deﬁnition to look like:

def two_sum(a: int, b: int):
    return a + b
        

'''


