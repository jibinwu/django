import re
# r=re.findall('a{3,5}?','aaaaaammmmmmm')
# print(r)
# r=re.findall('\d{3}\s+\d{3,}','123  4567891111')
# print(r)

# r=re.findall('\d{3}\s+\-\s+\d{5}','010 - 12345')
# print(r)

# r=re.findall('python','python1234Python',re.I)
# print(r)
# r=re.match(r'^\d{3}\-\d{3,8}$', 'a10-12345')
# print(r)


# r=re.findall('^(\d{3})\-(\d{3,8})','010-12345')
# print(r[0][1])

# r=re.match('^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$','2-30')
# print(r.groups())

# a = 'ABC'
# b = a
# a = 'XYZ'
# a = 'jbw'
# b=a
# print(b)
# print(a)

def add(x,y):
    return x+y
r=add(1,2)
print(r)