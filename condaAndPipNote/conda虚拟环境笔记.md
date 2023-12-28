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

## 根据yaml导入安装虚拟环境

```
conda env create -f environment.yaml
```

