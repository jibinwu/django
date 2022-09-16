import re
s='life is short,i use python,i love python you and me python'
# r=re.search('life(.*)python(.*)python',s)
# r=re.findall('life(.*)python(.*)python',s)
# r=re.findall('life(.*?)python',s)
# print(r)
# print(r.group(1))
# print(r[0][0])
# print(r.group(2))
# print(r.span())
# print(r.group(1,2))
# print(r)


def add(*args):#一个元组
    print(args)
    for i in args:
        print(i)
add('jbw','18','男')

def add1(**kwargs):#一个字典
    print(kwargs)
    for value in kwargs.keys():
        print(value)
add1(name='jbw',age='18',sex='男',school='光明小学')

