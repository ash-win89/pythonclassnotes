
'''
#inner class -- a class defined in another class is known inner class or else we can call it as a nested class
class outer:

    def __init__(self):
        print('this message comes from outer class')

    def dummy(self):
        print('this message comes from outer class method')
    class inner:
        def __init__(self):
            print('this message comes from inner class')

        def hello(self):
            print('hello world')

a=outer()
b= a.inner()
b.hello()
a.dummy()



#For the grouping of two or more classes. Suppose we have two classes remote and battery.
# Every remote needs a battery but a battery without a remote won’t be used.
# So, we make the Battery an inner class to the Remote. It helps us to save code.

# create outer class
class Doctors:
	def __init__(self):
		self.name = 'Doctor'
		self.den = self.Dentist()
		self.car = self.Cardiologist()

	def show(self):
		print('In outer class')
		print('Name:', self.name)

	# create a 1st Inner class
	class Dentist:
		def __init__(self):
			self.name = 'Dr. Savita'
			self.degree = 'BDS'

		def display(self):
			print("Name:", self.name)
			print("Degree:", self.degree)

	# create a 2nd Inner class
	class Cardiologist:
		def __init__(self):
			self.name = 'Dr. Amit'
			self.degree = 'DM'

		def display(self):
			print("Name:", self.name)
			print("Degree:", self.degree)


# create a object
# of outer class
outer = Doctors()
outer.show()

# create a object
# of 1st inner class
d1 = outer.den

# create a object
# of 2nd inner class
d2 = outer.car
print()
d1.display()
print()
d2.display()
'''
'''
Multilevel inner class
The class contains an inner class and that inner class again contains another inner class,
 this hierarchy is known as the multilevel inner class.
'''
# create an outer class
class Geeksforgeeks:

	def __init__(self):
		# create an inner class object
		self.inner = self.Inner()

	def show(self):
		print('This is an outer class')

	# create a 1st inner class

	class Inner:
		def __init__(self):
			# create an inner class of inner class object
			self.innerclassofinner = self.Innerclassofinner()

		def show(self):
			print('This is the inner class')

		# create an inner class of inner

		class Innerclassofinner:
			def show(self):
				print('This is an inner class of inner class')


# create an outer class object
# i.e.Geeksforgeeks class object
outer = Geeksforgeeks()
outer.show()
print()

# create an inner class object
gfg1 = outer.inner
gfg1.show()
print()

# create an inner class of inner class object
gfg2 = outer.inner.innerclassofinner
gfg2.show()
