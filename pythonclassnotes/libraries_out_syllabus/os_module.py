#We want to create the same subdir1, subdir2 under a new directory dir2,
# which does not exist yet.
import os
os.makedirs("./dir2/subdir1") #if the file alredy exists it will throw error
os.makedirs("./dir2/subdir2")

#to create another file in a existing directory --if the directory not exists it will throw error
os.mkdir("./dir2/subdir1")#this line will throw error bcuz 'dir2' not there

#Create a directory
os.mkdir('newdir')

#Get current directory:
print(os.getcwd())

#Determine the name of the operating system

print(os.name) #This can return one of the following in Python 3: ans :posix

#Remove a directory:

os.rmdir(path)