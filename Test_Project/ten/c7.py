#组
# import re
# a='PythonPythonPython'
# r=re.findall('(Python){1,3}',a)
# print(r)

#匹配模式参数
# re.I忽略大小写  re.S匹配所有字符(包括换行符\n)

import re
a='PythonC#\n_JavaPHP'
r=re.findall('c#.',a,re.I|re.S)
print(r)