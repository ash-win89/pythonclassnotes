
#conditional statements-- decision making statements in programming language used to control the direction of the
#flow of program execution

#if case-- will print the result when the condition is true if condition fails it will return nothing
#or--if a certain condition is true then the block of code will execute else it will not return anything
#else--whenever if case will get fails that time else automatically will execute
'''
a = 0
#here even except '0' or '' or False --what ever value there it will considered as True value
if a:
     print('a is a true value')# this line comes under the if block
#this is where if block ends if we write anythin in margin
else:
     print('a is not a true value')
'''


#indentation --the spaces what we are giving in starting point of lines code, python uses indention to identify
#a block of code


#nested -if--an if statement that is the target of another if statement or nested if statements means
#if statement inside another if statement

'''
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
'''
'''
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#elif --a program can decide multiple options or checking true with multiple conditions or multiple possibilities
ticket_price = 800
trasportation = ['bus','train','ship','flight']

if  ticket_price<500:
    if trasportation[0] == 'bus':
        print('we have a bus ticket')

elif ticket_price <1000:
    if trasportation[1] == "train":
        print('we have a train ticket')

elif ticket_price<1500:
    if trasportation[2] == 'ship':
        print('we have ship ticket')
elif ticket_price<50000:
    if trasportation[3] == 'flight':
        print('we have a flight ticket')
else:
    print('invalid price')


#Short Hand If
a = 9
b = 6
if a > b: print("a is greater than b")

#One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

#One line if else statement, with 3 conditions:

a = 330
b = 3000
print("A") if a > b else print("=") if a == b else print("B")

#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

'''
#You can have if statements inside if statements, this is called nested if statements.

x = 11

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")





