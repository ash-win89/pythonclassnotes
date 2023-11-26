'''
input()--it will read the line from the input keyword and take the input and convert it into
as string it will break the line then it will return the result
'''

# a = input('enter the name')
# b = 'hello'
# print(b+a)

# #converting input
# a = int(input('enter the first number'))
# b = int(input('enter the second number'))
# print('addition given numbers :',a+b)

#getting the same data type what user inserting
'''
eval()-- evaluates the given value if it is valid python data type it will return the result
'''

# a = eval(input('enter the first number'))
# b = eval(input('enter the second number'))
# print('addition given numbers :',a+b)

'''
string --immutable
'''
a= input('enter the fruit name')
b = int(input('price per kg'))
c = eval(input('enter the quantity'))

print('the fruit need to buy %s the per kg price is %d the quntity of the fruit is %.2f'%(a,b,c))
print('the fruit need to buy {} the per kg price is {} the quntity of the fruit is {}'.format(a,b,c))

'''
f-string--it will convinient way embed the values inside of a string
'''
value = f'the fruit i want is {a} i want quantity of {c} kgs and the price is {b}'
print(value)