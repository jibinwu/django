#边界匹配
import re
qq='10000100'
# r=re.findall('\d{3,6}?',qq)
# r=re.findall('100$',qq)
r=re.findall('^100',qq)
print(r)
