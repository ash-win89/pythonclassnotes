#pyton is based on oops in python everything is an object each objects has its properties and methods
#even class also object constructor or else we can say its a blueprint of a program
#to create a class we can 'class' keyword then we can define name following that keyword
'''
class hello:
     x=78
     print('hello world all')

print(hello)
#creating an object
#
h1 =hello
print(h1.x)



#__init__()--a function which always executes when the class being initiated or called,this function used to
#assign values object properties
#constructor -- a constructor always executes when the class called


The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to
 do when the object is being created:


class const:

    #magical methods basically dont have names it will automatically executes when we are calling the class
    #if we want to pass arguments owhile creating object of a class the intializer should be there
    #if we pass arguments into a class object intializers will take those arguments
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
        print('the person name {} and salary is {}'.format(self.name,self.sal))


c = const('rdj',9000)
c
print(c.name)
print(c.sal)


#instance methods --an object can contain methods. object methods are functions that belong to the object
#self -- parameter is a reference to the current instance of the class. we can use it to access the variables
#which are belongs to the class
class const:

    #we can initialize the data in any methods the difference between initializers and methods is
    #initializers can take arguments of the class
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal

    #we cannot pass the instance method parameter's argument directly on class through the object
    #we can pass the data
    def names(self,lname):
        self.lname = lname
        print('the user name is',self.name+lname)

    def salary(self):
        print('the salary gettting paid',self.sal)

ob = const('robert',8000)
ob.names('downey')
ob.salary()

#instead of giving self we can use any names

class const:
    def __init__(mine,name,sal):
        mine.name = name
        mine.sal = sal

    def names(other):
        print('the user name is',other.name)

    def salary(red):
        print('the salary gettting paid',red.sal)

ob = const('robert',8000)
ob.names()
ob.salary()

#modifying the object properties
ob1 =const('ryan',3000)
ob1.sal=5000
ob1.salary()
#deleting an object properties
del ob1.name
ob1.names()


class hello:
    pass
hello
print('hellloworld')

#instance methods--instance attributes not related by objects what we are creating based on classes a method which
#using initializers variables using self every objecs has its own copy instance attribute


#modifying initiated instance variables
class const:
    x=46
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
    def modifyName(self,NewName):
        #once after we changed the self.name even with the different method also it will the
        #new modified data only
        self.name = NewName
        print(self.name,self.sal)
    def modifysalary(self,Newsalary):
        self.sal = Newsalary
        print(self.sal,self.name)
a = const('chris',4000)
print(a.name)
print(a.sal)
a.modifyName('gary')
a.modifysalary(2000)
print(a.name)
print(a.sal)

#static method -- a method is bound to a class rather than the objects for that class or
#static methods does rely on intializer variables it is a stanalone method

class state:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    @staticmethod
    def add(x,y):
        print(x-y)

s =state('newyork', '6000')
s.add(90,70)

'''
#classmethod -- even classmethod also bound to the class not for its objects or
#class method used to access the values which is available inside of a class but which not inside of any methods
#using 'cls' keyword
'''
class const:

    x=46
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
        print(self.x)

    #class method will not allow us to use intilized datas but it will allow us to get class datas
    @classmethod
    def add(cls,y):
        print(cls.x+y)
        


cl = const('gary',90)
cl.add(88)


class const:
    x=67
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
        print('this is a constructor')

    def names(self):
        print('the user name is',self.name)

    def salary(self):
        print('the salary gettting paid',self.sal)

    def detail(self):
        print('name of the person {} and the salary {}'.format(self.name,self.sal))

    @staticmethod
    def add():
        print('hello world')


    def sub(self,a):
        print(self.x-a)

# a =const('rdj','8000')
# a.names()
# a.salary()
# a.detail()
# a.add()
# a.sub(20)


#if we simply call like this it will throw error but by using @classmethod we can do this
#const.names()

const.sub = classmethod(const.sub)
const.sub(40)

#The __str__() function controls what should be returned when the class object is represented as a string.
#If the __str__() function is not set, the string representation of the object is returned:
#The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

'''
#The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  #the __str__ constructor execute the initialized data without print()
  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
'''
'''
#extra notes for assignment:
'''
1.step ahead another examples for class
class Person(object):
    """A simple class."""
    species = "Homo Sapiens"
    # docstring
    # class attribute
    def __init__(self, name):
        """This is the initializer. It's a special
        method (see below).
        """
        self.name = name # special method

    def __str__(self):
        """This method is run when Python tries
        to cast the object to a string. Return
        this string when using print(), etc.
        """
        return self.name # special method
        # instance attribute
    def rename(self, renamed):
        # regular method
        """Reassign and print the name attribute."""
        self.name = renamed
        print("Now my name is {}".format(self.name))

kelly = Person("Kelly")
joseph = Person("Joseph")
john_doe = Person("John Doe")

print(kelly.species)
print(john_doe.species)
print(joseph.species)
print(kelly.name)
print(joseph.name)
print(john_doe.__str__())
john_doe.rename("John")

2.why we need to pass object as a parameter while defining a class:
The reason you may want to extend object explicitly is it turns the class into a new-style class.
 If you don't explicitly specify it extends object, until Python 3,
  it will default to being an old-style class.

3.what is an monkey patching:
"monkey patching" means adding a new variable or method to a class after it's been deﬁned

class A(object):
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return A(self.num + other.num)
       
4.enhanced way of define initializer:

class Person(object):
    def __init__(self, first_name, age, last_name=None):
        if last_name is None:
            self.first_name, self.last_name = first_name.split(" ", 2)
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.full_name = self.first_name + " " + self.last_name
            self.age = age
    def greet(self):
        print("Hello, my name is " + self.full_name + ".")

h = Person('jhon',' constantine','35')
h.greet()

        
5.defining multiple initializer using class method:

class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    @classmethod
    def from_full_name(cls, name, age):
        if " " not in name:
            raise ValueError
        first_name, last_name = name.split(" ", 2)
        return cls(first_name, last_name, age)

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")

rdj = Person('robert','downy','53')
chris = Person.from_full_name('chris Evans','56')
rdj.greet()
chris.greet()

6.appending with class:

class D:
    x = []
    def __init__(self, item):
        self.x.append(item) # note that this is not an assignment!

d1 = D(1)
d2 = D(2)

d1.x


7.to check all the magical methods:

print(dir(list))
'''