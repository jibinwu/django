import re
a='C1++2Java3C#4Python5Javascript6Python7Go8Python9'
# r=re.findall('\d',a)
r=re.findall('\D',a)
if  len(r)>0:
    print('字符串中包含Python')
else:
    print('找不到Python')
print(r)
# print(type(r))
print(len(r))
