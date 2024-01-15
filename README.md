# 介绍
1. 主要用于存放个人在自然语言处理或者其他课程内容授课内容，后续也会持续不断更新
1. 主要是用于仅供学习所用，如果需要有其他错误可以指出并在issue说明
1. 如果有其他问题请私信 lucasaeliott@gmail.com
1. 自动生成md文档的outline脚本步骤如下
   1. 运用npm下载doctoc，即为在admins权限下安装`npm install -g doctoc`
   1. 下载dos2unix.exe文件，执行`npm install dos2unix`或者追拖拉dos2unix.exe文件放置于`C:\Windows\System32`文件夹，linux直接apt-get install dos2unix即可，随后执行`dos2unix xxx.sh`
      1. 放置于testGenerateMdoutline文件夹中
   1. 执行generate_outline.sh脚本即可，`bash generate_outline.sh `，但是他只会保证在当前sh脚本同一级目录下的md文件自动生成，而不会保证子文件夹所有生成
