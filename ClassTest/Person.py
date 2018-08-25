# 创建父类，继承object
#__init__为构造函数
# __del__为析构函数
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_type(self):
        return '我是老师'

# 继承Person类
class Teacher(Person):
    def __init__(self, name, age, number):
        super(Teacher, self).__init__(name, age)
        self.number = number

    def get_number(self):
        return  self.number

    def get_type(self):
        return '我是学生'



