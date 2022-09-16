#map函数
def add(x,y):
    return x+y

r=map(add,[1,2,3,4],[2,3,4,5])
# print(r)#返回一个人map对象
# print(list(r))
print(tuple(r))


#用匿名函数实现
# r=map(lambda x,y:x+y,[1,2,3,4],[2,3,4,5])
# print(list(r))

#reduce函数
def add(x,y):
    return x+y
r=reduce(add,[1,2,3,4,5])
print(list(r))

#upper()转换成大写,lower()转换成小写
# a=[]
# s=['aAb','AdQ','mAB']
# for i in s:
#     a.append(i[0].upper()+i[1:].lower())
# print(a)

