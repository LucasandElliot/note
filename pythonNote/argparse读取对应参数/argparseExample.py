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
# 默认为真，即为最后namespace最终出现为args.flag变量，而且默认如果出现为赋值为假，默认为真
parser.add_argument('--is_flag', dest='flag', action='store_false', default=True)
args = parser.parse_args()
# 获得传入的参数
print(args)
# 计算结果
print(args.parameterThree + args.parameterTwo + args.parameterOne)