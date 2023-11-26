# Variables
# Variables are containers for storing data values.
# Creating Variables
# Python has no command for declaring a variable.
#
# A variable is created the moment you first assign a value to it.
#
# Example

x = 5
y = "John"
print(x)
print(y)


#Variables do not need to be declared with any particular type,
# and can even change type after they have been set.

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

#If you want to specify the data type of a variable, this can be done with casting.
x =str(3)# x will be '3'
y =int(3)# y will be 3
z =float(3)# z will be 3.0

#Python allows you to assign values to multiple variables in one line:
x, y, z ="Orange","Banana","Cherry"
print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables:
#The Python print() function is often used to output variables.

x ="Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
#For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator,
#Python will give you an error:

x = 5
y = "John"
print(x + y)

#You will get an error if you use double quotes inside a string that is surrounded
# by double quotes:
#txt = "We are the so-called "Vikings" from the north."

#To fix this problem, use the escape character \":
txt = "We are the so-called \"Vikings\" from the north."