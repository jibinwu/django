# print('a','b','c')
# def demo(*param):
#     print(param)
#     print(type(param))
# demo((1,2,3,4,5))
# def demo(param1,*param,param2=2):
#     print(param1)
#     print(param)
#     print(param2)
#
# demo('a',1,2,3,param2='param')

# def demo(*param):
#     print(param)
#     print(type(param))
# # demo([1,2,3])
# demo(*[1,2,3])
def city_temp(**param):
    print(param)
    # print(param1,param)
    # print(param)
    # print(type(param))
    for key,value in  param.items():
        print(key +':'+value)
        # print(type(i))
# city_temp(bj='32c',xm='23c',sh='31c')
# city_temp(1,2)
a={'bj':'32c','sh':'31c'}
city_temp(**a)