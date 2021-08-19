    记录python基础学习笔记，路径：https://www.liaoxuefeng.com/wiki/1016959663602400
    
    1.python以缩进的形式表示代码块，缩进一般是4个空格
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
        常量：全部大写的变量名表示常量，其实也是变量，仅仅习惯写法而已
    3.编码问题
        ASCII编码是1个字节，Unicode编码是2个字节
        UTF-8是“可变长编码”，常用的英文字母被编码成1个字节，汉字通常是3个字节，很生僻的字符被编码为4~6个字节
        计算机内存中统一使用Unicode编码，当需要保存到硬盘或者传输时转换为UTF-8编码
    4.#!/usr/bin/env python 告诉Linux/OS X系统，调用python解释器执行代码，windows系统会忽略这个注释，./test.py这样调用时生效
      # -*- coding:utf-8 -*- 告诉python解释器按照utf-8读取源代码
    5.格式化输出%  format
        print('Age: %d. Gender: %s' % (25, True))      %d 整数  %f 浮点数    %s字符串
        print('{0} {1} {0}'.format('hello','world'))
    6.list和tuple
        list：有序集合
            append('a') 追加元素到末尾
            insert(i,'a') 插入元素到i索引位置
            pop() 删除末尾的元素 pop(i) 删除i索引位置的元素
        tuple：有序集合，但不能更改，因此他没有append、insert等此类方法
            t=(1,)  一个元素的tuple
            
        list和tuple均可以指定索引范围进行切片操作，L[0:3]，包前不包后
        以上是集合，集合当中的元素类型可以不一致，比如可以同时出现数字，string，list，tuple，dict等
    7.dict字典，key必须是不可变对象，dict是无序的
        'Thoms' in d 判断key是否存在  //返回False或True
        d.get('Thomas') 如果key不存在，返回None
        d.pop(key)删除一个key，dict当中对应的value也会被删除
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
        
        
        