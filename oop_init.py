# coding=utf8
'''
__init__ 方法会在类的对象被实例化（ Instantiated） 时立即运行。这一方法可以对任何你想
进行操作的目标对象进行初始化（ Initialization） 操作。这里你要注意在 init 前后加上的双下
划线。
'''


class Person:
    def __init__(self, name):  # 因为点号 self.name 意味着这个叫作“name”的东西是某个叫作“self”的对象的一部分，
        self.name = name   # 而另一个 name 则是一个局部变量

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('douxiao')
p.say_hi()
