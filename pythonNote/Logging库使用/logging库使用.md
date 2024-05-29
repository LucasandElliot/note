# Log等级划分

- DEBUG， 最详细的日志信息
- INFO，详细仅次于DEBUG，只记录关键节点信息
- WARNING，用于记录记录一些WARNING，但是代码正常运行
- ERROR， 严重问题导致代码不能运行
- CRITICAL，发生了严重问题，代码不能正常运行
- 日志等级为DEUBUG->CRITICAL【从低到高】，日志信息逐渐减少

# Log模块级别函数

- | 代码                                   | 内容                                                         |
  | -------------------------------------- | ------------------------------------------------------------ |
  | logging.debug(msg, *args, **kwargs)    | 创建一条严重级别为DEBUG的日志记录                            |
  | logging.info(msg, *args, **kwargs)     | 创建一条严重级别为INFO的日志记录                             |
  | logging.warning(msg, *args, **kwargs)  | 创建一条严重级别为WARNING的日志记录                          |
  | logging.error(msg, *args, **kwargs)    | 创建一条严重级别为ERROR的日志记录                            |
  | logging.critical(msg, *args, **kwargs) | 创建一条严重级别为CRITICAL的日志记录                         |
  | logging.log(level, *args, **kwargs)    | 创建一条严重级别为level的日志记录                            |
  | logging.basicConfig(**kwargs)          | 对root logger进行一次性配置，需要设置记录日志级别，格式，日志输出位置，日志文件打开方式 |

# logging 组件

- | 类名      | 描述                                               |
  | --------- | -------------------------------------------------- |
  | logger    | 提供程序代码接口/logger类的初始化构造函数          |
  | handler   | 将日志记录发送到指定位置/分为stream和file的Handler |
  | filter    | 提供细粒度的日志过滤，决定部分日志会被输出         |
  | formatter | 控制日志信息最终输出                               |

## logger

- 一般用创建实例，在使用debug，info，warning等的时候必须创建类

- 代码

  - ```
    # 初始化logger
    logger = logging.getLogger('name')
    # 设置日志级别，只有大于WARNING才会被输出
    logger.setLevel(logging.WARNING)
    # 为Logger实例增加一个处理器
    logger.addHandler(handler_name)
    # 为 Logger 实例删除一个处理器
    logger.removeHandler(handler_name)
    ```

## handler

- 一般有StreamHandler，FileHandler和NullHandler

- 代码

  - ```
    # StreamHandler创建方式
    stream_handler = logging.StreamHandler(stream=None)
    # FileHandler创建方式
    file_handler = logging.FileHandler(filename, mode='a', encoding=None, delay=False)
    # NullHandler：NullHandler类位于核心logging包，不做任何的格式化或者输出。本质上它是个“什么都不做”的handler，由库开发者使用。 
    ```

- 创建StreamHandler之后，可以设置日志级别和设置Formatter，增删Filter

- 代码

  - ```
    
    # 设置stream_handler之后可以设置下列日志级别，格式化formatter和filters
    stream_handler.setLevel(logging.WARN) # 指定日志级别，低于WARN级别的日志将被忽略
    stream_handler.setFormatter(formatter_name) # 设置一个格式化器formatter
    stream_handler.addFilter(filter_name) # 增加一个过滤器，可以增加多个
    stream_handler.removeFilter(filter_name) # 删除一个过滤器
    ```

## filter

- 主要功能是允许Logger层级下的日志时间过滤，一般日志信息被输出需要经过：日志器级别过滤->日志器的filter过滤->日志器的handler过滤->日志器的handler的filter过滤

- 创建方式代码

  - ```
    filter = logging.Filter(name='')
    ```

## formatter

- 使用formatter对象设置之日信息最后的规则和内容，默认的时间格式为%Y-%M-%D %H:%M%S

- 创建方法代码

  - ```
    formatter = logging.Formatter(fmt=None, datefmt=None)
    # fmt是消息的格式化字符串，datefmt是日期字符串。如果不指明fmt，将使用'%(message)s'。如果不指明datefmt，将使用ISO8601日期格式。
    ```

## 组件的关系

- Logger里面可以有多个Handler/Filter，一个Handler可以有多个Formatter和Filters，而且日志级别会继承

# 使用案例

## 直接创建以及使用代码

- ```
  import logging
  import sys
  # 创建日志器logger并将其日志级别设置为DEBUG
  logger = logging.getLogger("Logger")
  logger.setLevel(logging.INFO)
  # 创建一个流处理器handler并将其日志级别设置为INFO
  handler = logging.StreamHandler(sys.stdout)
  handler.setLevel(logging.INFO)
  # 创建一个格式化器formatter并将其添加到处理器handler中
  formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
  handler.setFormatter(formatter)
  # 为日志器logger添加上面创建好的处理器handler
  logger.addHandler(handler)
  # 将日志打印在控制台
  logger.info('打印日志级别：info')
  ```

# 参考

- [Python中logging模块的基本用法](https://zhuanlan.zhihu.com/p/355448528)