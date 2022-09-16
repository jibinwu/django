#filter 过滤
list_x=[1,3,0,5,0,9,0,1]
r=filter(lambda x:x if x>0 else None,list_x)
# print(r)
print(list(r))