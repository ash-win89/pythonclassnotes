'''
generally --a functions is a chunk of codes that we can use over and over again instead
writing it again and again
user defined functions --the user or the programmer writes the code according his convinient
these kind of functions we used call them as user defined functions
built in functions --inline that the compiler already has ex: 'input()'
#functions -- the code  which written somewhere  when ever we called that time only it
will execute
to create a function we can use a keyword called 'def' and following that we have to declare the
name of the function

once you declared function using that function you can call the function as many as times
you want
'''
#basic function

def message():
    #print('hello world')
    #when we are using 'return' statement inside of a function we need to put print statement
    #when we call the function
    return 'hello world'
#to call a function we have to use function  along with parenthesis
#print(message())
#message()

#parameters -- while declaring a function inside of the parenthesis passing variable kind
#of charecters is known as parameters
#parameters --used to pass some values inside of the function if a function does not hold any
#parameters we cannot pass any data inside of it
def add(a,b):
    print(a + b)

#arguments -- the information (or) the data which is can passed into a function
#add(6,3)
#add(4)
#by default we need pass correct number of arguments --in this example two parameters
#declared so we need to pass only 2 arguments else we will get
#"TypeError: add() takes 2 positional arguments but 3 were given"
#add(4,7,8)

'''
Arbitrary arguments -- exactly if we dont know how many arguments (or) how many datas
will be passed inside of our function we can use * before the parameter that * will convert
your parameter into a tuple
or
we dont know how many number of arguments that will be passed into a function. to handle this
kind of situation we can use arbitrary arguments means a * with a parameter

to passing * before a parameter of a function that function will receive a tuple of arguments
and we can call them (or) access them through indexing
'''

def states(*args):
    print(f'the first state of america {args[0]} and following that {args[1]} state will be there ')

#states('newyork','washington dc','las vegas','los angeles')


def sum(*numbers):
    sums = 0
    for i in numbers:
        sums = sums +i
    print('sum of the passed arguments is=',sums)
#sum(4,32,7,65)

'''
keyword Arguments -- we can assign particular arguments to our desired parameters like 
key = value format
or
we can send arguments with the key = value syntax
in this way the order of the arguments what we are passing does not matter
or
arguments are assigned based on the name of the parameters
'''

def states(cap_state, pop_state1,pop_state2,pop_state3):
    print(f'the capital of usa {cap_state} and popular states {pop_state3} and {pop_state2}')

#states(pop_state3='sanfrancisco', pop_state1='las vegas', pop_state2='los angeles',cap_state='newyork')
#do not try to declare any function with 'test' keyword because the test keyword dedicated
#for the testing purpose
# def vale(*a):
#     print('the values with keys will not stored in arbitrary arguments')
#
#when we try to pass key value pair in a arbitrary  it will throw
# "TypeError: vale() got an unexpected keyword argument 'key"
#vale(a = '1',b=2,c=3)

#arbitrary keyword arguments function '**kwagrs'
'''
arbitrary keyword arguments function -- if we dont know how many key value pairs passed (or)
how many keyword argumenrs that will be passed into your function, that time we can use
** before the parameter  while declaring a function using the ** the parameter will be
converted into a dictionary
(or)
if we declare a parameter with ** (two asterix) in that way a function will receive a dictionary
of arguments, we can access those  values in the same way how we accessed datas from dictionary

'''

def fruit(**kwargs):
    print(f'the fruit1 is {kwargs["fruit1"]}, the fruit3 is {kwargs["fruit3"]}')

#fruit(fruit1 = 'apple', fruit2= 'orange', fruit3='cherry')

#accessing the whole dictionary

def fruit(**kwargs):
    for i in kwargs:
        print(f'the key is {i} and the value is {kwargs[i]}')
#fruit(fruit1 = 'apple', fruit2= 'orange', fruit3='cherry')
'''
default parameter value function -- if we call  the function without an argument, it will use the
default value what we have already declared in the function
'''

def capital(capit = 'newyork'):
    print(f'the capital city of united states {capit}')

# capital('los angeles')
# capital()
# capital('san francisco')
# capital('alaka')

#passing default parameter value as tuple

def capital(capit = ('moscow','vegas','san diego','florida')):
    #assigning the parameter to another value
    city = capit
    print(f'the capital city of united states {city}')

# capital('los angeles')
# capital()
# capital('san francisco')
# capital('alaka')


'''
1.there will only one value for one default parameter
2.passed parameter should matched while we call them
3.if we are going to pass formal parameters, along with  default value parameters
formal parameters should come in the first place 
'''

def add(b,a=8,c=67):
    print(a+b+c)
# add(5)
# add(3,7)
# add(6,2,4)

'''
    a function we defining should not be empty, for some reason you want to have a function
    with no content we can use pass statement. while calling the function it will nothing
'''
def nothing():
    pass
nothing()


'''
recursion
    a function which can call itself 
    factorial of 5 means --5x4x3x2x1 = 120
'''

def fact(n):
    if n == 1:
        return 1
    else:
        return (n*fact(n-1))
#print(fact(5))
#scope of a function:
'''
local scope: a variable which is created inside of a function belongs to the local scope of that 
function and that variable can be called inside of that function

even for if condition the condtion is true we'll get the value even if it is available
inside of the 'if' block
if False:
    a= 55

print(a)
but if the condition is false we will get error stating the variable not defined
'''

def hello():
    x= 'hello world'#local scope
    print(x)
#hello()
#print(x)
'''
gloabal scope:
    a variable that declared on the main body is a global scope we can call it anywhere 
    
'''
x= 'hello world'
def hello():
    print(x)
# hello()
# print(x)

#innerfunction
#docstring of a function __doc__, help(funcname)
#gloabla variable

'''
inner function:
    a function which is defined inside another  function is known as inner function or nested function
    
__name__ == if the source file is executing as the main program the interpretter sets the __name__
to have a "__main__"
    if the file is being imported from another program file __name__ automatically will set to the 
    module's name    
'''
def hello():
    s = 'iron man'
    def inner():
        s= 'tony stark'
        print(s)

    inner()
    print(s)
    #where we use return statement which indicates the end of the function
    return inner()  # while we calling the parent this inner name will get called


# h1 =hello()
# h1

#how to make a local scope into a gloabal scope:

def glob():
    global name # to make a variable global use 'global' keyword before that
    name = 'steve rogers'
    print(name)

#print(name)
# glob()
# print(name)

def hello():
    '''
    fucntions are reusable code
    you can call any functions
    from any file
    '''
    print('hello world')
#print(hello.__doc__)
#help(hello)