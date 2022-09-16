from urllib import request
#断点调试
class  Splider():
    url='https://www.panda.tv/cate/lol?pdt=1.24.s1.3.1984u5eomev'

    def __fetch_content(self):
        r=request.urlopen(Splider.url)
        htmls=r.read()
        a=1

    def go(self):
        self.__fetch_content()
splider=Splider()
splider.go()
