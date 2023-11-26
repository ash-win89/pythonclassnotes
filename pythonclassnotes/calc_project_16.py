#topics using this project -- data types,operators,if else, while, input

ans = 'yes'

while ans == 'yes':

    number1 = eval(input('enter the first value'))
    number2 = eval(input('enter the second value'))
    print(['additon ==+', 'subraction==-', 'multiplication = *','division == /','floordiv == //','exponen == **','reminder == %'])
    op = input('enter the operation you want to perform')

    if op == '+':
        print(number1+number2)
    elif op == '-':
        print(number1- number2)
    elif op == '*':
        print(number1* number2)
    elif op == '/':
        print(number1/ number2)
    elif op == '//':
        print(number1// number2)
    elif op == '**':
        print(number1** number2)
    elif op == '%':
        print(number1% number2)
    else:
        print('invalid operator')

    ans = input('do you want to continue yes/no')

#user authorization:
#nested loops, data structures, data types,if, while,indexing,operators, input statements
#first we need to get user name as input and verify with alredy existing user name list
#match found put a welcome and ask password message.verify password with the password list
#put the authorise use confirmed, then use break
#if user or password wrong loop again and give three chances using while loop