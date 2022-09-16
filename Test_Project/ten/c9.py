import re
a='PythonC#JavaC#PHPC#'
# r=re.sub('c#','Go',a,0,re.I)
def covert(value):
    # print(value)
    # print(value.group())
    # name=value.group()
    return '!!'+value+'!!'

r=re.sub('c#',covert,a,0,re.I)
print(r)