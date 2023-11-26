#polymorphism -- one operation can be perfomed multiple ways --the same function name but that can do
# different operations
#polymorphism --will allow to define methods with the same name for both classes which means even child class also
#parent also can have same name methods
'''
duck typing in Python-Earlier, we have discussed that Python is a dynamic typed language.
 However, we can
use the dynamic approach with custom data types. Let's understand the following example.

#type 1:

class VisualStudio:
    def execute(self):
        print('Compiling')
        print('Running')
        print('Spell Check')
        print('Convention Check')


class Desktop:
    def code(self, ide):
        ide.execute()


ide = VisualStudio()
desk = Desktop()
desk.code(ide)


#type2:
class england():
    def capital(self):
        print('the capital ciy of england is london')

    def language(self):
        print('the mother language of england is british english')

    def type(self):
        print('it is a developing country')


class America():
    def capital(self):
        print('the capital ciy of america is newyork')

    def language(self):
        print('the mother language of england is america english')

    def type(self):
        print('it is a developed country')


eng = england()
am = America()

for country in (eng,am):
     country.capital()
     country.language()
     country.type()

'''
class Duck():
    def sound(self):
        print('quack,quack')


class lion():
    def sound(self):
        print('roaring')

    def legs(self):
        print('4 legs')

class cat():
    def sound(self):
        print('meow,meow')

    def legs(self):
        print('4 legs')

class hynas():
    def sound(self):
        print('laughing')

def call(x):
    x.sound()

def walk(y):
    y.legs()


lists = [Duck(),lion(),cat(),hynas()]
w = [lion(),cat()]
w[0].legs()
w[1].legs()

for x in lists:
    call(x)


