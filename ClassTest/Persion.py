class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return  self.name

    def get_age(self):
        return self.age

class Teacher(Person):
    def __init__(self,name,age,number):
        super(Teacher,self).__init__(name,age)
        self.number = number

    def get_number(self):
        return  self.number



