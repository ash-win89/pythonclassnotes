'''
import urllib.request
print(urllib.request.urlopen("http://stackoverflow.com/documentation/"))
# Prints: <http.client.HTTPResponse at 0x7f37a97e3b00>
response = urllib.request.urlopen("http://stackoverflow.com/documentation/")
print(response.code)
# Prints: 200
print(response.read())'''

import urllib.request
response = urllib.request.urlopen("http://stackoverflow.com/")
data = response.read()
encoding = response.info().get_content_charset()
html = data.decode(encoding)
print(html)