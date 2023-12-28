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

