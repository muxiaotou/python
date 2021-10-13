#!/usr/bin/env python

class Car(object):
    name = "BWM"

    # 构造函数，在生成对象时调用
    def __init__(self, name):
        self.name = name

    # 实例方法（可调类变量、可调实例变量、可被实例调用）
    # 第一个参数强制为实例对象 self。
    #  当self.name没有被重新赋值前，也可以用self.name调用类变量name，但本质上name已经变成了实例变量
    def run(self, speed):
        print(self.name, Car.name, speed, '行驶')

    # 类方法（可调类变量、可被实例调用、可被类调用）
    # 1、类方法通过@classmethod装饰器实现，只能访问类变量，不能访问实例变量；
    # 2、通过cls参数传递当前类对象，不需要实例化。
    @classmethod
    def run1(cls, speed):
        print(cls.name, speed)

    # 静态方法（可调类变量、可被实例调用、可被类调用）
    # 1、用 @ staticmethod装饰的不带self参数的方法；
    # 2、静态方法名义上归类管理，实际中在静态方法中无法访问类和实例中的任何属性；
    # 3、调用时并不需要传递类或实例。
    @staticmethod
    def run2(speed):
        print(Car.name,speed)


c = Car("宝马")
c.run("100迈")
# 宝马 100迈 行驶

c1 = Car("保时捷")
c1.run1("200迈")
Car.run1("300迈")
# BWM 200迈
# BWM 300迈

c2 = Car("法拉利")
c2.run2("400迈")
Car.run2("500迈")
# BWM 400迈
# BWM 500迈
