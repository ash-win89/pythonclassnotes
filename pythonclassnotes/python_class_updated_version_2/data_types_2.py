
#integers:
a =32
b = -43
print(a,b)
print(type(a))
print(type(b))

#its just a representation of an integer in '0's and '1's formation:
#in python binary values comes up with '0b'
c = 0B010011
print(c)

#octal -- its just a representation of an integer in '0 to 7's  formation:
#in python binary values comes up with '0o'
d = 0o44567
print(d)

#hexa -- its just a representation of an integer in '0 to 9, a to f's  formation:
#in python binary values comes up with '0x'
e = 0x45bde
print(e)

#float--a number contains one or more point values
a = 1.0
b = -56.89
print(type(a))
print(type(b))

#the another to declare a float 'e' to indicate the power of 10
#using 'e' to declare even if we did not mentioned decimal points also it will give decimal values

x = 3e2  #3x100, or 3x10x10
print(type(x))

#complex -- combination of real and imaginary to declare imaginary values use 'j'

a = 5+7j
print(type(a))
print(a.real)
print(a.imag)

#the values sorrounded by quotes -string
a = '56'
b = '''6+7j'''
#using '\' to give multiline string will bring the result in a single line
c  = "hello world" \
     "again"
#using ''' to declare multiline string will return the same format result
d = '''hello
    world
    thanks'''
print(type(a))
print(type(b))
print(type(c))
print(a,b,c,d)

#True or False
a = True
b = False
print(type(a))
print(type(b))
c = 7
d = 9
print(bool(c == d))
e = ()
print(bool(e))
print(bool([]))
print(bool(0.0))

#None -- used to define a null there is no value at all
print(None == 0)
z = None
print(type(z))

#bytes--converting actual values bytes
a = bytes(2)
print(a)

#converting a string bytes format
a = 'hello world'
b = bytes(a,'utf-8')
c = a.encode('utf-8')
print(b)
print(c)
d = c.decode()
print(d)