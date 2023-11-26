'''
for --used to iterating over a sequence ('string',tuple,list,set,dict,set)
its does not require an indexing
'''
'''
a = ['apple',50,'orange',20]

for i in a:
    print(i)


for i in 'goodmorning':
    print(i)


#using a break statement:

a = [4,2,7,8,9,1]
#first it will check the condition then it will allow to print
for i in a:
    if i ==8:
        break
    print(i)

# first it will print the values then it will check the condition
a = [4,2,7,8,9,1]
for i in a:
    print(i)
    if i == 8:
        break

#continue keyword in for
a = ['apple','','orange','','kiwi']
# first it will check the condition then it will allow to print
for i in a:

    if i == '':
        continue
    print(i)



#range in for loop

for i in range(10,30,3):
    print(i)
else:
    print('loop broken')

#nested for loop
fruit = ['apple','orange','kiwi','cherry']
colors = ['red','green','yellow']

for i in fruit:
    for j in colors:
        print(f'the fruit is {i} and the color fruit is {j}')


a= {'carrot':10,'beets':6,'drumstick':7}
#print(a)
#if we pass a dictionary in a for loop it will print keys only
for i in a:
    print(i,a[i])
    #print(a.get(i))

a = (34,56,7,8,91,23)
#printing the values and index position as well
for i in a:
    print(i,a.index(i))

a = (34,56,7,8,91,23)
#to bring all the datas in a same line 'end = ''
for i in a:
    if i%2 == 0:
        print(i, end=' ')

a = (34,56,7,8,91,23)
#enumerate used to find indexing 
for count,i in enumerate(a):
    print(f'the value is {i} and the index position is {count}')
    pass

a = (34,56,7,8)
fruit = ['apple','orange','kiwi','cherry']

for i,j in zip(a,fruit):
    print(f'the price of the fruit {i} is {j} ')
    #pass


#creating a triangle

for i in range(10):
    for j in range(i):
        print('*', end='')
    print()

#number triangle:

for i in range(10):
    for j in range(i):
        print(j, end='')
    print()


a =[2,4,6,8,9,7,5,4]

i = 0
while i< len(a):
    b = a[i]

    i += 1
    if b%2 != 0:
        continue
    print(b)
'''
# i = 'yes'
# while i == 'yes':
#     a = eval(input('enter the first value'))
#     print(a)
#     i = input('do you want to continue yes/no')




if __name__ == "__main__":
    hello()