#module -- a file with .py extension having some functions that we need to use in our program we can import and use it
'''
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
To create a module just save the code you want in a file with the file extension .py:
'''

from  func_18 import hello,add,sub
hello()
add(89)
sub(7,3)
# import func_18
# func_18.add(45)

from func_18 import add as a
a(78)

#List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)

#extra notes for assignment:
'''
1.to import everything from a model we can use '*'

from math import *
sqrt(4)
# Output: 2.0

2.To install the latest version of a package
$ pip install SomePackage

3.Install from requirements ﬁles
$ pip install -r requirements.txt

4.To list installed packages:
$ pip list
# example output

5.To list outdated packages, and show the latest version available:
$ pip list --outdated

6.Upgrade Packages
$ pip install --upgrade SomePackage

7.To upgrade pip itself, do
$ pip install --upgrade pip

8.To uninstall a package:
$ pip uninstall SomePackage

9.the ﬁrst element in the sys.argv list is the name of the Python script itself, while the rest of the
elements are the tokens passed by the user when invoking the script.

import sys
print(sys.argv)
$ python cli.py
=> ['cli.py']
$ python cli.py fizz
=> ['cli.py', 'fizz']
$ python cli.py fizz buzz
=> ['cli.py', 'fizz', 'buzz']
'''