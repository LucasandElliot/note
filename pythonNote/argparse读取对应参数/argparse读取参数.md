<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [用法](#%E7%94%A8%E6%B3%95)
- [argparseExample.py简单示例](#argparseexamplepy%E7%AE%80%E5%8D%95%E7%A4%BA%E4%BE%8B)
- [参考](#%E5%8F%82%E8%80%83)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 用法

- argparse是内置于python中，所以即为直接在命令行中对程序传入参数并让程序运行的便捷工具。
- 具体步骤如下所示
  1. 导包，为`import argparse`
  2. 创建一个ArugmentParser对象，随后一切都在这个对象里面操作，为`parser = argparse.ArgumentParser()`
  3. 加入一些参数，具体方法为`parser.add_argument()`
  4. 解析参数，为`args = parser.parse_args()`
- -h，帮助操作，一般用显示帮助信息，如在加入参数的时候一些定义以及显示
- 传入参数方法，为`parser.add_argument('--integers', type=str, help='传入的数字', default='1', required=True, nargs='+')`
  1. --integers， 分为可选参数--和普通参数，可选参数的意义在于保持了代码的逻辑性，可以自定义输入参数顺序，而且在调用的时候只需要args.integers即可【以上述代码为例，省略--即为实际参数】
  2. type，指定参数类型，可以为int，str，float，list，dict等类型
  3. help，为在输入-h参数的时候，显示的信息，一般用于说明介绍参数
  4. default，即为设置默认参数，一般与type类型一直
  5. required为必须参数，required=True即为输入进入命令行的时候必须带入该参数
  6. nargs为设置该参数下的个数，如果为2-n个参数，需要设置如下操作
     1. '\*'为接受0-n个参数
     2. '?'为参数可以设置0-1个
     3. "+"可以设置为1-n个
     4. 【具体跟正则表达式匹配类似】

# argparseExample.py简单示例

- ```
  #!/usr/bin/env python
  # -- coding: utf-8 --
  # @Time : 2024/1/13 16:08
  # @Author : Lucas
  # @File : argparseExample.py
  import argparse
  parser = argparse.ArgumentParser(description='命令行输入参数随后遍历出来')
  #type是要传入的参数的数据类型  help是该参数的提示信息
  parser.add_argument('--parameterOne', type=int, nargs='+', help='参数1', default=1)
  parser.add_argument('--parameterTwo', type=int, nargs='+', help='参数2', default=2)
  parser.add_argument('--parameterThree', type=int, nargs='?', help='参数2', default=3, required=True)
  args = parser.parse_args()
  # 获得传入的参数
  print(args)
  # 计算结果
  print(args.parameterThree + args.parameterTwo + args.parameterOne)
  ```

- 在命令行中输入`python argparseExample.py --parameterThree 1`即可

# 参考

- [python中parse的用法](https://blog.csdn.net/qq_35498453/article/details/108757215)

- [argparse模块用法实例详解](https://zhuanlan.zhihu.com/p/56922793)