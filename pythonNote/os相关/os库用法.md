<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [判断文件路径是否存在](#%E5%88%A4%E6%96%AD%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8)
- [创建一个文件路径](#%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84)
- [删除文件/目录](#%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6%E7%9B%AE%E5%BD%95)
- [复制文件/文件目录](#%E5%A4%8D%E5%88%B6%E6%96%87%E4%BB%B6%E6%96%87%E4%BB%B6%E7%9B%AE%E5%BD%95)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 判断文件路径是否存在

```
import os
import sys
log_path = '../exp/log'
if os.path.exists(log_path):
	print("文件存在")
# 因为如果存在os.path.exists()返回真
```

# 创建一个文件路径

```
import os
os.mkdir() # 创建单级目录
os.makedirs() # 创建多级别目录
```

# 删除文件/目录

```
import os
import shutil
os.remove()
os.rmdir(“dir”) # 只能删除空目录
shutil.rmtree(“dir”) # 空目录、有内容的目录都可以删
```

# 复制文件/文件目录

```
import os
import shutil
shutil.copyfile(“old_file”,”new_file”) # old_file和new_file都只能是文件
shutil.copy(“old_file”,”new_file”) # old_file只为文件夹，new_file可以是文件，也可以是目标目录
shutil.copytree(“old_dir”,”new_dir”) # old_dir和new_dir都为目录，且newdir必须不存在
```

