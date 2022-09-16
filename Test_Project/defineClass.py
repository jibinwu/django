#类名最好大写
#类最基本的作用:封装(比如属性和方法,方便其他模块调用,一般不会再封装中实例化)
#类相当于一个模板,可以创造出很多对象
class Student(object):
    sum=0
    name='qiyue'
    age=0
    #'类变量' ,'实例变量'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('yes')
        self.learn()
        # print(age)
        # print(name)
    #构造函数

    #特征与行为
    def do_honework(self):#行为与主体相对应,什么样的主体具备相应的行为.比如:学生可以有做作业这个行为,而不具备打印功能
        print('homework')

    def learn(self):
        print('我爱学习')
        self.do_honework()
class Printer(object):
    def test_file(self):
        print('name:',self.name) #调用类中的变量,需加上self.变量调用
        print('age:',self.age)

student=Student('jbw',27) #类的实例化
# student.__init__('jbw','28')
# print(student.name)#实例对象能调用类的的变量和方法,但要记住类方法中的局部变量赋的值不会改变类的全局变量,就像例子中返回为空一个道理,而不是jbw
# student.test_file()#类的调用

