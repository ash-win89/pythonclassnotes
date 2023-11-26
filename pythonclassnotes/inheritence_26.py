#inheritence --allows us to define a class that inherits all the methods and
# properties from another class
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.
#sinngleinheritence: -- there can one to one relationship only one parent one child method
'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
print(x.lastname)

'''
'''
Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its 
parent.We want to add the __init__() function to the child class 
(instead of the pass keyword).Note: The __init__() function is called automatically every time the class is being used to create a new object.

When you add the __init__() function, the child class will no longer inherit the 
parent's __init__() function.Note: The child's __init__() function overrides the
inheritance of the parent's __init__() function.To keep the inheritance of the parent's
__init__() function, add a call to the parent's __init__() function:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    self.salary = 8000

x = Student("Mike", "Olsen")
x.printname()
print(x.salary)

'''
'''
Now we have successfully added the __init__() function, 
and kept the inheritance of the parent class,
and we are ready to add functionality in the __init__() function.
Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#Add a property called graduationyear to the Student class:


'''
'''
In the example below, the year 2019 should be a variable, and passed 
into the Student class when creating student objects.
To do so, add another parameter in the __init__() function:
Add a year parameter, and pass the correct year when creating objects:

'''
'''

#A class can be derived from more than one base class in Python, similar to C++.
# This is called multiple inheritance.

class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        #if we are getting more key values pairs we can initialize them by using super
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area

r = RightPyramid(5,3)
print(r.area())
print(r.area_2())

#multipleinheritence-- many to one --ther can be multiple parents one child

class first:
    def hi(self):
        print('this is first class')

class second:

    def hello(self):
        print('this is second class')

class third(first,second):
    #instead using object to call every inherited class method we can do at once using define a method
    #in that method we can call all the class by passing self keyword
    def no(self):
        print('this is third class')



t = third()
t.no()
t.hi()
t.hello()
#t.nos()
'''
#multilevel or hybrid inheritence -- many to many --there can be multiple childs and multiple classes
#a class can be derived from more than one parent or base classes

class first:
    def no(self):
        print('this is first class')

class second:

    def hello(self):
        print('this is second class')

class third(first,second):
    def no(self):
        print('this is third class')

class fourth(third):
    def no(self):
        print('display all the values from the multilevel inhertence clases')
        #super(fourth).no(self)
        third.no(self)
        second.hello(self)
        first.no(self)
        print('this is fourth class')

# f= fourth()
# f.no()
# f.hello()

#bringing all the datas and initializing all the methods using super
class hi(fourth):
    def __init__(self, *args, **kwargs):
        super(hi,self).__init__(*args,**kwargs)

hi.no(super)
