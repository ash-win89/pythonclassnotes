#try -- try block used to put our suspicious code inside of it and try block will return result when the code runs properly
#except -- when the try block code throws error except will execute

'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''


#a = 5/0
# a = 8
# b= 'hello'
# print(a+b)
'''
#basic
try:#where we can test our code
    x =5/4
    print(x)
except:#let us handle the error
    print('something went wrong')


#hanling different errors

try:
    a=8
    b = 'hello'
    x = a+b
    print(x)
except TypeError:
    print('you are trying to add two different data types')
except ZeroDivisionError:
    print('code that you have written having Zerodivisionerror')
except:
    print('invalid syntax')




#else-- case will execute when the try block found no errors :

#finally -- this block will execute always  whether the program raises error or not it will never care about that
try:
    a = 4
    b = 'hello'
    x = a / b
    print(x)
except TypeError:
    print(TypeError)
except:
    print('code that you have written having error')

else:
    print('there is no errors program succeeded')
finally:
    print('end of the error handling')

'''
'''
class Error(Exception):
    pass

class ValueSmallError(Error):
    pass

class ValueBigError(Error):
    pass

number = 10

while True:#the condition is true always so we have to break the loop using 'break'

    try:
        gues_num = int(input('enter you guess'))
        if gues_num < number:
            raise ValueSmallError
        elif gues_num > number:
            raise ValueBigError
        break#if its not reach break the loop will run again and again
    except ValueSmallError:
        print('guessed number too small')
    except ValueBigError:
        print('guessed value too big')
print('the guessed number matched you won')


#Try to open and write to a file that is not writable:
try:
  f = open("file_1.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


#Raise an error and stop the program if x is lower than 0:

x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
else:
    print('given value is bigger than zero')


The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.
'''

x = eval(input('enter the value'))

if not type(x) is int:
  raise TypeError("Only integers are allowed")
else:
    print(x*x)


#extra things for assignment

"""
1.to get all the list of errors use "print(dir(__builtins__))" and all the keywords and dunder methods
2.error handling inside of a function:
def input_number(msg, err_msg=None):
while True:
    try:
        return float(input(msg))
    except ValueError:
        if err_msg is not None:
            print(err_msg)
            
user_number = input_number("input a number: ", "that's not a number!")


"""

#print(dir(__builtins__))#checking builtins values