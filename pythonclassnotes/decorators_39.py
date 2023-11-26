#one function which is taking another function as a parameter that function we used to call as a decorator
#without touching the original function if we need add some more attributes we can use decorators

'''
def decorating(a):
    def inner():
        print('this is the extra added line')
        a()
    return   inner



def normal():
    print('this is the normal function')

obj = decorating(normal)
obj()
'''

#@ --method used to provide the propertiess from the decorator to the orgin function

def zerofinder(func):
    def inner(a,b):
        if b == 0:
            print('if we use zero in denominator we will get zerodivision error')
            return
        return func(a,b)
    return inner


@zerofinder
def divide(a,b):
    print(a/b)

divide(6,2)
divide(5,0)

#extra notes for assignment:
'''
1.printing a result using return simple method:

def super_secret_function(f):
    return f

@super_secret_function
def my_function():
    print("This is my secret function.")

mu_f = super_secret_function(my_function())
mu_f

2.stop a function from giving result without touching it using decorators:

def disabled(f):
    """
    This function returns nothing, and hence removes the decorated function
    from the local scope.
    """
    pass

@disabled
def my_function():
    print("This function can no longer be called...")

#my_function()#we will get type error
#print(my_function)#answer is null

3.using the decorators with *args and **kwargs:

def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)  # Call the original function with its arguments.
    return inner_func

@print_args
def multiply(num_a, num_b):
    return num_a * num_b

print(multiply(3, 5))
# Output:
# (3,5) - This is actually the 'args' that the function receives.
# {} - This is the 'kwargs', empty because we didn't specify keyword arguments.
# 15 - The result of the function.

4.how to pass value into a decorator:

def decoratorfactory(message):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator wants to tell you: {}'.format(message))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator

@decoratorfactory('Hello Ultron')
def hello():
    pass

hello()

5.using the decorators to get function name, docstrings :

from functools import wraps

def decorator(func):
    # Copies the docstring, name, annotations and module to the decorator
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped_func

@decorator
def hello():
    """function derived  by pugal"""
    pass

print(hello.__name__)
print(hello.__doc__)
'''
