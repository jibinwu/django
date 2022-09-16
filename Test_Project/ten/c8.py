import re
a='PythonC#JavaC#PHPC#'
print(id(a))
r=re.sub('c#','Go',a,0,re.I)
a=a.replace('C#','Go')
print(a)
print(id(a))
# print(r)
