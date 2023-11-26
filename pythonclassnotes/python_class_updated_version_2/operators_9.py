'''
operators in python:
    used to perform operations on variables and values(or) special symbols it holds some
    computation should performed when we call them
'''

'''
arithmetic operators:
    used to perform mathematical operations
'''
'''
addition operator:
    '+' used add more than one values, operands -- values on which the operatore operates
'''
a = 6
b = 26
print(a+b)

'''
subraction: it will subtract the second value from the first the value '-'
'''
print(b-a)

'''
multiplication:used to find the product of two values '*'
'''
print(a*b)
'''
division:
    used to find the  quotient when the first operator is divided by the second '/'
'''
print(b/a)

'''
modulus: used to find the remainder when the nominator is divided by the denominator '%'
'''
print(b%a)

'''
exponentiation:used to raise the first operand to the power of second operand '**'
'''
a= 8
b=3
print(a**b)

'''
floor division:used to find the floor values of a division operation result in between
two values
'''
print(a//b)

'''
Assignment operators:
    used to assigning the values to the variables, right side of expression to the left side
    operand
'''
x = 0
print(x)
x += 5
print(x)
x -= 5
print(x)
x *=5
print(x)
x /=5
print(x)
x = 2
x **=5
print(x)
x //=5
print(x)

'''
comparison:
    used to compare two operands, '==','>','<','>=','<=','!='
'''
a = 6
b =4
print(a == b)
print(a != b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
a = 'hello'
b = 'world'
print(a == b)
print(a != b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

'''
identical operators -- if two values stored in a same address it will return true
'''
a= 5
b = [5]
print(id(a))
print(id(b))
print(a is b)


'''
membership -- to check a particular value in a sequence or a group of values
'''
a= (4,23,7,89,1,7,)
print(4 not in a)
'''
bit wise operators are used to performing bitwise calculations on integers
'''
#and: '&'
a= 9
b = 7
print(a & b)
print(bin(a))
print(bin(b))

'''
calculation format of '&' operator

bin(a)  = 1001
bin(b)  = 0111
        ------   
          0001 --ans result of '&'  
          ---  ---
'''
print(int(0b0001))



'''
calculation format of '|' operator

bin(a)  = 1001
bin(b)  = 0111
        ------   
          1111 --ans result of '|'  
          ---  ---
'''
print(a | b)
print(int(0b1111))

'''
bitwise not operator -- return one's complement of the number 
formula = -(n)-1
'''
a=8
b = -7
print(~a)
print(~b)

'''
bitwise xor operator: if both side values are different we will get 1 else it will return 0
'''
a = 7
b= 3

print(bin(a))
print(bin(b))
'''
bin(a) == 0111
bin(b) == 0011
         -----
          0100  
'''
print(a ^ b)
print(int(0b100))

'''
right shift--shifts the bits of the number to the right it will  fills 0's in the first place
'''
a = 8
print(8 >> 1)
print(bin(a))

'''
bin(a) = 0000 1000
result = 0000 0100 --ans
'''

'''
lest shift--shifts the bits of the number to the left it will  fills 0's in the last place
'''
a = 8
print(8 << 1)
print(bin(a))


'''
bin(a) = 0000 1000
result = 0001 0000 --ans
'''
print(int(0b10000))