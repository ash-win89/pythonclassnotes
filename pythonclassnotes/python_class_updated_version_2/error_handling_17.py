#syntax error:-- the written code not in the right format
'''
for i in range(10)
    print(i)
'''

#type error -- if we try to do use operators in between two different data types
'''
a = 'hello world'
b =99
print(a+b)'''

#try block -- uses to test a block code which is inserted inside the try block
#and it always comes up with except block else it will throw
#except--allow us to handle the error
'''
try:
    a = 8/0
    print(a)
except:
    print('the program throws error')
'''
#multiple exceptions -- we can define multiple exceptions blocks as much as we want
#if we want to filter exactly what error is happening there
'''
number = input('enter the value')
try:
    # re = number+4
    # print(re)
    a = int(number)
    div = 4/a
    print(div)
except TypeError:
    print('you are trying add two different data types')
except ZeroDivisionError:
    print('you cannot divide any value by zero')
except:
    print('something went wrong')
'''
'''
else -- to indicate if there is no errors in the try block or no error has been raised by try block
else only will execute when the try block executes
'''
'''
finally --either the try or except or anything executes or not regardless finally block executes
'''
'''
try:
    a=4/2
    print(a)
except:
    print('multiplication went wrong')
else:
    print('no erros has been raised')
finally:
    print('end of the error checking')
'''
'''


raising an exception:  we can choose what error should be thrown if a condition occurs using
'raise' keyword
'''

# x = -2
#
# if x<0:
#     raise Exception('minus values will not be tolerated')
#
# print('the given value is',x)


a = eval(input('enter a values'))

#checking the value is integer or not
if type(a) is not int:
    raise TypeError('you should enter an integer')
print('we got an integer',a)