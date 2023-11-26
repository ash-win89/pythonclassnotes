# The input() function helps to enter data at run time by the user and the output
# function print()
# is used to display the result of the program on the screen after execution
'''
name = input('enter your name')
print(type(name))
print(name)

#the input keyword converts all the inputs as string so if we want to convert that into int use int keyword

#if we put '9' it will throw error because it will add two more quotations "'9'"
num1 = int(input('enter the first number'))
num2 = int(input('enter the second number'))

print(num1 + num2)
'''
#sometimes you want to get str and int inputs both of them use 'eval' it will get both inputs

num1 = eval(input('enter the first number'))
num2 = eval(input('enter the second number'))

print(num1 + num2)






