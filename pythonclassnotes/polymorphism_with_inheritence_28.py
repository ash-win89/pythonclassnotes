#polymorphism will let us define  methods  with same name even for parent can also have even can have same of a method
#if we have multiple class methods with same name the parentclass methods will be overloaded by the child class methods
'''
class Bird:
    def species(self):
        print('there is different types of birds are there but every birds have wings')

    def flight(self):
        print('some of them can fly some of them can walk')

class eagle(Bird):
    def flight(self):
        print('eagle can fly on top of the sky')

class ostrich(Bird):
    def flight(self):
        Bird.flight(self)
        print('ostriches cannot fly but they can run')

b =Bird()
e= eagle()
o = ostrich()

b.species()
b.flight()

e.species()
e.flight()

o.species()
o.flight()


#operator overloading -- we can use same operator for multiple purpose:
#The operator overloading in Python means provide extended meaning beyond their
#predefined operational meaning. Such as, we use the "+" operator for adding two
#integers as well as joining two strings or merging two lists.
#We can achieve this as the "+" operator is overloaded by the "int" class and "str" class.

class example:
    def __init__(self, X):
        self.X = X

    # adding two objects
    def __add__(self, U):
        return self.X + U.X
object_1 = example( int( input( print ("Please enter the value: "))))
object_2 = example( int( input( print ("Please enter the value: "))))
print (": ", object_1 + object_2)
object_3 = example(str( input( print ("Please enter the value: "))))
object_4 = example(str( input( print ("Please enter the value: "))))
print (": ", object_3 + object_4)


#Python program for overloading comparison operators.

class example_1:
    def __init__(self, X):
        self.X = X
    def __gt__(self, U):
        if(self.X > U.X):
            return True
        else:
            return False
object_1 = example_1(int( input( print ("Please enter the value: "))))
object_2 = example_1(int (input( print("Please enter the value: "))))
if(object_1 > object_2):
    print ("The object_1 is greater than object_2")
else:
    print ("The object_2 is greater than object_1")


#Python Program for overloading equality and less than operators:

class E_1:
    def __init__(self, X):
        self.X = X
    def __lt__(self, U):
        if(self.X < U.X):
            return "object_1 is less than object_2"
        else:
            return "object_2 is less than object_1"
    def __eq__(self, U):
        if(self.X == U.X):
            return "Both the objects are equal"
        else:
            return "Objects are not equal"

object_1 = E_1(int( input( print ("Please enter the value: "))))
object_2 = E_1(int( input( print ("Please enter the value: "))))
print (": ", object_1 < object_2)

object_3 = E_1(int( input( print ("Please enter the value: "))))
object_4 = E_1(int( input( print ("Please enter the value: "))))
print (": ", object_3 == object_4)




#method overloading -- last method will override previous methods inside of  class
#alternatively if we do have multiple methods with same name inside of a single class that also will get overload
#the final method will overload the previous methods

#Two or more methods have the same name but different numbers of parameters or different types
#of parameters, or both. These methods are called overloaded methods and this is called
#method overloading.
# First product method.
# Takes two argument and print their
# product
a = 9
a =99
print(a)



def product(a, b,c):
	p = a * b*c
	print(p)

# Second product method
# Takes three argument and print their
# product


def product(a, b):
	p = a * b
	print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5)


#By Using Multiple Dispatch Decorator

from multipledispatch import dispatch

# passing one parameter


@dispatch(int, int)
def product(first, second):
	result = first*second
	print(result)

# passing two parameters


@dispatch(int, int, int)
def product(first, second, third):
	result = first * second * third
	print(result)

# you can also pass data type of any value as per requirement


@dispatch(float, float, float)
def product(first, second, third):
	result = first * second * third
	print(result)


# calling product method with 2 arguments
product(2, 3) # this will give output of 6

# calling product method with 3 arguments but all int
product(2, 3, 2) # this will give output of 12

# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3) # this will give output of 17.985999999999997



class Test:

    def call(self,a):
        print('this method has one parameter')

    def call(self,a,b):
        print('this method has two parameters')

    def call(self):
         print('this method has no arguments')

t =Test()
t.call(8)

#constructor overloading
class Test:

    def __init__(self,a,b,c):
        print('this construct have no parameters')


    def __init__(self):
        print('this construct have one parameters')


    def __init__(self,a,b):
        print('this construct have two parameters')

Test(44,33,7)


#one more example for method overloading
class courses:

    def __init__(self):
        print('this is about learnig internship')

    def course(self):
        print('the course name is javascript')

class intern(courses):
    def  course(self):
        print('the course name is python')


i = intern()
i.course()

#method overriding
#Using Super(): Python super() function provides us the facility to
#refer to the parent class explicitly.
# Python program to demonstrate
# overriding in multilevel inheritance


# Python program to demonstrate
# overriding in multilevel inheritance


class Parent():
	# Parent's show method
	def display(self):
		print("Inside Parent")
# Inherited or Sub class (Note Parent in bracket)
class Child(Parent):
	# Child's show method
	def show(self):
		print("Inside Child")
# Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):
	# Child's show method
    def show(self):
        print("Inside GrandChild")
    def call(self):
        Child.show(self)
g = GrandChild()
g.show()
g.display()
#g.call()


class add:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('sum of the given 3 numbers is ==', a+b+c)

        elif a!=None and b!=None:
            print('sum of the given 2 numbers ==', a+b)

        else:
            print('the passed number is ==',a)
a =add()
a.sum(2,4)
a.sum(1)
a.sum(5,2,7)


#constructor overloading with inheritence
class Parent:
    def __init__(self):
        print('this message is coming from parent class')

class Child(Parent):
    def __init__(self):
        print('this message is coming child class')


Child()

'''
#constructor overriding
class add:

    def __init__(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('sum of the given 3 numbers is ==', a+b+c)

        elif a!=None and b!=None:
            print('sum of the given 2 numbers ==', a+b)

        else:
            print('the passed number is ==',a)

add(2,3)
add(2)
add(3,2,9)


