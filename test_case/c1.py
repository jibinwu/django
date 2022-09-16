# class Student(object):
#     def __init__(self,name,score):
#         self.__name=name
#         self.__score=score
#     def print_score(self):
#         print('%s:%s'%(self.__name,self.__score))
#     def get_name(self):
#         return self.__name
# a=Student('jbw',100)
# print(a.get_name())
# print(isinstance((1,2,3),(list or tuple)))


# class Student(object):
#     name='kobe'
#     def __init__(self,name):
#         self.name=name
#         # pass
# s=Student('jbw')
# print(s.name)
# s.name='zjj'
# print(s.name)
# print(s.__dict__)


# class Student(object):
#     count=0
#     def __init__(self):
#         self.__class__.count +=1
#         print(Student.count)
#         pass
# s=Student()
# # print(Student.count)
# s1=Student()
# s2=Student()
# s3=Student()
# s4=Student()
# s5=Student()

class Student(object):

    # __slots__ = ('name','age')
    name='zjj'
    age=28
    sex='女'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):

        return self.name

s=Student('jbw',23)
# b=s.get_name()
# print(b)
print(s.get_name())
# s.sex='男'
# print(s.sex)
# print(s.sex)



