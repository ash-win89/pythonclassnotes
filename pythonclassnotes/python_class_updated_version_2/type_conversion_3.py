#data type conversion:
'''
 a data which we want convert into another data type using the respective data type conversion
 keyword that process we used to call them as a type conversion
'''

'''
implicit data type conversion:
     the python interpreter automatically converts one data type to another without any user
     involvement

a,b = 45,99.99
print(a)
print(b)
print(type(a))#to get to know what type of data that we are dealing with use 'type()
print(type(b))
c = a+b
print(type(c))
'''
'''
explicit data type conversion:
     the data type is manually changed by the user as per their requirement
'''
#int(),bin(),oct(),hex(),str(),bool(),float(),complex():
a = '5'
print(int(a))
#this line will throw error--because even a number available inbetween the quotes it will convert
#bin,oct,hex
#print(bin(a))
#this line will give result
#print(bin(int(a)))
#print(oct(a))
#print(hex(a))
print(float(a))
print(bool(a))
print(complex(a))
#print(str(a))

