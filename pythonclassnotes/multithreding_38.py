#thread -- it is a subset  of the process. a process can have multithreds
#if we put two threads it will crash with each other
import threading
import time
'''
def hello_five():
    for i in range(5):
        print('hello',i)


def hi_five():
    for i in range(5):
        print('say hi',i)


# hello_five()
# hi_five()

t1 =threading.Thread(target=hello_five)
t2 =threading.Thread(target=hi_five)

t1.start()
t2.start()

import threading

def hello_five():
    for i in range(5):
        print('hello',i)
        time.sleep(1)


def hi_five():
    for i in range(5):
        print('hi there',i)
        time.sleep(1.1)

def message():
    for i in range(5):
        print('good morning',i)
        time.sleep(1.2)

t1 = threading.Thread(target=hello_five)
t2 = threading.Thread(target=hi_five)
t3 = threading.Thread(target=message)

t1.start()
t2.start()
t3.start()

'''

import time  # import time module
import threading
from threading import *


def cal_sqre(num):  # define a square calculating function
    print(" Calculate the square root of the given number")
    for n in num:  # Use for loop
        time.sleep(0.3)  # at each iteration it waits for 0.3 time
        print(' Square is : ', n * n)


def cal_cube(num):  # define a cube calculating function
    print(" Calculate the cube of  the given number")
    for n in num:  # for loop
        time.sleep(0.3)  # at each iteration it waits for 0.3 time
        print(" Cube is : ", n * n * n)


ar = [4, 5, 6, 7, 2]  # given array

t = time.time()  # get total time to execute the functions
cal_cube(ar)
cal_sqre(ar)
th1 = threading.Thread(target=cal_sqre, args=(ar,))
th2 = threading.Thread(target=cal_cube, args=(ar,))
th1.start()
th2.start()
th1.join()
th2.join()
print(" Total time taking by threads is :", time.time() - t)  # print the total time
print(" Again executing the main thread")
print(" Thread 1 and Thread 2 have finished their execution.")

