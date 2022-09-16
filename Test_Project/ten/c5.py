# *匹配0次,1次或者无限次
# +匹配1次或者无限次
# ?匹配0次,1次
import re
a='pytho0python1pythonn2pythonnnn3'
# r=re.findall('python',a)
# r=re.findall('python*',a)
# r=re.findall('python+',a)
# r=re.findall('python?',a)
# r=re.findall('python{0,3}',a)
r=re.findall('python{0,3}?',a)
# r=re.findall('python{0,3}',a)


print(r)