'''File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.'''


#to check the files existing or not;

#to check a file whter its empty or not:
'''
import os

fpath = 'file_1.txt'
def is_empty_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

print(is_empty_file(fpath))


#another way to check the file exists or not:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#To delete an entire folder, use the os.rmdir() method:
import os
os.rmdir("python_class_updated_version_2")
'''
#Note: You can only remove empty folders.

#creating , reading ,writing, updating, deleting
#open() --if you want work with a file use 'open()' to get access to handle the file
#open() will take two parameters first one is the file name second one is the mode open operation

#'w'--used to create a new file and if the file already it will remove all the existing data from that file and enter the
#new given files if it is not exist it will create new file

f = open('file_1.txt','w')
f.write('good morning \n the day name today is thursday')
f.close()

#r- it is a immutable status mode which we are not able to change the file's existing data just we can read it
'''
f = open('file_1.txt','r')
#print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

#'a' - append will not erase the existing data in a file but it will add more datas in that file

f = open('file_1.txt','a')
f.write('\n this line added by append mode')

#'x' -- to check a file already exists or not before creating a file with a same name


f = open('file_1.txt','x')

#with statement -- what code that we are writing for that file will open out of the it will get close:


with open('file_1.txt','r') as f:
    print(f.read())
#print(f.read())#I/O operation on closed file.


#to get to know count of lines 
f = open('file_1.txt','r')
count_lines = 0
for i in f:
    print(i)
    count_lines +=1

print(count_lines)

f = open('file_1.txt','r')
print(f.tell())
f.seek(7)
print(f.tell())
print(f.read())



f = open('python.jpeg','rb')
f1 = open('newPic.png','wb')
data = f.read()
print(data)
f1.write(data)


import csv#csv library created using lists for huge data it will take some time
#then pandas

with open('category.csv','r') as f:
    file = csv.reader(f)

    for i in file:
        print(i)

        with open('stores.csv','a') as d:
            data = csv.writer(d)
            data.writerow(i)


import json

#1.reading a json file
f = open('sample.json','r')
#load -- accept the variable populate the data as python dictionary
data = json.load(f)
#print(data)

for i in data:
    print(i)

#f = '{"pk": 1,"model": "business_category.BusinessCategory"}'
#loads --it will not take file path return the content from a string format
# data = json.loads(data)
# print(data)

#writing  json file
    with open('demo.json','a') as f:
        json.dump(i,f)
#print(dir(json))-- will return all the methods in a library



#Because "r" for read, and "t" for text are the default values, you do not need to specify them.
f = open("demofile.txt", "rt")

#Open a file on a different location:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

#Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))

#Remove the file "demofile.txt":

import os
os.remove("demofile.txt")

'''
'''
#extra notes for assigment:

1.another way of writing a file:

with open('fred.txt', 'w') as outfile:
    s = "I'm Not Dead Yet!"
    print(s) # writes to stdout
    print(s, file = outfile) # writes to outfile

2.to replace some words with existing words in your files:

import fileinput
replacements = {'Search1': 'Replace1',
                'Search2': 'Replace2'}
for line in fileinput.input('filename.txt', inplace=True):
    for search_for in replacements:
        replace_with = replacements[search_for]
        line = line.replace(search_for, replace_with)
    print(line, end='')
3.in a short way copy all the datas from one file to another file:
with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
        out_file.write(line)

or:
Using the shutil module:
import shutil
shutil.copyfile(src, dst)    
    

4.reading particular lines from a file --slicing:
import itertools
with open('myfile.txt', 'r') as f:
    for line in itertools.islice(f, 12, 30):    
    
5.writing file:

with open('.txt', 'w') as outfile:
    s = "I'm Not scared of the dark!"
    print(s) # writes to stdout
    print(s, file = outfile) # writes to outfile
    
'''