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
