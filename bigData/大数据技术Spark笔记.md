# Spark特点

- 运行速度快：使用DAG执行引擎以支持循环数据流与内存计算

- 容易使用：支持使用Scala、Java、Python和R语言进行编程，可以通过Spark Shell进行交互式编程 

- 通用性：Spark提供了完整而强大的技术栈，包括SQL查询、流式计算、机器学习和图算法组件

- 运行模式多样：可运行于独立的集群模式中，可运行于Hadoop中，也可运行于Amazon EC2等云环境中，并且可以访问HDFS、Cassandra、HBase、Hive等多种数据源 

# Scala介绍

- Scala是Spark的主要编程语言，但Spark还支持Java、Python、R作为编程语言

- Scala的优势是提供了REPL（Read-Eval-Print Loop，交互式解释器），提高程序开发效率

- Scala具备强大的**并发性**，支持**函数式编程**，可以更好地支持分布式系统

  Scala语法简洁，能提供规范的API

# Spark与Hadoop对比优势

- Spark的计算模式也属于MapReduce，但不局限于Map和Reduce操作，还提供了**多种数据集操作类型**，编程模型比Hadoop MapReduce更灵活

- Spark提供了**内存计算**，可将中间结果放到内存中，对于迭代运算效率更高

- Spark基于DAG的**任务调度执行**机制，要优于Hadoop MapReduce的迭代执行机制 

# Spark运行架构

（未写）

# Spark代码实践

