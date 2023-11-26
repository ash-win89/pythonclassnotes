import base64

s = "Hello World!"
b = s.encode("UTF-8")
print(b)


#To Base64 encode these bytes, we use the base64.b64encode() function:
import base64
s = "Hello World!"
b = s.encode("UTF-8")
e = base64.b64encode(b)
print(e)  #ans --b'SGVsbG8gV29ybGQh'