#a loop will run as long as the condition is true --while loop
#while -uses to execute as set of statements as long as a conditions is true
#we need a variable for make conditions
#if the condition always pass while become an infinite loop
'''
i=0

while i<15:
    print(i)
#to stop the while we have increment the variable
    i +=1

#break --used to stop the loop even if the while condition is true:
#break not only we can use in while even for loop it will work


i=0

while i<20:

    if i == 15:
        break
    print(i)
    i += 1

'''

#continue--statement we can stop the current iteration, it will pass the loop to the next(or) iteration
#if we want to ignore or stop a value from execution we can continue statement


i=0

while i<20:
    #after the continue if we use incrementation it will become an infinite loop alway do increment before
    #continue statement
    #print(i)
    i += 1
    if i == 15:
        continue
    print('helloworld',i)

else:
    print('the loop used continue')





#extra notes for assignment:

'''
1. we can check multiple conditions and we can apply continue to skip multiple values
ex:
"
for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)
"



'''