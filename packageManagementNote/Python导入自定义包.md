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