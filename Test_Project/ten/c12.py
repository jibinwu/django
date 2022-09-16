import json
#json两种数据表
#现形式  object 和 array
s='{"name":"jibinwu","age":27}'# object
s='[{"name":"jibinwu","age":27},{"name":"kobi","age":38}]'# 数组
student=json.loads(s)#将JSON字符串转换成Python的数据结构
print(student)
print(student[0])
print(type(student))


# teacher=[
#             {'name':'qiyue','age':18,'flag':False,'school':None},
#             {'name':'bayue','age':'19'}
#         ]
# json_str=json.dumps(teacher)
# print(type(json_str))
# print(json_str)
