<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [安装Yaml第三方库](#%E5%AE%89%E8%A3%85yaml%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93)
- [yaml文件介绍](#yaml%E6%96%87%E4%BB%B6%E4%BB%8B%E7%BB%8D)
  - [注意事项](#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)
  - [文件案例](#%E6%96%87%E4%BB%B6%E6%A1%88%E4%BE%8B)
- [Python读取yaml文件](#python%E8%AF%BB%E5%8F%96yaml%E6%96%87%E4%BB%B6)
- [参考](#%E5%8F%82%E8%80%83)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 安装Yaml第三方库

- 主要是介绍对应的命令如下所示【以下命令都可，选一个即可】

  - ```
    pip install pyyaml
    conda install pyyaml
    ```

# yaml文件介绍

- yaml读取文件具体可以参考对应default.yaml文件【在下文文件案例给出】，具体形式如下所示。yaml对大小写和缩进敏感，如果在同一个缩进里面即为为同一层级字典形式，强制转化为`!!str 11`【从int类型转化为str类型】

- yaml存储了三种数据结构，即为对象、数组、纯量【在python对应为字典，列表，基本数据结构】

  - 对象，即为键值对的集合，在python读取后为字典

    - 可以嵌套/不嵌套，具体如下所示，config为不嵌套，nest_config为嵌套形式

      - ```
        config: usage_yaml
        nest_config:
        	para_1 : 1
        	para_2 : 2
        ```

  - 数组，一次按照次数排列，具体在python读取后为列表

    - 数组具体排列形式如下所示

      - ```
        para_list:
        	- 1
        	- 2
        	- 3
        ```

  - 纯量（scalars）,如字符串，布尔值，整数，浮点数，NULL，时间【为ISO8601格式】、日期【ISO8601格式】等

    - ```
      para_str: "1"
      para_boolen: true
      para_int: 1
      para_float: 2.0
      para_null: ~
      para_datetime: 2024-01-13
      para_time: 2001-12-14t21:59:43.10-05:00
      ```

## 注意事项

- 本版本的yaml为Version: 5.4.1，加载的时候为`yaml.load(file_stream, Loader=yaml.FullLoader)`

  - >  所以抛弃了yaml.load(stream)方法，
    > 所以会报以下错误：TypeError: load() missing 1 required positional argument: 'Loader'【所以需要查看版本号】，如果为5.1之前，可以使用yaml.load(file)

- 在yaml中不能使用Tab，需要使用四个space代替

- yaml注释形式为# 

- yaml对于""和''不敏感，但是对大小写敏感

## 文件案例

- ```
  config : usage_yaml # 这里是非嵌套形式的参数
  nest_config : # 这里是嵌套形式的参数
      para_1: 1
      para_2: 2
  para_list: # 读取后为列表形式
    - 1
    - 2
    - 3
  para_str: "1" # 读取后为字符串形式
  para_boolen: true
  para_int: 1
  para_float: 2.0
  para_null: ~
  para_datetime: 2024-01-13
  para_time: 2001-12-14t21:59:43.10-05:00
  para_list_dict:
    - user: '1'
      password: '123456'
    - user: "2"
      password: '123'
  ```

# Python读取yaml文件

- 具体通过open函数或者with open函数读取，获取stream流对象，根据` yaml.load(file_stream, Loader=yaml.FullLoader)`直接调用即可

- 具体代码参照loadYaml.py文件

  - ```
    import yaml
    '''
    1. 本版本的yaml为Version: 5.4.1，所以抛弃了yaml.load(stream)方法，
        所以会报以下错误：TypeError: load() missing 1 required positional argument: 'Loader'
        所以在yaml.load(stream, Loader)形式的文件中输入为yaml.load(file_stream, Loader=yaml.FullLoader)
    2. 在yaml中不能使用Tab，需要使用四个space代替
    3. yaml注释形式为# 
    4. yaml对于""和''不敏感，但是对大小写敏感
    '''
    
    def load_yaml(data_dir):
        with open(data_dir) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        f.close()
        return config
    
    if __name__ == "__main__":
        data_dir = './default.yaml'
        config = load_yaml(data_dir)
        print(config)
    ```

# 参考

- [python读取yaml配置文件](https://cloud.tencent.com/developer/article/1571186)
- [stack overflow解决yaml读取无法识别\t](https://stackoverflow.com/questions/56696640/yaml-scanner-scannererror-while-scanning-for-the-next-token-found-character-t)
- [使用 python 读取 yaml 文件](https://blog.csdn.net/HeatDeath/article/details/72833642)
- [解决报错：TypeError: load() missing 1 required positional argument: ‘Loader‘](https://blog.csdn.net/qq_44824148/article/details/122337056)