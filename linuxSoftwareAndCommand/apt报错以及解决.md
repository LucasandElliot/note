[toc]

# 备份source.list

- ```
  sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
  ```

# 更换以及修改对应版本镜像源

- ```
  sudo gedit /etc/apt/sources.list 
  # 修改对应的soucrecs.list文件
  ```

- 清华镜像源网站【Ubuntu为例】
  - ARM-64架构
    - https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu-ports/
  - x86结构以及32/64位系统
    - https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/
- 选择对应系统版本的apt【以ARM为例】
  - ![image-20231230190812214](src/image-20231230190812214.png)

- 执行更新即可

  - ```
    sudo apt-get update
    sudo apt-get upgrade
    ```

- 随后等待更新成功即可

  - server certificate verification failed，将https更换为http即可
  - CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none 将https更换为http即可，或者查看对应笔记