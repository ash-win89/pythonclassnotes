#to make some search on google we need 'beatifulsoup4' and a python library called 'google'
from googlesearch import search

query = "Geeksforgeeks"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	print(j)
