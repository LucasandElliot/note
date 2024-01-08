# 查看虚拟环境

```
conda env list
```

# 移除虚拟环境

```
conda env remove --name envrionmentName 
```

# 创建虚拟环境

```
conda create --name envName python=3.x
```

# 导出Conda虚拟环境

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

  
