'''
file handling -- to read and write files along with many other files to operate on files
syntax:
f = open(filename,mode)

r-read--open an existing file for  a read operation which is immutable
w-write -- open an existing file. if the file already containing some datas that will deleted and the
new values will be created or override the existing data and enter the new data
a-append -- it wont override. but we can enter new as well
r+-- read and write the file, the previous data will overriden
w+-- write and read data.will override existing data
a+ -- to append and read  the data. it will not override

'''

#to read a variable which contains the data about the file we need to use