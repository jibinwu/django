import re
newsurl='http://news.sina.com.cn/o/2018-05-02/doc-ifzyqqip9992790.shtml'
# print(newsurl.strip())
# print(newsurl.split('/')[-1].lstrip('doc-').strip('.shtml'))
r=re.findall('doc-i(.*).shtml',newsurl)
print(r[0])
# m=re.search('doc-i(.*).shtml',newsurl)
# print(m.group(0))
# print(m.group(1))
