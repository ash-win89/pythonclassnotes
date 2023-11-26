
#NumPy Introduction

#NumPy is a Python library used for working with arrays.
#NumPy stands for Numerical Python
#Import NumPy

import numpy

#NumPy as np
#NumPy is usually imported under the np alias.

import numpy as np

#Create a NumPy ndarray Object

#NumPy is used to work with arrays. The array object in NumPy is called ndarray
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

#Dimensions in Arrays
#0-D Arrays
import numpy as np

arr = np.array(42)

print(arr)

#1-D Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

#2-D Arrays

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

#3-D arrays

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

#Number of Dimensions

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Higher Dimensional Arrays
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

#NumPy Array Indexing

#The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

#Access 2-D Arrays

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

#Access 3-D Arrays

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

#Negative Indexing

#import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

#Slicing arrays
#slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

#Negative Slicing

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

import numpy as np#rom the second element, slice elements from index 1 to index 4 (not included)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


print(arr[1, 1:4])

import numpy as np#From both elements, return index 2:

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])

#Get the data type of an array object:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

#We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
#If a type is given in which elements can't be casted then NumPy will raise a ValueError.
import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')
#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

#The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
#Make a copy, change the original array, and display both arrays:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)#The copy SHOULD NOT be affected by the changes made to the original array.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)#The view SHOULD be affected by the changes made to the original array.

#Check if Array Owns its Data
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

#The shape of an array is the number of elements in each dimension.
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

#By reshaping we can add or remove dimensions or change number of elements in each dimension.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)#Reshape From 1-D to 2-D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)#Reshape From 1-D to 3-D
#Check if the returned array is a copy or a view:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

#Unknown Dimension
#You are allowed to have one "unknown" dimension.Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
#Pass -1 as the value, and NumPy will calculate this number for you.
#We can not pass -1 to more than one dimension.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

#Flattening array means converting a multidimensional array into a 1D array.
#We can use reshape(-1) to do this.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

#Iterating Arrays
#Iterating means going through elements one by one.As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)#Iterate on each scalar element of the 2-D array:

#The function nditer() is a helping function that can be used from very basic to very advanced iterations
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

#We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
#NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
#Iterating With Different Step Size

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
#Enumeration means mentioning sequence number of somethings one by one.

import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
#Joining means putting contents of two or more arrays in a single array.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)#Join two 2-D arrays along rows (axis=1):

#Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
#NumPy provides a helper function: hstack() to stack along rows.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))
print(arr)
#NumPy provides a helper function: vstack()  to stack along columns.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
#NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

#Splitting is reverse operation of Joining.
#We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)#Split the array in 3 parts:
#Split Into Array-The return value of the array_split() method is an array containing each of the split as an array.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

import numpy as np#Split the 2-D array into three 2-D arrays.

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)
#An alternate solution is using hsplit() opposite of hstack()
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)

#Searching Arrays-To search an array, use the where() method
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)#Find the indexes where the values are even:

#The searchsorted() method is assumed to be used on sorted arrays.
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)#By default the left most index is returned, but we can give side='right' to return the right most index instead.

import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)#To search for more than one value

#The NumPy ndarray object has a function called sort(), that will sort a specified array.
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))#This method returns a copy of the array, leaving the original array unchanged

import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))



#Getting some elements out of an existing array and creating a new array out of them is called filtering.
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

#We can directly substitute the array instead of the iterable variable in our condition
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)





#Generate Random Number

#NumPy offers the random module to work with random numbers.
'''
from numpy_full import random

x = random.randint(100)

print(x)

#The random module's rand() method returns a random float between 0 and 1.
from numpy_full import random

x = random.rand()

print(x)

#Generate Random Array-The randint() method takes a size parameter where you can specify the shape of an array.

from numpy_full import random

x=random.randint(100, size=(5))

print(x)

#2d Eg
from numpy_full import random

x = random.randint(100,size=(3, 5))

print(x)

#The choice() method takes an array as a parameter and randomly returns one of the values.
from numpy_full import random

x = random.choice([3, 5, 7, 9])

print(x)

#We can generate random numbers based on defined probabilities using the choice() method of the random module.
#The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.

from numpy_full import random

x = random.choice([3, 5, 7, 9], p=[0.2, 0.8, 0.0, 0.0], size=(10))

print(x)#The sum of all probability numbers should be 1.

#Shuffling Arrays-Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
from numpy_full import random
import numpy_full as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)#The shuffle() method makes changes to the original array.

#The permutation() method returns a re-arranged array (and leaves the original array un-changed).
from numpy_full import random
import numpy_full as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

#Normal Distribution
#Use the random.normal() method to get a Normal Data Distribution.
#It has three parameters:
#loc - (Mean) where the peak of the bell exists.
#scale - (Standard Deviation) how flat the graph distribution should be.
#size - The shape of the returned array.
rom numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

#Binomial Distribution is a Discrete Distribution.
#It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
#It has three parameters:
#n - number of trials.
#p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
#size - The shape of the returned array.

from numpy_full import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)

#Poisson Distribution
#Poisson Distribution is a Discrete Distribution.
#It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is probability he will eat thrice?

#It has two parameters:

#lam - rate or known number of occurences e.g. 2 for above problem.

#size - The shape of the returned array

from numpy_full import random

x = random.poisson(lam=2, size=10)

print(x)

#Uniform Distribution
3Used to describe probability where every event has equal chances of occuring.

#E.g. Generation of random numbers.

#It has three parameters:

#a - lower bound - default 0 .0.

#b - upper bound - default 1.0.

#size - The shape of the returned array.
from numpy_full import random

x = random.uniform(size=(2, 3))

print(x)

#Logistic Distribution is used to describe growth.

#Used extensively in machine learning in logistic regression, neural networks etc.

#It has three parameters:

#loc - mean, where the peak is. Default 0.

#scale - standard deviation, the flatness of distribution. Default 1.

#size - The shape of the returned array.
from numpy_full import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)

#Multinomial distribution is a generalization of binomial distribution.

#It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

#It has three parameters:

#n - number of possible outcomes (e.g. 6 for dice roll).

#pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).

#size - The shape of the returned array.

from numpy_full import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

#Exponential distribution is used for describing time till next event e.g. failure/success etc.

#It has two parameters:

#scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

#size - The shape of the returned array.
from numpy_full import random

x = random.exponential(scale=2, size=(2, 3))

print(x)

#Chi Square distribution is used as a basis to verify the hypothesis.

#It has two parameters:

#df - (degree of freedom).

#size - The shape of the returned array.
from numpy_full import random

x = random.chisquare(df=2, size=(2, 3))

print(x)

#Rayleigh distribution is used in signal processing.

#It has two parameters:

#scale - (standard deviation) decides how flat the distribution will be default 1.0).

#size - The shape of the returned array.

from numpy_full import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

#A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

#It has two parameter:

#a - shape parameter.

#size - The shape of the returned array.

from numpy_full import random

x = random.pareto(a=2, size=(2, 3))

print(x)

#Zipf distritutions-In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
#It has two parameters:

#a - distribution parameter.

#size - The shape of the returned array.

from numpy_full import random

x = random.zipf(a=2, size=(2, 3))

print(x)


#Visualization

#Visualization of Normal Distribution

from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()

#Visualization of Binomial Distribution

from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()

#Visualization of Poisson Distribution
from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()

#Visualization of Uniform Distribution

from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False)

plt.show()

#Logistic Distribution

from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()

#Visualization of Exponential Distribution

from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=1000), hist=False)

plt.show()

#Visualization of Chi Square Distribution

from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()

#Visualization of Rayleigh Distribution
from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()

#Visualization of Pareto Distribution

from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()

#Visualization of Zipf Distribution

from numpy_full import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()

'''#ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.
#ufuncs also take additional arguments, like:

#where boolean array or condition defining where the operations should take place.

#dtype defining the return type of elements.

#out output array where the return value should be copied.
#Converting iterative statements into a vector based operation is called vectorization.
#Add the Elements of Two Lists
import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

#Create Your Own ufunc
#To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

#The frompyfunc() method takes the following arguments:

#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.
import numpy as np

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

#Check the type of a function to check if it is a ufunc or not.
import numpy as np

print(type(np.add))

import numpy as np

print(type(np.concatenate))

#Simple Arithmetic
#Addition
#The add() function sums the content of two arrays, and return the results in a new array.
import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)

#Subtraction
#The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)

#Multiplication
#The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)

#Division
#The divide() function divides the values from one array with the values from another array, and return the results in a new array.

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)

#Power
#The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)

#Remainder
#Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)

#Quotient and Mod
#The divmod() function return both the quotient and the the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)

#Absolute Values
#Both the absolute() and the abs() functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()

import numpy as np

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)

#Rounding Decimals
#Truncation
#Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)

#Fix
import numpy as np

arr = np.fix([-3.1666, 3.6667])

print(arr)

#Rounding
#The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

import numpy as np

arr = np.around(3.1666, 2)

print(arr)
#Floor
#The floor() function rounds off decimal to nearest lower integer.
import numpy as np

arr = np.floor([-3.1666, 3.6667])

print(arr)

#Ceil
#The ceil() function rounds off decimal to nearest upper integer.
import numpy as np

arr = np.ceil([-3.1666, 3.6667])

print(arr)

#Logs
#NumPy provides functions to perform log at the base 2, e and 10.
#Log at Base 2
import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))

#Log at Base 10
import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))

#Natural Log, or Log at Base e
import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))

#Log at Any Base
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))

#Summations
#Addition is done between two arguments whereas summation happens over n elements.
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)

#Summation Over an Axis

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)

#Cummulative Sum

import numpy as np

arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr)

#Products
import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)

#Product Over an Axis
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)

#Cummulative Product
import numpy as np

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)

#Differences
import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)

#Compute discrete difference of the following array twice

import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

#LCM (Lowest Common Multiple)
import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)

#LCM in Arrays
import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)
#CM of all values of an array where the array contains all integers from 1 to 10:
import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)

#GCD (Greatest Common Denominator)
import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)

import numpy as np

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)

#Trigonometric Functions
#NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.

import numpy as np

x = np.sin(np.pi/2)

print(x)

import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)

#Convert all of the values in following array arr to radians:
import numpy as np

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)

#Convert all of the values in following array arr to degrees
import numpy as np

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)


#Angles
#NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
import numpy as np

x = np.arcsin(1.0)

print(x)

import numpy as np

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)

#Hypotenues
#NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.

import numpy as np

base = 3
perp = 4

x = np.hypot(base, perp)

print(x)

#Hyperbolic Functions
#NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..

import numpy as np

x = np.sinh(np.pi/2)

print(x)

import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)

print(x)
#Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.

import numpy as np

x = np.arcsinh(1.0)

print(x)

import numpy as np

arr = np.array([0.1, 0.2, 0.5])

x = np.arctanh(arr)

print(x)

#NumPy Set Operations

#Sets are used for operations involving frequent intersection, union and difference operations.

#Create Sets in NumPy
#We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.
'''
import numpy_full as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)

#Union
#o find the unique values of two arrays, use the union1d() method.
import numpy_full as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)

#Intersection
import numpy_full as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr)

#Difference
import numpy_full as np

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)

#Symmetric Difference

import numpy_full as np

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)




























