#regular expression --special sequence of characters which helps us to find or match in a sentence

#starts with finder:

import re

str = 'the highest falls in the world is nayagara'

#to check whether sequence starts with particular word
x = re.findall('^the',str)
#print(x)

#to check whether sequence ends with particular word
y = re.findall('nayagara$',str)
#print(y)


#finding the boundary characters using []

str = 'the highest falls in the world is nayagara'

x= re.findall('[a-m]',str)
print(x)



str = 'the tall and small and itans fall anything'
#to fetch the 'an' returns the data how many times it is available inside of the sequence
x= re.findall('anx*',str)
print(x)
'''

#the srting contains 'a' that followed two l's:

str = 'the talll and small and its fall so its al'
x= re.findall('al{2}',str)
print(x)

#finding the either condition
str = 'the talll and small and its fall so its al'
x= re.findall('talll|small',str)

print(x)

#try to find a particular word in our string

str = 'the talll and small and its fall so its al'
x= re.findall('fall',str)
print(x)


#search() --used to search a string for a match -- used find the first occurance


str = 'thetalll and small and its fall so its al'
x= re.search('so',str)
print('the white space available in the position no',x)


str = 'the talll and small and its fall so its al'
x= re.search('fal',str)
print(x)

#we want to break our sentence based on some character use split()
str = 'the talll and small and its fall so its al'
x= re.split('\s',str)
print(x)


#trying to replace one value instead another

str = 'the talll and small and its fall so its al'
x= re.sub('\s','_',str)
print(x)

#filtering integers in a string

str = 'the 1 st thing we have to wake up 5 o clock on 23 rd'
x = re.findall('[0-9][0-9]',str)
print(x)


#filtering special char in a string

str = 'the $ st thing@ we have to wake% up 5$ o @clock on 23 rd'
x = re.findall('[@,$]',str)
print(x)
#group() --want to find the similar word starts with particular character

#a character with entire string
str = 'the morning sunlight too bright'
x = re.search(r'\bs\w+', str)
print(x.group())

#find the  starting position and ending position of a word starts with particular character

str = 'the morning sunlight too bright'
x = re.search(r'\bs\w+', str)
print(x.span())
'''

#extra notes for assignment:
'''
1.The ﬁrst argument of re.match() is the regular expression, the second is the string to match:
import re
pattern = r"123"
string = "123zzb"
re.match(pattern, string)
match = re.match(pattern, string)
match.group()

2.Searching

pattern = r"(your base)"
sentence = "All your base are belong to us."
match = re.search(pattern, sentence)
match.group(1)
# Out: 'your base'
match = re.search(r"(belong.*)", sentence)
match.group(1)
# Out: 'belong to us.'

3.You can also search at the beginning of the string (use ^ ),
match = re.search(r"^123", "123zzb")
match.group(0)
# Out: '123'
match = re.search(r"^123", "a123zzb")
match is None
# Out: True

4.at the end of the string (use $ ),
match = re.search(r"123$", "zzb123")
match.group(0)
# Out: '123'
match = re.search(r"123$", "123zzb")
match is None
# Out: True
or both (use both ^ and $ ):
match = re.search(r"^123$", "123")
match.group(0)
# Out: '123'

5.Precompiled patterns
import re
precompiled_pattern = re.compile(r"(\d+)")
matches = precompiled_pattern.search("The answer is 41!")
matches.group(1)
# Out: 41
matches = precompiled_pattern.search("Or was it 42?")
matches.group(1)
# Out: 42

6.Flags keyword
#Below an example for re.search but it works for most functions in the re module.
m = re.search("b", "ABC")
m is None
# Out: True
m = re.search("b", "ABC", flags=re.IGNORECASE)
m.group()
# Out: 'B'
m = re.search("a.b", "A\nBC", flags=re.IGNORECASE)
m is None
# Out: True
m = re.search("a.b", "A\nBC", flags=re.IGNORECASE|re.DOTALL)
m.group()
# Out: 'A\nB'

"
Common Flags
Flag
Short Description
re.IGNORECASE , re.I Makes the pattern ignore the case
re.DOTALL , re.S
Makes . match everything including newlines
re.MULTILINE , re.M Makes ^ match the begin of a line and $ the end of a line
re.DEBUG
Turns on debug information

7.Replacing strings
re.sub(r"t[0-9][0-9]", "foo", "my name t13 is t44 what t99 ever t44")
# Out: 'my name foo is foo what foo ever foo'
8.Using group references Replacements with a small number of groups can be made as follows:

re.sub(r"t([0-9])([0-9])", r"t\2\1", "t13 t19 t81 t25")
# Out: 't31 t91 t18 t52'"

9.Using a replacement function
items = ["zero", "one", "two"]
re.sub(r"a\[([0-3])\]", lambda match: items[int(match.group(1))], "Items: a[0], a[1], something,
a[2]")
# Out: 'Items: zero, one, something, two'
'''