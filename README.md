# 介绍
1. 主要用于存放个人在自然语言处理或者其他课程内容授课内容，后续也会持续不断更新
1. 主要是用于仅供学习所用，如果需要有其他错误可以指出并在issue说明
1. 如果有其他问题请私信 lucasaeliott@gmail.com
1. 自动生成md文档的outline脚本步骤如下
   1. 运用npm下载doctoc，即为在admins权限下安装`npm install -g doctoc`
      1. 下载npm的方法如[npm下载和使用（超详细）](https://blog.csdn.net/chen_junfeng/article/details/110422090)下载博客使用即可
   1. 下载dos2unix
      1. 备注【安装dos2uinx】
         1. window系统下载exe文件，追拖拉dos2unix.exe文件放置于`C:\Windows\System32`文件夹
         1. linux直接apt-get install dos2unix
         1. `npm install dos2unix`
      1. dos2unix.exe放置于testGenerateMdoutline文件夹中
      1. 运行以下命令 `dos2unix generateDirectoryRecursively.sh`
   1. 执行generateDirectoryRecursively.sh脚本即可，即为会直接同步所有md文档的更新
      1. `bash generateDirectoryRecursively.sh`
