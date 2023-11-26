'''
modules in python -- a file that contains a set of functions that we can include in our
current files or application
any file that saved along with the extension of .py

'''
#import method 1:
from  funtions_14 import hello
#hello()
#import method 2:
# import funtions_14
# funtions_14.hello()

#import method 3: renaming a module
#
import funtions_14 as f
# f.hello()
# f.add(89,888)

'''
#variables in a module: - a module can contain variables of all types(data types, arrays,dictionaries etc)
import main

data = main.person
name = data['name']
print(name)'''

#builin-modules- there are lot of modules built in  in python we can import it whereever we want

import platform
#to get to know what platform we are working
x = platform.system()
print(x)

#to get to know the current directory
x = dir(f)
print(x)
import pandas
#to get to know all the pandas function
#print(dir(pandas))

# import numpy
# print(dir(numpy))