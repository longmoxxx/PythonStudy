from ClassTest.Person import Teacher

if __name__=="__main__":
    teacher = Teacher("majian",23,'13520192432')
    print(teacher.get_name())
    print(teacher.get_age())
    print(teacher.get_number())
    print(teacher.get_type())