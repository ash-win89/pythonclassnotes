'''
while -- as long as the given condition or test expression returns true it will iterate or
loop will run
we can execute some set of results as long as the conditions is true
'''
'''
#formal way of approach
i = 0

while i<=25:
    #print('loop is running',i)
    i += 1

#square summation values
num = 15
summation = 0
c = 1
while c<=num:
    summation = c**2+summation
    c = c+1
print(summation)

#finding the prime number -- a prime cannot be divisible by any numbers except one and itself
c = 0
#divisier = 2
a = [34,12,54,755]
while c< len(a):
    b = a[c]
    if b%2 != 0 and b%3 != 0 and b%4 != 0:
        print('prime number')
    else:
        print('it is not a prime number')
    c +=1




#printing the multiplication table:
a = 12
c=1

while c<11:
    p = a*c
    print(f'{a} x {c} = {p}')
    c +=1
#12x1=1
#12x2=24


#reading a datastructure using while loop
a = (2,4,6,8,10,12,14)
i = 0
while i<len(a):
    print(a[i])
    i += 1

# a= {'a':'apple','b':'banana'}
# b= a.keys()
# i = 0
# print(b[0])
# while i< len(b):
#     #print(a[b])
#     i +=1
#filtering the odd values from a datastructure with nested if case
a = (2,4,6,8,5,10,7,12,14,9)
i = 0
while i<len(a):
    b = a[i]
    # if   b%2 != 0:
    #     print(b)

    i +=1

#even the condition is true still if we want to break look  use 'break'
a = (2,4,6,8,5,10,7,12,14,9)
i = 0
while i<len(a):
    if a[i]%2 != 0:
        break
    print(a[i])
    i +=1

s = 'hello world'
c = 0
while c<len(s):
    pass
    # c +=1

'''    

#even the condition is true some particular value want to skip use 'continue'
#without executing the codes which comes after continue key push the loop into next loop
a = (2,4,6,8,5,10,7,12,14,9)
i = 0
while i<len(a):
    b = i
    i += 1
    if a[b]%2 != 0:
        continue
    print(a[b])
else:
    print('loop closed')

