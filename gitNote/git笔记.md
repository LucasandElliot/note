<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [参考](#%E5%8F%82%E8%80%83)
- [设置github邮箱以及账号](#%E8%AE%BE%E7%BD%AEgithub%E9%82%AE%E7%AE%B1%E4%BB%A5%E5%8F%8A%E8%B4%A6%E5%8F%B7)
- [设置SSH key钥匙](#%E8%AE%BE%E7%BD%AEssh-key%E9%92%A5%E5%8C%99)
- [上传文件](#%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6)
- [更新库的文件](#%E6%9B%B4%E6%96%B0%E5%BA%93%E7%9A%84%E6%96%87%E4%BB%B6)
- [查询对应仓库路径](#%E6%9F%A5%E8%AF%A2%E5%AF%B9%E5%BA%94%E4%BB%93%E5%BA%93%E8%B7%AF%E5%BE%84)
- [修改远程仓库地址](#%E4%BF%AE%E6%94%B9%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93%E5%9C%B0%E5%9D%80)
- [添加远程仓库](#%E6%B7%BB%E5%8A%A0%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93)
- [删除远程仓库地址](#%E5%88%A0%E9%99%A4%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93%E5%9C%B0%E5%9D%80)
- [git查看回退历史记录](#git%E6%9F%A5%E7%9C%8B%E5%9B%9E%E9%80%80%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95)
- [git更新仓库并上传文件](#git%E6%9B%B4%E6%96%B0%E4%BB%93%E5%BA%93%E5%B9%B6%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6)
- [Git激活虚拟环境](#git%E6%BF%80%E6%B4%BB%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)
- [移除文件缓存](#%E7%A7%BB%E9%99%A4%E6%96%87%E4%BB%B6%E7%BC%93%E5%AD%98)
- [移除文件夹缓存](#%E7%A7%BB%E9%99%A4%E6%96%87%E4%BB%B6%E5%A4%B9%E7%BC%93%E5%AD%98)
- [上传大文件](#%E4%B8%8A%E4%BC%A0%E5%A4%A7%E6%96%87%E4%BB%B6)
- [合并分支](#%E5%90%88%E5%B9%B6%E5%88%86%E6%94%AF)
- [删除本地master分支](#%E5%88%A0%E9%99%A4%E6%9C%AC%E5%9C%B0master%E5%88%86%E6%94%AF)
- [删除git的commit记录](#%E5%88%A0%E9%99%A4git%E7%9A%84commit%E8%AE%B0%E5%BD%95)
- [撤回没有被上传的commit指令](#%E6%92%A4%E5%9B%9E%E6%B2%A1%E6%9C%89%E8%A2%AB%E4%B8%8A%E4%BC%A0%E7%9A%84commit%E6%8C%87%E4%BB%A4)
- [Git 合并分支](#git-%E5%90%88%E5%B9%B6%E5%88%86%E6%94%AF)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

[toc]

# 参考

- https://blog.csdn.net/zhezhebie/article/details/78761417

# 设置github邮箱以及账号

1.  git config --globaluser.name"LucasandElliot"

2. git config --globaluser.email"xxxxxx@xx.com"

#  设置SSH key钥匙
检查是否已经生成密钥
1. cd ~/.ssh
如果返回了三个文件证明已经生成了密钥
如果没有密钥，即为输入以下命令
1. ssh-keygen -t rsa -C "xxxxxx@xx.com"
随后直接回车即可，即为默认路径以及默认没有密码登录
查看 SSH key的输出，复制输出到剪贴板，随后打开github的setting，检索是否有SSH，随后创建即可
1. cat ~/.ssh/id_rsa.pub
# 上传文件
进入对应文件夹，随后初始化git文件夹，执行对应指令，但需要先关联仓库地址(这里需要为Https形式文件/git后缀文件)
1. cd C:/Users/lucus/Desktop/Typora_note
2. git init
3. git remote add orgin git@github.com:LucasandElliot/note.git
4. git add .  /git add --all
5. git commit -m "提交文件，即为文件提交注释"
6. git push -u origin master(branch)

# 更新库的文件

如果已经存在readme文件，提交的时候可能会有冲突，因此需要有以下两种操作
- 舍弃线上文件，强制推送
	1. git push origin master -f
- 保留线上文件，用于合并远程仓库（通常是命名为 "origin"）的 "master" 分支拉取最新的更新到本地仓库。
	1. git pull origin master
	2. git push origin master
# 查询对应仓库路径
1. git remote -v
# 修改远程仓库地址
1. git remote set-url origin <your_remote_url>

# 添加远程仓库

1. git remote add origin 项目地址(url.git 或者是git.git)如【 git@github.com:LucasandElliot/note.git】

# 删除远程仓库地址

- ```
  git remote remove orgin（需要删除的代名词或分支）
  ```

# git查看回退历史记录

参考：https://blog.csdn.net/jacke121/article/details/54565222

命令具体如下所示

1. git log
2. git reset --hard commit_id

# git更新仓库并上传文件

1. git pull origin master
2. git push origin master
3. git add .  /git add --all
4. git commit -m "提交文件，即为文件提交注释"
5. git push -u origin master(branch)

# Git激活虚拟环境

主要要求你的venv的script文件夹需要有activate文件和activate.bat文件

具体命令如下所示。打开所需要激活的文件夹。如图所示。

`source activate conDigSum`

![image-20231128105540044](src/image-20231128105540044.png)

# 移除文件缓存

```
git rm --cached your_path_file
```

# 移除文件夹缓存

```
git rm --cached -r path_of_the_dir
```

# 上传大文件

1. 安装lfs

   ```
   git lfs install
   ```

2. 设置需要上传的大文件后缀

   ```
   git lfs track "*.dll" 
   ```

3. 确定初始化

   ```
    git add .gitattributes
   ```

4. 随后正常push和pull即可

# 合并分支

1. 切换到main分支

   ```
   git checkout main
   ```

2. 将main分支代码pull拖拉下来

   ```
   git pull orgin main

3. 合并master分支

   ```
   git merge master
   ```

4. 查看状态以及执行提交指令

   ```
   git status
   ```

5. push代码进入到指令中

   ```
   git push origin main
   ```

# 删除本地master分支

```
git branch -d master
```

# 删除git的commit记录

1. 查看记录

   ```
   git log
   ```

2. 设置改写从xx记录之后所有记录的权限

   ```
   git rebase -i 
   ```

3. 运用vim打开commit log list，随后将pick改为drop即可，保存文件。随后再次推送

# 撤回没有被上传的commit指令

```
git reset  HEAD^
```

- --mixed， 不改动工作空间代码，但是撤销commit，以及git add 操作，一般为默认操作
- --soft， 不删除工作空间以及代码，撤销commit。不撤销git add .
- --hard，删除工作空间改动diam，撤销commit， 撤销git add . 这个执行之后，就恢复到了上次commit的状态
- HEAD^是回退到上一次，HEAD~2是回退上两次（而且是会根据执行之后再次回退，即为先执行HEAD^，后执行HEAD~2一共会回退3次）

# Git 合并分支

- 具体常见如下，假设有master和change分支，从同一个节点分裂，随后各自进行了两次提交commit以及修改。随后即为change想合并到master分支中，但是直接git commit和git push是不成功的，因为分支冲突了【master以及修改】
  - 原来开始master和change图示【相同颜色为同一分支内容】
    - ![image-20240122230337824](src/image-20240122230337824.png)

- git merge操作【历史记录较多】

  - git merge实际上为即为先让git按照master和change分支提交顺序排列，分别到达各自顶端，随后执行merge commit具体如下图所示，git log命令查看的时候会存在多个提交记录，而且最终合并到feature分支中

  - 代码

    - ```
      git checkout change
      git pull origin master # 等于 git fetch origin master + git merge master change
      ```

  - 具体如下图所示

    - ![image-20240122230321936](src/image-20240122230321936.png)

- git rebase操作【历史记录较少】

  - git rebase实际上先移动到master顶端，即为更新所有change分支内的master分支内容，即为先更新master分支内容，随后对change分支直接移动到master分支顶端，在执行change分支内容，因此，最终合并记录较少

    - 具体如下图所示

      - ![image-20240122230224061](src/image-20240122230224061.png)

    - 代码

      - ```
        git checkout feature
        git pull --rebase origin master # 等于git fetch origin master + git rebase master
        ```

