<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [粘贴](#%E7%B2%98%E8%B4%B4)
- [复制](#%E5%A4%8D%E5%88%B6)
- [退出](#%E9%80%80%E5%87%BA)
- [帮助](#%E5%B8%AE%E5%8A%A9)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

[toc]

# 粘贴

- 打开vim，随后进入光标结束后的位置，输入p进行粘贴

# 复制

- 将光标移动到所需要复制的文本开始位置，v进行可视模式
- 将光标移动在所需要赋值的文本结束位置，输入y（默认为自动复制，而且会退出可视模式）
- 移动光标到文本结束的位置，输入p粘贴

# 退出

- ``:q``，为退出
- ``:q!``，为不保存退出
- ``:wq``，写入文件并退出
- ``:wq!``，如果文件有只读权限，写入退出，如果没有写权限，强制写入
- ``:x``，类似于`:wq`，如果没有变动，就不写入
- `:qa`，退出全部
- `ZZ`，大写ZZ，如果文件有变动，写入/保存，然后退出
- `ZQ`，如果不想保存文件，使用命令退出

# 帮助

- 进入vim的时候，可以输入help，随后查看对应帮助信息