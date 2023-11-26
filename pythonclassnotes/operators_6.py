# Operators are used to perform operations on variables and values.
#
# In the example below, we use the + operator to add together two values:

#operators will take one or more than one values(operands) and do preserved operations for the operators
#and it will return a value
#Arithmetic operators are used with numeric values to perform common mathematical operations:
#operators can change their assigned operations based the situation

a=7
b=6
'''
print(a+b)#addition
print(a-b)#subraction
print(a*b)#multiplication
print(a/b)#division
print(a//b)#floor division
print(a**2)#exponential
print(a%b)#remainder


#Assignment operators are used to assign values to variables:

a +=4  #same as x = x+4
print(a)


a -=4  #same as x = x-4
print(a)

a *=4  #same as x = x*4
print(a)

a /=4  #same as x = x/4
print(a)

a //=4  #same as x = x//4
print(a)

a **=2  #same as x = x**4
print(a)

b %=4  #same as x = x%4
print(b)



#Comparison operators are used to compare two values:

a='hello'#ascii value of 'h' --104
b='world'#ascii value of 'w' --119

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

#Logical operators are used to combine conditional statements:
"""

x or y# if x is False then y otherwise x
x and y# if x is False then x otherwise y
not x# if x is True then False, otherwise True
"""

# a = True
# b = False
a=7
b=3

print(a and b)#if both values are true and will return the second value
print(a or b) #if both values are true or will return the first value
print(not a)


# Identical operators are used to compare the objects, not if they are equal, but if they are actually the same object,
# with the same memory location:

a=6
b=6
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

#Membership operators are used to test if a sequence is presented in an object:

a= 'hello world'
print('h' in a)
print('l' not in a)



#ternery operators
a=5
b=4
c = 'smaller' if a<b else 'greater'
print(c)





#Bitwise operators are used to compare (binary) numbers:

#& --it will take the binary version of values and operate them with and operator for each values

 bin(5) --101
 bin(6)-- 110
        -----
          100  

'''
'''
print(5 & 6) #ans 4
print(bin(5))
print(bin(6))
print(int(0b100))#here to check we just passed the binary version out come value 5&6
'''
#    |	OR	--it will take binary versions of given value then perform 'or' operation then it will return result of
#integer version

'''
 bin(5) --101
 bin(6)-- 110
        -----
          111  

'''
'''
print(5 | 6) #ans 7
print(int(0b111))
'''
'''
#     ^	XOR	--from the binary version given values it will return '1'--if any one value is 1 another is 0

 bin(5) --101
 bin(6)-- 110
        -----
          011
'''
'''
print(5 ^ 6) #ans 3 ob11
print(int(0b011))
'''
'''
#    ~ 	NOT	Inverts all the bits


'''
'''
formulat "~" is ~n = -n-1
         = -6-1 = -7    
          #to convert into integer version then add '-' operators to that value
'''
'''
print(~(-6)) #it is a representation of ~n = -n-1
'''

#    <<	right shift operator --shifts (or) moves of the number to the right and fills 0 in the void
'''
bin(10) ==0000 1010
#if we move the data to the rightt for 1 space result will be =(0000 0101)

10>>1 =   0000 0101

ex:2

bin(8) ==0000 1000 #doing right shift with 1 bit like --8>>1
        =0000 0100
 


'''
'''
print(bin(8))
print(8>>1)
print(int(0b100))
'''
#print(8>>1) #ans --4 ob10
#000101
'''
'''
# left shift operator --shifts or moves bits of the number to the left then it will fills the void with 0
'''
ex:2
bin(8) ==0000 1000 #doing left shift with 1 bit like --8<<1
        =0001 0000
       


print(int(0b10000))

print(8<<1) #ans  16
#110100
'''
#Assignment operators with Bitwise operators:
x = 5
x &= 6
print(x)

x = 5
x |= 6
print(x)

x = 5
x ^= 6
print(x)

x = 5
x <<= 1
print(x)

x = 5
x >>= 1
print(x)


#extra notes for assignments:
"""
1.a boolean is also an int . The bool type is a subclass of the int type and True and
False are its only instances:
print(issubclass(bool, int))# True
print(isinstance(True, bool))# True
print(isinstance(False, bool)) # True

2.The < , <= , > and >= operators will raise a TypeError exception when any operand is a complex number.
"
a = 6+5j
b = 8+5j
print(a>b)
"
3.reversed : A reversed order of str with reversed function
"a = reversed('hello')"

4.we can add multiple sequences with key inside of a dictionary
5.dir(math) will give you all the functions which is available under the  maths library
6.not only for math any library you want to get to know all the functions available inside of it
use 'dir()' and pass the library name inside of it you will all of them
7. you want to read the documentations of the libraries use ".__doc__" like
"print(math.__doc__)"
8.the combinations of multiplications operators could be:
int and int (gives an int in Python 2 and a float in Python 3)
int and float (gives a float )
int and complex (gives a complex )
float and float (gives a float )
float and complex (gives a complex )
complex and complex (gives a complex )

9. the combination of additions operators could be:same goes for mltiplication and subraction as well
int and int (gives an int )
int and float (gives a float )
int and complex (gives a complex )
float and float (gives a float )
float and complex (gives a complex )
complex and complex (gives a complex )

10. an alternative of do exponential we can use 'pow' for ex instead (2**3) we can  use "pow(2,3)"

11.to find the square we can use sqrt but these 'pow' and 'sqrt' comes under math library
do a documentation about math library

12."operator preceedence"- which means what operators should excute first if we have combinations
of operator in same line:
"Python follows PEMDAS rule. PEMDAS stands for Parentheses, Exponents, Multiplication and Division, and Addition
and Subtraction."
a, b, c, d = 2, 3, 5, 7
a ** (b + c) # parentheses
256
a * b ** c # exponent: same as `a * (b ** c)`
7776
a + b * c / d # multiplication / division: same as `a + (b * c / d)`
4.142857142857142

13.we can use ternary operators to check multiple conditions at a time
"n = 5
"Hello" if n > 10 else "Goodbye" if n > 5 else "Good day""

14.we can use comparison operators using the dunder methods in classes

"class Foo(object):
def __init__(self, item):
self.my_item = item
def __eq__(self, other):
return self.my_item == other.my_item

a= Foo(5)
b= Foo(5)
a== b # True
a!= b # False
a is b # False"


15.accessing operators with names:

from operator import *
print(add(1, 1))

print(mul('a', 10))
# Output: 'aaaaaaaaaa'
print(mul([3], 3))
# Output: [3, 3, 3]
alist = ['wolf', 'sheep', 'duck']
print(list(filter(methodcaller('startswith', 'd'), alist)))
# Output: ['duck']

"""
