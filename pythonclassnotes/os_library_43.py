#when it comes to handle the path 'os' library will be quite helpful
#'join' method used to concatenate datas;

import os

a = os.path.join('a',' for', ' apple')
print(a)# ans  --a/ for/ apple in linux

#get current working directory 'getcwd()' -- path component manipulations methods:

p = os.path.join(os.getcwd(),'hello.txt')
print(p)

#to find the directory use 'dirname'
d= os.path.dirname(p)
print(d)

#to get the file name use 'basename'
f= os.path.basename(p)
print(f)
# to split the directory and filename we can use 'split' operation
dp = os.path.split(os.getcwd())
print(dp)

#split text from the basename from extension:
sp = os.path.splitext(os.path.basename(p))
print(sp)

#to check the path exists  or not we can use 'exists' and it will return true if the path exists
path = '/home/pugal/Desktop/pythonclassnotes'
print(os.path.exists(path))

#to check the given pathe is a directory:
print(os.path.isdir(path))

#to check the given path is a file:
p = path+'/hello.txt'
print(os.path.isfile(p))