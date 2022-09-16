#\d \D
#\w等价于
import re
s='abc,acc,adc,aec,afc,ahc'
# r=re.findall('a[^deh]c',s)
r=re.findall('a[c-f]c',s)
print(r)
print(len(r))