#\d 0-9 \D 非数字
#\w 单词字符 \W
#\s 空白字符 \S非 空白字符
# .匹配除换行符之外所有字符
#贪婪与非贪婪 python默认是贪婪尽可能取多的
import re
a='pythonf 11\t13java&678p\nh\rp__nihaoC##'
# r=re.findall('\d',a)
# r=re.findall('\D',a)
# r=re.findall('\w',a)
# r=re.findall('\W',a)
# r=re.findall('\s',a)
# r=re.findall('\S',a)
# r=re.findall('[a-z]{3,6}',a)  #贪婪
# r=re.findall('[a-z]{3,6}?',a)
# r=re.findall('c#{1,2}',a,re.I)
# r=re.findall('c#{1,2}?',a,re.I)
print(r)

