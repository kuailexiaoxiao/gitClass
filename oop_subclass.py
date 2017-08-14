# coding=UTF8
class SchoolMember:
    def __init__(self, name, age):  # 代表任何学校里的成员
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")  # 告诉有关我的细节


class Teacher(SchoolMember):  # 代表一位老师
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):  # 代表一位学生
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Mark: "{}"'.format(self.mark))


t = Teacher('Mrs.dou', 24, 888888)
s = Student('dou.x', 19, 90)

print()

members = [t, s]

for member in members:
    member.tell()

