import base64
s=base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d=base64.b64decode(s).decode('utf-8')
print(d)

c=base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(c)
e=base64.urlsafe_b64decode(c).decode('utf-8')
print(e)
