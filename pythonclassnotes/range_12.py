#range data structures
#if we perform range with single value passed it will take default starting from 0
a = range(10)
print(a)
for i in a:
    print(i)

print('===========================')
#if we pass two values it will take first valu as starting range and last value as ending range
b = list(range(5,15))
print(b)
for i in b:
    print(i)
print('===========================')
#if we pass three values first value for starting and second value for ending and third value for interval or step
for i in range(1,30,3):
    print(i)

#it will not support any kind of function or operations
