#Built-in Data Types
'''
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

'''

#data types python has 7 types of data

#1. integer family has 4 types -- int, bin,oct, hex--just numbers in different formations
#int--normal whole numbers we used to call them as integers

a =89765

#0s and 1s we used to call them as binary numbers to declare a binary numbers in python use '0b' or '0B'
#implicit type conversion automatically while calling the binary will convert as integer
binary = 0b01001

#0 to 7 numbers are know octal numbers to declare them use '0o' or '0O' in python--IUPAC numeric form -octa stands for =8
#implicit type conversion automatically while calling the octal will convert as integer
octal = 0o7423

#0 to 9 and a to f is know as hexadecimal numbers to declare them use '0x' or '0X'-in IUPAC --16 of hexa
#implicit type conversion automatically while calling the binary will convert as integer
hexa = 0xab952

#2.string -- in python anything that comes under the single or double or triple quotations that known as string
#string is an array of values
b = 'hello world'
c = '569821' #also a string

#3. bool-- True(1), False(0) mentioning true or false called boolean except 0 or nothing('') everythin is true

e= True
'''
In fact, there are not many values that evaluate to False, except empty values,
such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
'''
f = False# 0,(),[],{},''

#The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))

#4.complex -- a real part with imaginary part called complex to declare imaginary part use 'j' in python

g = 4+7j

#None data types are there

h = None
#float
i = 45.348923

print(a,b,c,e,f,g,h,i,binary,octal,hexa)


'''
Setting the Specific Data Type

If you want to specify the data type, you can use the following constructor functions:

Example	Data Type	
'''
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

#python casting
#Specify a Variable Type --Integers:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


#extra notes for assignment
"""

1. using 'del' key we can delete defined variable

2.using a duplicate variable for unncessary extra values that cannot be printed:
a = 1,2,3,4  #even if we did not used '(' also it will be considered as tuple only
_,x,y,_ = a
print(x,y)

3.a target variable with a * preﬁx can be used as a catch-all variable
which means multiple values and less variables in that case if we put * on a variable
it will gather all extra values:

first, *more, last = (1, 2, 3, 4, 5)
print(first)#1
print(*more)#2,3,4
print(last)#5
print(type(first))#int
print(type(more))#list

4.string Methods:
#to uppercase:
print("This is a 'string'.".upper()) 
#or:
print(str.upper("This is a 'string'"))
#to lowercase:
print("This IS a 'string'.".lower())
#to capitalize
print("this Is A 'String'.".capitalize())
#to title
print("this Is a 'String'".title())
#to interchange lower to upper and upper to lower:
print("this iS A STRiNG".swapcase())
#with a list:
print(list(map(str.upper,["These","are","some","'strings'"])))

5.string translation:

translation_table = str.maketrans("aeiou", "12345")
my_string = "This is a string!"
translated = my_string.translate(translation_table)
print(translated)

6.ASCII values:

import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.octdigits)
print(string.hexdigits)
print(string.digits)
print(string.punctuation)
print(string.whitespace)
print(string.printable)

7.stripping a whitespace in a string:

st = "  a line with leading and trailing space   "
print(st.strip())

#striping specialchar and whitespace as well
st = ">>> a Python prompt".strip('> ')
print(st.strip())

8.right stript and left strip:
#rightstrip:
st = "      spacious string     ".rstrip()
print(st) #ans--"      spacious string"

#leftstrip:
st = "      spacious string     ".lstrip()
print(st) #ans--"spacious string      "

9.reverse and join the string:
st = ''.join(reversed('hello'))
print(st)

10.how to control how much time a string should as to split: using maxsplit:

st = "This is a sentence.".split('e', maxsplit=2)
print(st)

11.Testing what a string is composed of:
#to check all the datas in the string is only alphabet:

print("Hello World".isalpha()) #contains a space-False
print("Hello2World".isalpha()) ## contains a number -False
print("HelloWorld".isalpha()) #True
same case we can use "isupper(),islower(),istitle(),isdecimal,isdigit,isnumeric,isalnum(),isspace()"

12.using the join operations:

st = " ".join(["once","upon","a","time"])
print(st) #ans--once upon a time

13.using the '.count' on string:

st = "She sells seashells by the seashore."
print(st.count("sh"))

14.using 'startswith' and 'endswith':

s = "This is a test string"
print(s.startswith("T"))  #ans True

15.checking with indexing:
s = "This is a test string"
print(s.startswith("is", 2))    #ans  True

#endswidth:
s = "this ends in a full stop."
print(s.endswith('.'))      #ans True

#using this 'or' that method:

s = "this ends in a full stop."
print(s.endswith(('.', 'something')))   #ans True 


"""