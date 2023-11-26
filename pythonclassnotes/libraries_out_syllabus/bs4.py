'''webscrapping here we are going to use beautifulsoup4 so to install beautifullsoup4
use 'pip install bs4' and following that we cannot directly use htmlparser it will throw the error
while we are trying to parse the broken html codes for that we have to insert 'lxml' parser library
'pip install lxml' '''

#importing beautifulsoup: and we need an html here the webscrap.html to do
from bs4 import BeautifulSoup

#reading the html file:
with open('webscrap.html', 'r') as html_file:
    content = html_file.read()
    #print the entire content from the html file
    print(content)
    #scrapiing the htmlpage using beautifulsoup
