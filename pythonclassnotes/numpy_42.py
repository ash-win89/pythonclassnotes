#numpy --used to create arrays
#arrays are faster than list

import numpy

#creating arrays:
'''
a = numpy.array([1,2,3,4,5,6,7])
print(type(a))
print(a)
print(numpy.__version__)

b = numpy.array((2,4,8,5,1))
print(b)

#o-dimensional

c = numpy.array(67)
print(c)


b = numpy.array((2,4,8,5,1))
#1-dimensional
tup = numpy.array((2,4,8,5,1))
print(b)

#2-dimensional

dime2 = numpy.array([[2,5,6],[7,2,9]])
print(dime2)

#3-dimentional

dime3 = numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[6,3,9]]])
print(dime3)

#checking the dimention

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(tup.ndim)
print(dime2.ndim)
print(dime3.ndim)
'''
import  numpy as np
'''
#converting an array to required dimentsions
test = np.array([1,2,3,4,5,6,7,8,9,10,11], ndmin=6)
print(test)
print('number of dimensions', test.ndim)

#indexing
test = np.array([1,2,3,4,5,6,7,8,9,10,11])
print(test[3])

#2d-indexing
dime2 = np.array([[2,5,6],[7,2,9]])
print(dime2[0,1])

#negative indexing
print(dime2[-1,1])

#3d-indexing
#we have four sequence seperated as 2(0,1) nested each(0,1) nested has two sequence(0)
dime3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[6,3,9]]])
print(dime3[1,1,2])

import numpy as np

test = np.array([1,2,3,4,5,6,7,8,9,10,11])
#slicing
print(test[4:11])
print(test[:7])
print(test[2:])
print(test[-4:-1])
print(test[1:11:2])

#slicing with 2d

dime2 = np.array([[2,5,6],[7,2,9]])
print(dime2[0,0:1])
#

print(dime2[0:2,2])#indexing

print(dime2[0:2,0:2])#slicing
print(dime2.dtype)
'''

test = np.array([1,2,3,4,5,6,7,8,9,10,11],dtype='S')
print(test.dtype)
print(test)

