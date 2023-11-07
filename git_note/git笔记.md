# Git指令集合

## 设置github邮箱以及账号

1.  git config --globaluser.name"LucasandElliot"

2. git config --globaluser.email"1530575924@qq.com"

##  设置SSH key钥匙
检查是否已经生成密钥
1. cd ~/.ssh
如果返回了三个文件证明已经生成了密钥
如果没有密钥，即为输入以下命令
1. ssh-keygen -t rsa -C"1530575924@qq.com"
随后直接回车即可，即为默认路径以及默认没有密码登录
查看 SSH key的输出，复制输出到剪贴板，随后打开github的setting，检索是否有SSH，随后创建即可
1. cat ~/.ssh/id_rsa.pub
## 上传文件
进入对应文件夹，随后初始化git文件夹，执行对应指令
1. cd C:/Users/lucus/Desktop/Typora_note
2. git init
3. git add .
4. git commit -m "提交文件，即为文件注释系统"


   

