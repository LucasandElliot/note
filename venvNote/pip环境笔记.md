<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [更换清华镜像源](#%E6%9B%B4%E6%8D%A2%E6%B8%85%E5%8D%8E%E9%95%9C%E5%83%8F%E6%BA%90)
- [查看包安装](#%E6%9F%A5%E7%9C%8B%E5%8C%85%E5%AE%89%E8%A3%85)
- [导出pip虚拟环境](#%E5%AF%BC%E5%87%BApip%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)
- [pip更换镜像源](#pip%E6%9B%B4%E6%8D%A2%E9%95%9C%E5%83%8F%E6%BA%90)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 更换清华镜像源

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```

```
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip config set install.trusted-host mirrors.aliyun.com
```



# 查看包安装

```
pip show packageName
```

# 导出pip虚拟环境

```
pip freeze > requirements.txt
```

- 运用上述命令会发生@file等问题，因此我们采用下述方案

```
pip list --format=freeze > requirements.txt
```



# pip更换镜像源

具体也可以为直接找到.condarc文件，具体文件路径为分win和linux

- win下换源

  1. 在文件资源管理系统输入%APPDATA%

  2. 随后创建如下代码

     - ```
       [global]
       index-url = https://pypi.douban.com/simple
       ```

- linux下换源

  1. 输入以下命令

     - ```
       cd ~
       mkdir -p .pip
       vi pip.conf
       ```

  2. 输入内容与win上述一致，为如上所示

     - ```
       [global]
       index-url = https://pypi.douban.com/simple
       ```
