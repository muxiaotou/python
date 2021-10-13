    记录python基础学习笔记，路径：https://www.liaoxuefeng.com/wiki/1016959663602400
    学习文档：https://mp.weixin.qq.com/s/gtdG6A1lxz_W9QbrRY6zew
    
    dir()返回当前范围内的变量、方法和定义类型列表   
    dir(obj)返回对象的属性列表
    help()返回python的帮助信息文档
    help(obj)返回对象的help信息文档
    
    1.面向对象：每个变量都是一个类，都有自己的属性及其方法
        python以缩进的形式表示代码块，缩进一般是4个空格
        注释：行内用#，行间注释用两组'''
    2.数据类型
        整数：包括正负整数
        浮点数：即小数
        字符串：单引号或双引号括起来的任意文本
            \ 转义字符，\n 换行，\t 制表符，\\ 字符\
            r('\\t\\') r表示''内的字符串默认不转义
            '''...''' 表示多行内容，内容是可以多行的
            加号(+) 用于字符串连接运算，星号(*)用于字符串重复
        布尔值：True False，注意大小写
        None：特殊的空值，不是0
        变量：字母、数字、下划线的组合，且不能以数字开头
            a = 123， a = 'a'，类型不固定的动态语言，同一变量可以反复赋值，而且可以是不同类型的变量
            不需要预先声明变量类型，变量的类型和值在赋值那一刻被初始化
            变量名区分大小写，大小写被认为是两个不同的字符
        常量：全部大写的变量名表示常量，其实也是变量，仅仅习惯写法而已
        
        Python有6个标准的数据类型：
        1）不可变类型：number、string、tuple
        2）可变类型：list、dictionary、set
    3.编码问题
        ASCII编码是1个字节，Unicode编码是2个字节
        UTF-8是“可变长编码”，常用的英文字母被编码成1个字节，汉字通常是3个字节，很生僻的字符被编码为4~6个字节
        计算机内存中统一使用Unicode编码，当需要保存到硬盘或者传输时转换为UTF-8编码
    4.#!/usr/bin/env python 告诉Linux/OS X系统，调用python解释器执行代码，windows系统会忽略这个注释，./test.py这样调用时生效
      # -*- coding:utf-8 -*- 告诉python解释器按照utf-8读取源代码
    5.格式化输出%  format
        print('Age: %d. Gender: %s' % (25, True))      %d 整数  %f 浮点数    %s字符串
        print('{0} {1} {0}'.format('hello','world'))
        print默认换行，需要不换行时，print(x, end=' ')
    6.list和tuple
        list：有序集合，列表可变，数据项的类型可以不同
        列表创建：list1 = ['baidu', 'google', 12, 34]
            list.append('a') 追加元素到末尾
            list.insert(i,'a') 插入元素到i索引位置
            list.pop() 删除末尾的元素 pop(i) 删除i索引位置的元素
        tuple：有序集合，但不能更改，因此他没有append、insert等此类方法
        元祖创建：tup1 = ('baidu', 'google', 12, 34)
            t=(1,)  一个元素的tuple
            
        list和tuple均可以指定索引范围进行切片操作，L[0:3]，包前不包后
        以上是集合，集合当中的元素类型可以不一致，比如可以同时出现数字，string，list，tuple，dict等
    7.dict字典，key必须是不可变对象，数字、字符串、元祖均可，但必须不可变，值也可以是任何类型对象，dict是无序的
        字典创建 dictionary  = {'url1':'baidu', 'url':'google', 'num1':12, 'num2':34};
        'Thoms' in d 判断key是否存在  //返回False或True
        d.get('Thomas') 如果key不存在，返回None，d.get('Thomas',default) 如何key不存在，返回default
        d.pop(key)删除一个key，dict当中对应的value也会被删除

      set集合，是由不重复元素组成的无序的集
        集合创建set1 = {'hello', 'hello', 'word', 'word'}，自动会去重，set1结果是{'hello', 'word'},或者set(iterable)来创建
        创建空集合必须是set(),创建空dict是{}
        集合也有推导式，类似列表生成式和迭代器一样，a = {x for x in 'abracadabra' if x not in 'abc'}
    8.函数
        1.函数名本质是指向一个函数对象的引用，可以把函数名赋给一个变量，相当于给这个函数起了一个别名
            a = abs #变量指向abs函数
            a(-1)
        2.
        def my_abs(x):
            if x >= 0:
                return x
            else:
                return -x
        return 时函数执行完毕返回，如果没有return语句，函数执行完成后也会返回结果，结果是None，return Node简写为return
        return也可以返回多个值，本质返回的是一个tuple
        3.pass    可以在函数当中用来作为占位符
        4.默认参数
            def power(x, n=2):
                pass
            必选参数在前，默认参数在后；
        5.可变参数&关键字参数(可以是0个)
            def person(name, *args, **kw):
                pass
                
            ages = [30, 20, 15]
            extra = {'city': 'Beijing', 'job': 'Engineer'}
            person('Jack', *ages, **extra)
            
            *age list或tuple
            **kw dict
    9.迭代
        一个对象同时具有__iter__()和__next__()这两个方法，那这个对象就是一个迭代器，有__iter__()，这个对象就是可迭代的
        list、tuple、string均可以使用for i in ... 来进行迭代
        dict也是可以迭代的：
            for key in d:  迭代dict的key
            for value in d.values()： 迭代dict的value
            for k, v in d.itmes()：  迭代dict的key，value
        
        可以直接作用于for循环的数据类型有以下几种：
            一类是集合数据类型，如list、tuple、dict、set、str等；
            一类是generator，包括生成器和带yield的generator function。
            这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
        迭代器：
            概念没怎么理解，与生成器对比着看------TODO
    10.列表生成式[]，一次性生成所有列表元素，如果元素较多，会占用大量内存空间
        [x * x for x in range(1, 11)]  生成[1,4,9,.....100]
        列表生成式里面可以继续嵌套if、for语句，if用来筛选，因此不能在列表生成式当中带else
        [x for x in range(1, 11) if x % 2 == 0 else 0] 报错，不能带else，因为if在for之后，是一个筛选条件，带了else就无法筛选了
        [x if x % 2 == 0 else -x for x in range(1, 11)] 正确，必须带else，因为if在for之前，是表达式，根据if或else计算出确定的结果
    11.生成器generator ()或者yield，仅仅用到某个元素才更加某种特定算法推算出来
        1）把list的[]改成()
        >>> L = [x * x for x in range(10)]
        >>> L
        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        >>> g = (x * x for x in range(10))
        >>> g
        <generator object <genexpr> at 0x1022ef630>
        以上L是一个list，而g是一个generator：
            1) 使用next(g)可以依次打印出g当中的所有元素，直到最后抛出StopIteration的错误，因此永远不要使用next了
            2）使用for n in g来循环迭代
        2）def当中使用yield 
        含有yield的函数，也是generator，普通函数遇到return或者函数最后一行即返回函数，而generator函数每次使用next()调用或者再for循环当中，每次遇到yield即
        返回，下次从上次yield返回的地方开始继续执行
        def fib(max):
            n, a, b = 0, 0, 1
            while n < max:
                yield b
                a, b = b, a + b
                n = n + 1
            return 'done'
        上面generator当中，yield b，b为每次generator的返回值，
    12.交叉赋值
        a , b = b , a
    13.函数式编程
        默认值参数(=，调用函数时未提供则使用默认值)，关键字参数(*args代表传入的是一个list或者tuple,**args代表传入的是一个dict)，形参
        函数可以当做变量来进行使用，例如：high_func是一个高阶函数，因为参数f是一个函数变量
        def high_func(f, arr):
            return [f(x) for x in arr]
    14.模块和包
        模块：其实就是一些py文件，里面定义了一些函数、类、变量等，用来封装一组功能
        包：多个模块形成的文件夹，里面包含多个py文件，也可以嵌套文件夹，将一类模块归集在一起
        import pandas
        import pandas as pd
        import module1[, module2[,... moduleN]]
        from pandas import Dataframe

        ***包路径下必须存在 __init__.py 文件
    15.流程控制
        python无Switch case的流程控制语句
        if...else...
        if...elif...[else]...

        for 变量名 in 序列    ， 序列主要指列表，元组，字符串，文件

        while  True: ...

        range(start， end， scan)  创建一个数字列表

        break 退出循环， continue 退出本次循环，继续下一次循环， pass 空语句， return 返回调用函数
        ***python中，在进行对象真值判断是，None，False,0,'',[],{},()都可以视为假
    16.序列
        python序列包括字符串、列表、元组、集合和字典
        序列一般都有索引、切片、相加、相乘、检查元素是否包含在元素中
        集合和字典不支持索引、切片、相加和相乘操作
        列表，元祖，字符串支持直接相加操作，也支持与数字相乘，支持相加是因为对象实现了__add__魔法方法，可以通过dict(obj)方法来查询对象的所有方法
    17.类与对象  方法：实例方法、类方法、静态方法
        class Car(object):
            #类变量
            name = "BWM"

            # 构造函数，在生成对象时调用
            def __init__(self, name):
                self.name = name

            # 实例方法（可调类变量、可调实例变量、可被实例调用）
            # 第一个参数强制为实例对象 self。
            # 当self.name没有被重新赋值前，也可以用self.name调用类变量name，但本质上name已经变成了实例变量
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
    18.异常处理
        class BException(Exception):  #定义一个异常，继承Exception基类
            pass   #也可以添加构造函数__init__
        raise AExpection() 抛出一个异常
        try...except...[except...] [else...] [finally...]
        先执行try内语句，当有异常发生进入对应的except，如果没有异常发生，执行else，无论有无异常，均执行finally
    19.装饰器
        即装饰函数，返回值是一个函数的函数
        装饰器有且只能有一个参数，即要被装饰的函数
    20.作用域
        x = 1

        def func():
            x = 2

        func()
        print(x)
        输出：1
        内部函数有引用外部函数的同名变量或者全局变量，并且对这个变量有修改的时候，此时 Python 会认为它是一个局部变量，因此内部函数的修改不会体现到外部同名的变量
        x = 5
        def func()
            x = x + 1
        func()
        内部函数有引用外部函数的同名变量或者全局变量，并且对这个变量有修改的时候，此时 Python 会认为它是一个局部变量,而内部函数中并没有 x 的定义和赋值，所以报错。
        
        以上，可以在x前面加上global，明确此变量是外部函数的变量或者全局变量
    21.python 值传递？引用传递？ https://mp.weixin.qq.com/s/XJ1nzEKEtNf0bMmy6X5CaA 
        Python 的参数传递是赋值传递 （pass by assignment），或者叫作对象的引用传递（pass by object reference）。
        Python 里所有的数据类型都是对象，所以参数传递时，只是让新变量与原变量指向相同的对象而已，并不存在值传递或是引用传递一说
        这里的赋值或对象的引用传递，不是指向一个具体的内存地址，而是指向一个具体的对象。

        如果对象是可变的，当其改变时，所有指向这个对象的变量都会改变。
        如果对象不可变，简单的赋值只能改变其中一个变量的值，其余变量则不受影响。
        清楚了这一点，如果你想通过一个函数来改变某个变量的值，通常有两种方法。
        一种是直接将可变数据类型（比如列表，字典，集合）当作参数传入，直接在其上修改；
        第二种则是创建一个新变量，来保存修改后的值，然后将其返回给原变量。在实际工作中，我们更倾向于使用后者，因为其表达清晰明了，不易出错。
    22.Python中list的append, extend, +=, +区别  http://noahsnail.com/2020/06/17/2020-06-17-python%E4%B8%ADlist%E7%9A%84append,%20extend%E5%8C%BA%E5%88%AB/
        list.append(x) append方法会将x作为list的一项添加到末尾。等价于a[len(a):] = [x]。
        list.extend(iterable) extend方法会将后面的可迭代对象的所有项添加到列表中。
        extend效果与+=是等价的，主要差异在于字节码执行的方式不同，extend方法涉及了函数调用，开销更大一些。extend比+=应用范围更广，某些情况下只能使用extend。
        +=会将后面的数据添加到原有的列表中，而+会返回一个新的列表，不改变原有列表。+只能连接列表。
        append方式会将参数作为列表的一项添加到原有的列表中。


        
    
    
    一些包
    1.print
        python 2: print >>sys.stderr, "This is a error"
        python 3: print("This is a error", file=sys.stderr)
    2.getopt.getopt(args, shortopts, longopts=[]) c风格的命令参数解释器
        1）短命令后有":"表示带参数，长命令后有"="表示带参数
        2）getopt函数返回两个list，opts和args，opts为分析出的格式信息，args为不属于格式信息的剩余的命令行参数，opts是一个两元组的列表。每个元素为：(选项串,附加参数)。如果没有附加参数则为空串
        #!/usr/bin/env python
        
        import getopt,sys
        
        try:
            opts, args = getopt.getopt(sys.argv[1:],'ho:',["help", "output="])
            print opts
            print args
        except getopt.GetoptError:
            print "An error has occurred"
            sys.exit(1)
            
        python chenli.py -h -o file --help --output=out file1 file2
        [('-h', ''), ('-o', 'file'), ('--help', ''), ('--output', 'out')]
        ['file1', 'file2']
        
        
        