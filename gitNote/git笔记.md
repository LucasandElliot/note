# Git指令集合
## 参考：https://blog.csdn.net/zhezhebie/article/details/78761417

## 设置github邮箱以及账号

1.  git config --globaluser.name"LucasandElliot"

2. git config --globaluser.email"xxxxxx@xx.com"

##  设置SSH key钥匙
检查是否已经生成密钥
1. cd ~/.ssh
如果返回了三个文件证明已经生成了密钥
如果没有密钥，即为输入以下命令
1. ssh-keygen -t rsa -C "xxxxxx@xx.com"
随后直接回车即可，即为默认路径以及默认没有密码登录
查看 SSH key的输出，复制输出到剪贴板，随后打开github的setting，检索是否有SSH，随后创建即可
1. cat ~/.ssh/id_rsa.pub
## 上传文件
进入对应文件夹，随后初始化git文件夹，执行对应指令，但需要先关联仓库地址(这里需要为Https形式文件/git后缀文件)
1. cd C:/Users/lucus/Desktop/Typora_note
2. git init
3. git remote add orgin git@github.com:LucasandElliot/note.git
4. git add .  /git add --all
5. git commit -m "提交文件，即为文件提交注释"
6. git push -u origin master(branch)
## 更新库的文件
如果已经存在readme文件，提交的时候可能会有冲突，因此需要有以下两种操作
- 舍弃线上文件，强制推送
	1. git push origin master -f
- 保留线上文件，用于合并远程仓库（通常是命名为 "origin"）的 "master" 分支拉取最新的更新到本地仓库。
	1. git pull origin master
	2. git push origin master
## 查询对应仓库路径
1. git remote -v
## 修改远程仓库地址
1. git remote set-url orgin <your_remote_url>
## 添加远程仓库
1. git remote add orgin 项目地址(url.git 或者是git.git)
## git查看回退历史记录
参考：https://blog.csdn.net/jacke121/article/details/54565222

命令具体如下所示

1. git log
2. git reset --hard commit_id

## git更新仓库并上传文件

1. git pull origin master
2. git push origin master
3. git add .  /git add --all
4. git commit -m "提交文件，即为文件提交注释"
5. git push -u origin master(branch)

## Git激活虚拟环境

主要要求你的venv的script文件夹需要有activate文件和activate.bat文件

具体命令如下所示。打开所需要激活的文件夹。如图所示。

`source activate conDigSum`

![image-20231128105540044](src/image-20231128105540044.png)
