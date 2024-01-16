<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [执行py文件与package属于同一层级](#%E6%89%A7%E8%A1%8Cpy%E6%96%87%E4%BB%B6%E4%B8%8Epackage%E5%B1%9E%E4%BA%8E%E5%90%8C%E4%B8%80%E5%B1%82%E7%BA%A7)
- [执行py文件与package不在一个层级中](#%E6%89%A7%E8%A1%8Cpy%E6%96%87%E4%BB%B6%E4%B8%8Epackage%E4%B8%8D%E5%9C%A8%E4%B8%80%E4%B8%AA%E5%B1%82%E7%BA%A7%E4%B8%AD)
- [直接进入Python安装路径直接创建pth文件，放置包路径](#%E7%9B%B4%E6%8E%A5%E8%BF%9B%E5%85%A5python%E5%AE%89%E8%A3%85%E8%B7%AF%E5%BE%84%E7%9B%B4%E6%8E%A5%E5%88%9B%E5%BB%BApth%E6%96%87%E4%BB%B6%E6%94%BE%E7%BD%AE%E5%8C%85%E8%B7%AF%E5%BE%84)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 执行py文件与package属于同一层级

1. 需要创建一个文件夹，而且需要包含有\__init__.py文件
2. 随后在包里面放置你所需要的文件类型
3. 在其他文件调用的时候统一是from xx import xx，或者是import xxx.xxx
4. 具体文件目录树形式如下所示
   1. ![image-20240110113042640](C:/Users/lucus/AppData/Roaming/Typora/typora-user-images/image-20240110113042640.png)

# 执行py文件与package不在一个层级中

1. 需要运用sys库，导入sys

2. 在执行py文件中加入一个sys.append(绝对路径代码)

   1. 具体代码如下所示

      1. ```python
         import sys
         sys.path.append(r"C:\Users\lucus\Desktop\typoraNote\packageManagementNote\Python导入自定义包\packageOne")
         from packageOne.functionOne import function_one
         function_one()
         ```

3. 具体目录如下所示

   1. ![image-20240110113358425](C:/Users/lucus/AppData/Roaming/Typora/typora-user-images/image-20240110113358425.png)

# 直接进入Python安装路径直接创建pth文件，放置包路径

1. 检索python可执行文件放置位置，具体代码如下所示

   1. ```
      import sys
      print(sys.executable)
      ```

2. 随后进入到python的安装文件路径夹里面，查看**python安装目录\Python35\Lib\site-packages**中创建一个文件为**module_packageOne.pth**的文件，而且module_（包名）最好一致，运用vim/gedit或者记事本打开文件，里面填写的是**包的绝对路径**即可

   1. 具体文件内容为

      1. > ```
         > C:\Users\lucus\Desktop\typoraNote\packageManagementNote\Python导入自定义包\packageOne
         > ```