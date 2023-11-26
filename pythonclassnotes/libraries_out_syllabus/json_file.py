import json
d = {
'foo': 'bar',
'alice': 1,
'wonderland': [1, 2, 3]
}
with open('dummy.json', 'w') as f:
    json.dump(d, f)

#Formatting JSON output:
data = {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"}]}
print(json.dumps(data))

#If we want pretty printing, we can set an indent size:
print(json.dumps(data, indent=2))

#Sorting keys alphabetically to get consistent output

print(json.dumps(data, sort_keys=True))

#Getting rid of whitespace to get compact output

print(json.dumps(data, separators=(',', ':')))

#the difference between 'dump' and 'dumps' if we want to convert a dictionary
#into json just for temproary we can use 'dumps' but we want to create a file we can
#use dump same goes for 'loads' loading a data from a variable but 'load' used to load
#data from a file

data = {u"foo": u"bar", u"baz": []}
json_string = json.dumps(data)
# u'{"foo": "bar", "baz": []}'
json.loads(json_string)
# {u"foo": u"bar", u"baz": []}

from io import StringIO

json_file = StringIO()
data = {u"foo": u"bar", u"baz": []}
json.dump(data, json_file)
json_file.seek(0) # Seek back to the start of the file before reading
json_file_content = json_file.read()
# u'{"foo": "bar", "baz": []}'
json_file.seek(0) # Seek back to the start of the file before reading
json.load(json_file)
# {u"foo": u"bar", u"baz": []}


#Creating JSON from Python dict

import json
d = {
'foo': 'bar',
'alice': 1,
'wonderland': [1, 2, 3]
}
json.dumps(d)

#Creating Python dict from JSON

import json
s = '{"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}'
json.loads(s)