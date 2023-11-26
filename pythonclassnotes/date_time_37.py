#date time:

import datetime
'''
#print local machine time
x = datetime.datetime.now()
print(x)

#to print year we have to use 'year' keyword
print(x.year)
print(x.month)
print(x.day)
print(x.second)
print(x.hour)
print(x.microsecond)
print(x.minute)


#to get string format use keyword 'strftime'
print(x.strftime('%A'))
print(x.strftime('%B'))
print(x.strftime('%a'))
print(x.strftime('%b'))

#to get to know the day of a particular year

y = datetime.datetime(1998,8,3)
print(y.strftime('%B'))
print(y.strftime('%A'))


import time

#time library has 'sleep()' which will freeze the program till the mentioned timing

print('this message will come immediately')

time.sleep(3)
print('this message will pring after 3 secs')

#creating digital clock using time library:
'''
import time

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p",localtime)
    print(result)
    time.sleep(1)


#extra notes for assignment:
'''
1.to parse a datetime from a string 
ex:
import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)

2.if we want to compute the time differences in between two dates:
"from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2016, 5, 23)
# datetime.datetime(2016, 05, 23, 0, 0, 0)
delta = now-then
print(delta.days)
print(delta.microseconds)"

3. finding the days difference between two dates:
# Python3 program to find number of days
# between two given dates
from datetime import date


def numOfDays(date1, date2):
    return (date2 - date1).days


# Driver program
date1 = date(2018, 12, 13)
date2 = date.today()
print(numOfDays(date1, date2), "days")

'''
