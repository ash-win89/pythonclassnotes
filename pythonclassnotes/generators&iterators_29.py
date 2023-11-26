
#iteration-a process that is repeated more than one time by applying the same logic is called an iteration
#iterator--an iterator is an object  which contains a countable number of values and it is used to iterate over
#iterable objects-string,list,tuple,set

#iter() --keyword used to create an iterator containing an iterable object
#next() -- keyword used to call the next element in the iterable object
# through all the values
'''
l = [5,2,8,5,7,9]
it = iter(l)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#print(next(myit))


class Numbers:
    #__iter__ function returns an iterator for the initialized object(set,tuple)creates an object that can
    #be accessed one element at a time
    def __iter__(self):
        self.a =1
        return self

    #the __next__ function can be accessed through next keyword
    def __next__(self):
        x =self.a
        self.a +=1
        return x

n = Numbers()
it = iter(n)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


class Numbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
       if self.a <=8:
            x = self.a
            self.a += 1
            return x
       else:
           raise StopIteration


n = Numbers()
it = iter(n)

# for i in it:
#     print(i)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''


#generators-- a generator it is just like normal function whenever it needs generate next we have yield to generate them
#or
#generators function is same as normal fucntion but when it needs to generate a value it will do with 'yield'
'''
Generator-Function: A generator-function is defined like a normal function,
but whenever it needs to generate a value, it does so with the yield keyword rather 
than return. If the body of a def contains yield,
the function automatically becomes a generator function. '''
'''

# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)
'''

'''
Generator-Object : Generator functions return a generator object. 
Generator objects are used either by calling the next method on the generator object
 or using the generator object in a “for in” loop'''
'''

def num():
    yield 1
    yield 2
    yield 6

t =num()
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())

#finding fibonauci numbers:
'''
# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(15)

# Iterating over the generator object using next
# print(next(x))  # In Python 3, __next__()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#print(next(x))



# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(40):
    print(i)

'''
'''
#extra notes for assignments:
'''
1.using yield to an infinite function

def integers_starting_from(n):
    while True:
        yield n
        n += 1
natural_numbers = integers_starting_from(1)
print(natural_numbers)
'''
