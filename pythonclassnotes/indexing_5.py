#a complex number we can split  real and imaginary part

a = 4 + 5j

print(a.real)
print(a.imag)

#str--indexing is accessing values based on stored address or position

b = 'hello world'#for indexing spaces also comes under the count
#left to right count --positive indexing

print(b.index('w'))
#print(b.index('z'))
print(b.find('z'))
print(b.find('w'))
print(b[2])  #accessing third word count starts from 0
print(b[8]) #accessing nineth word

#negative indexing- right to left(negative index starts from -1)
print(b[-2])  #negative indexing accessing second last word

#slicing used to slice the required words from the orgin word

print(b[2:9]) #it will print 2 to 9 word only we can  do negative slicing as well
print(b[2:]) #if we give any values before the colon it will take that as a starting point
print(b[:7]) #if we give any values after the colon it will take that as a finishing point
print(b[3:100])#if we are mention out of range index it will return till end of the sequence'''
print(b[-5:-1])