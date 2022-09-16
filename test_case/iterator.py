# try:
#     print('try...')
#     r=10/0
#     print('result:',r)
# except  ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally....')
# print('end')



# from functools import reduce
#
# def str2num(s):
#     return int(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     try:
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
#
# main()


# filename=r'G:\测试.txt'
# try:
#     with open(filename) as f:
#         contens=f.read()
# except  FileNotFoundError:
#         print('sorry,the file %s does not exist.'%filename)
# else:
#     words=contens.split()
#     count=len(words)
#     print('%s含有%d个字'%(filename,count))

# tilte='Alice/in/World'
# a=tilte.split('/',1)
# print(a[1])
# with open('test') as f:
#     for line in f:
#         print(line.rstrip())
#     # contens=f.read()
#     print(contens.rstrip())


# a=[1,2,3,4,5,6,7,8]
# # b=[i*i for i in a if i>5]
# # print(b)
# data=filter(lambda x:x if x>5 else None,a)
# # print(list(data))
# c=map(lambda x:x*x,data)
# print(list(c))

# print(type(range(100)))
#任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环
#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
# from collections import Iterable
# isinstance('abc', Iterable) # str是否可迭代
# isinstance([1,2,3], Iterable) # list是否可迭代
# isinstance(123, Iterable) # 整数是否可迭代
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象
#由于列表生成式受到内存限制,故列表的容量也是有限的,但生成器就不一样,生成器保存的是算法,
# 每次调用next(),就可以算出下一个值,直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
#当然，这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象,这样就不用StopIteration的错误.
#生成器generator
# g=(x for x in range(1,10001))#第一种方法
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for i in g:
#     print(i)

#第二种方法
# def gen(max):
#     n=0
#     while n<=max:
#         n+=1
#         yield n
# g=gen(10000)
# # for i in g:
# #     print(i)
# print(next(g))

# 小结:
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
# 首先获得Iterator对象:通过iter()函数把list变成一个iterator对象
# it = iter([1, 2, 3, 4, 5])
# print(type(it))
# 循环:
# while True:
#     try:
        # 获得下一个值:
# for x in it:
        # x = next(it)
    # print(x)
    # except StopIteration:
    #     # 遇到StopIteration就退出循环
    #     break

a=int()
print(type(a))
# print(a('8'))
