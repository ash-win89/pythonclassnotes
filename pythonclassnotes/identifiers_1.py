#printing statement
#if we want to execute specific result into the terminal we can use print statement
print('hello world')

#using the escape characters inside of a string:
print("You can print \n escape characters too.")

#returning two print statement values in a single line:


print("Hello, ", end="")
print("World!")

#Creating a Comment
#Comments starts with a #, and Python will ignore them:

#Example
#This is a comment
print("Hello, World!")


#Comments can be placed at the end of a line, and Python will ignore the rest of the line:

print("Hello, World!")#This is a comment

#A comment does not have to be text that explains the code, it can also be used to prevent Python from executing code:
#ex:
#print("Hello, World!")
print("Cheers, Mate!")

#Multi Line Comments
#Python does not really have a syntax for multi line comments.
#To add a multiline comment you could insert a # for each line:
#Ex:
#This is a comment
#written in
#more than just one line
print("Hello, World!")

#Or, not quite as intended, you can use a multiline string.
#Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

#ex:

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.

#identifiers --way of giving names to the variable for different entities such as constants, variables, function
#identifiers used to define variables --rules that we need to follow
#rule --1-- dont use any constant values infront of a variable or we should pass any constant values in the first
#place of a variable name
#1a =55 #wrong

a = 'apple'
a2b = 78 # in the middle or end we can use identifiers
a1 = 67
print(a,a2b,a1)

#rule --2-- dont use special characters even middle or first or end

name = 'hello'  # wrong

#rule --3 -- keywords should be used as a variable or-- reserved words already occupied with some operation

#for = 45

#case sensitive means if we are declaring a variable name with lower case we cannot call that
#variable name with upper case
print(name)


#to define or to intimate any variable as a private values we have to use underscore single underscore
#means private double underscore means strictly private

_private = 'this is the private key'
#
__sPrivate = 'this is strictly private key'

#to define a constant value for a variable we have to use uppercases while defining a variable

APPLE =45
print(_private,APPLE)





#extra notes for assignments:
'''
1.if we need to run python script in cmd prompt without converting it python shell 
we have to open 'cmd' and type "python3 -c 'print("Hello, World")'" in linux 
in windows "python -c 'print("Hello, World")'"

2.to check all the keyword list in python practise this program
"import keyword
print(keyword.kwlist)"

3.variables are casesensitive if we define 'x' variable with a value and if we try to call with 'X' not gonna happen
"
x = 9
y = X*5
=>NameError: name 'X' is not defined"
4. we can assign multiple values according the how much variables we have defined in a single line
"a, b, c = 1, 2, 3"

5.we can assign dummy variable name using "_" but we cannot print it
"
a, b, _ = 1, 2, 3
print(a, b)
# Output: 1, 2

6.You can also assign a single value to several variables simultaneously.
a = b = c = 1
print(a, b, c)

7.to upgrade any package or library in ubuntu use "pip install [package_name] --upgrade"
8.to upgrade pip in ubuntu "$ pip install -U pip"
9.to upgrade pip in windows "py -m pip install -U pip"

10.if we want get more informations of a keyword use 'help()' for example "print(help('if'))"
dont forget we have to pass them with quotes
"

11.print statement with parameters:

print('apples','bananas', 'cherries', sep=', ')

'''


