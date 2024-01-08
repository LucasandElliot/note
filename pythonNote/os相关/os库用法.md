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

