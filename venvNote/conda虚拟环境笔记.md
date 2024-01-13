<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [查看虚拟环境](#%E6%9F%A5%E7%9C%8B%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)
- [移除虚拟环境](#%E7%A7%BB%E9%99%A4%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)
- [创建虚拟环境](#%E5%88%9B%E5%BB%BA%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)
- [导出conda虚拟环境](#%E5%AF%BC%E5%87%BAconda%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)
- [根据yaml导入安装虚拟环境](#%E6%A0%B9%E6%8D%AEyaml%E5%AF%BC%E5%85%A5%E5%AE%89%E8%A3%85%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)
- [conda添加镜像源](#conda%E6%B7%BB%E5%8A%A0%E9%95%9C%E5%83%8F%E6%BA%90)
- [conda 删除镜像源](#conda-%E5%88%A0%E9%99%A4%E9%95%9C%E5%83%8F%E6%BA%90)
- [conda 查看镜像源](#conda-%E6%9F%A5%E7%9C%8B%E9%95%9C%E5%83%8F%E6%BA%90)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 查看虚拟环境

```
conda env list
```

# 移除虚拟环境

```
conda env remove --name envrionmentName --all
```

# 创建虚拟环境

```
conda create --name envName python=3.x
```

# 导出conda虚拟环境

```
conda env export > environment.yaml
```

# 根据yaml导入安装虚拟环境

```
conda env create -f environment.yaml
```

# conda添加镜像源

- 下文以换清华镜像源为例子，具体代码如下图所示	

  - ```
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/

# conda 删除镜像源

- 具体代码为将channels中的url换成对应所需要的URL（删除即可）	

	- ```
  conda config --remove channels  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

# conda 查看镜像源

- ```
  conda config --show channels
  ```

  
