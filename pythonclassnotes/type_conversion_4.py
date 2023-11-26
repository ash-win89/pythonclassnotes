#type conversion-- to convert a value from one data type to another data type known as type conversion

#to convert all other data types into integer use 'int()' key word:
'''
print(int(0b0111))
print(int(0o654))
print(int(0x98ad))
print(int('45'))
print(int('hello'))
print(int(False))
print(int(6+7j))
print(int(4.5676896))

'''
#to convert all other data types into binary use 'bin()' key word:
'''
print(bin(111))
print(bin(0o654))
print(bin(0x98ad))
#print(bin('45'))
#print(bin('hello'))
print(bin(True))
#print(bin(6+7j))


#to convert all other data types into octal use 'oct()' key word:

print(oct(0b111))
print(oct(654))
print(oct(0x98ad))
#print(oct('45'))
#print(oct('hello'))
print(oct(True))
print(oct(6+7j))


#to convert all other data types into hexadecimal use 'hex()' key word:

print(hex(0b111))
print(hex(0o654))
print(hex(98))
#print(hex('45'))
#print(hex('hello'))
print(hex(True))
print(hex(6+7j))


#to convert all other data types into str use 'str()' key word:

print(str(0b111))
print(str(0o654))
print(str(0x98ad))
print(str('45'))
print(str(89))
print(str(True))
print(str(6+7j))


#to convert all other data types into boolean use 'bool()' key word:

print(bool(0b111))
print(bool(0o654))
print(bool(0x98ad))
print(bool(''))
print(bool('hello'))
print(bool(98))
print(bool(6+7j))


#to convert all other data types into complex use 'complex()' key word:

print(complex(0b111))
print(complex(0o654))
print(complex(0x98ad))
print(complex('45'))
#print(complex('hello'))
print(complex(True))
print(complex(67))


#to convert all other data types into float use 'float()' key word

print(float(0b111))
print(float(0o654))
print(float(0x98ad))
print(float('45'))
#print(float('hello'))
print(float(True))
print(float(67))
print(float(3+8j))
'''
#print(int(3.8976))
#print(bin(3.8976))
#print(oct(3.8976))
#print(hex(3.8976))
#print(str(3.8976))
#print(bool(3.8976))
#print(complex(3.8976))

#implicit type conversion: without user knowledge a programming language automatically
#convert one typpe of data into another type of data

a=4
b= 2.3
c = a+b
print(type(c))
#explicit--user trying convert one type of data into another type
#to convert a integer to binary use bin(),
a = 7
print(bin(a))
print(oct(a))
print(hex(a))
print(str(a))
print(bool(a))
print(float(a))
print(complex(a))
a = 5.6
print(int(a))