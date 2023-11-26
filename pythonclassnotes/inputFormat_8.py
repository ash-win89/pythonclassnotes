#string formatting -- passing strings inside of a sentences:

name = input('enter the name')
marks = int(input('enter marks'))
grade = eval(input('enter the grade'))
#method1--substituting is not an mutable operation
print('the student name is %s and the marks he earned %d and the grade he earned %f'%(name,marks,grade))

#method2
print('the student name is {} and the marks he earned {} and the grade he earned {}'.format(name,marks,grade))

#method 3: f'string:
print(f'the student name is {name} and the marks he earned {marks} and the grade he earned {grade}')

#extra notes for assignment:
'''
1.Named arguments can be also used:
print("X value is: {x_val}. Y value is: {y_val}.".format(x_val=2, y_val=3))

2.Object attributes can be referenced when passed into str.format:

class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('My value is: {.value}'.format(my_value))


3.Dictionary keys can be used as well:
my_dict = {'key': 6, 'other_key': 7}
print("My other key is: {0[other_key]}".format(my_dict))

4.with tuples and lists:
my_list = ['zero', 'one', 'two']
print("2nd element is: {0[2]}".format(my_list))

5.format allows behaviour not possible with % , for example repetition of arguments:

t = (12, 45, 22222, 103, 6)
print '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*t)

6.As format is a function, it can be used as an argument in other functions:
number_list = [12,45,78]
print map('the number is {}'.format, number_list)
# Out: ['the number is 12', 'the number is 45', 'the number is 78']

7.Format literals (f-string):
allowing you to prepend f to the
beginning of a string literal to eﬀectively apply .format to it with all variables in the current scope.

foo = 'bar'
print(f'Foo is {foo}')#ans -Foo is bar
print(f'{foo:^7s}')# ans-- bar --indexing

8.nested string formatting:

price = 478.23
print(f"{f'${price:0.2f}':*>20s}")
#ans --*************$478.23

9.function can be callable inside of a "f'()" string formating:
def add(x,y):
    return  x+y

print(f'{add(5,89)} {add(65,34)}')
ans --94 99

10.float formatting with "f'()" based on numbers:

print('{0:.3f}'.format(42.12345)) #ans --42.123

#another way around:
'{:.3f}'.format(42.12345)
#or

print('{answer:.3f}'.format(answer=42.12345))

11.Named placeholders using .format:

data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format_map(data))

12.nested formatting:

print('{:.>10}'.format('foo')) # ans --.......foo

13.line aligning:

data = ["a", "bbbbbbb", "ccc"]
m = max(map(len, data))

for d in data:
    print('{:>{}}'.format(d, m))

#ans:
"
      a
bbbbbbb
    ccc"
    
14.Format using Getitem and Getattr:
#with dictionary:

person = {'first': 'Arthur', 'last': 'Dent'}
print('{p[first]} {p[last]}'.format(p=person))

ans:Arthur Dent

15.with class:

class Person(object):
    first = 'Zaphod'
    last = 'Beeblebrox'

print('{p.first} {p.last}'.format(p=Person()))

#ans:Zaphod Beeblebrox
    

'''