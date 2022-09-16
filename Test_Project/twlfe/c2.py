#map
list_x=[1,2,3,4,5,6,7]
list_y=[]
def square(x):
    return x**2

# for i in list_x:
#     square(i)
#     list_y.append(square(i))
# print(list_y)


#用map来实现
r=map(square,list_x)
# print(r)
# print(list(r))
# print(tuple(r))

print(set(r))
