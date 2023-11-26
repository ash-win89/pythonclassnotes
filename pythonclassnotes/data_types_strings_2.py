#Strings in python are surrounded by either single quotation marks, or double quotation marks
print("Hello")
print('Hello')

a = "Hello"
print(a)

#You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
#Square brackets can be used to access elements of the string.

#Looping Through a String
#Loop through the letters in the word "banana":

for x in "banana":
  print(x)

#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#check string:--Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

#slicing
b = "Hello, World!"
print(b[:5])

#Upper Case
a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
