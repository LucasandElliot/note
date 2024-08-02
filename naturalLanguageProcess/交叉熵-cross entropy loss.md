# 信息熵

- 公式
  - $\begin{aligned}\mathrm{H}\left(\mathrm{x}\right)&=-\mathrm{P}\left(\mathrm{x}\right)\cdot\log(\mathrm{P}\left(\mathrm{x}\right))\\&=-\sum_\mathrm{i}\mathrm{p}(\mathrm{x}_\mathrm{i})\cdot\log(\mathrm{p}(\mathrm{x}_\mathrm{i}))\end{aligned}$
- 衡量事件所带有的信息量，而且如果为连续分布转化求和为积分即可

# KL散度【相对熵】

- 当用一个分布q(x)拟合p(x)分布的时候得到的信息增量，对于连续分布而言，将求和转化为积分即可
- 公式
  - $\begin{aligned}
    \mathrm{KL}(\mathrm{p}||\mathrm{q})& =\sum_\mathrm{i}\left(-\mathrm{p(x_i)}\cdot\log(\mathrm{q(x_i)}-(-\mathrm{p(x_i)}\cdot\log(\mathrm{p(x_i)})))\right) \\
    &\mathrm{=-\sum_ip(x_i)\cdot\log(\frac{q(x_i)}{p(x_i)})}
    \end{aligned}$

# 交叉熵

- 交叉熵=信息熵+KL散度【相对熵】
- 公式
  - $\begin{aligned}\text{cross entropy }&=-\sum_{\mathrm{i}}\mathrm{p(x_i)}\cdot\log(\mathrm{q(x_i)})\\&=\mathrm{H}(\mathrm{x})+\mathrm{KL}(\mathrm{p}||\mathrm{q})\end{aligned}$

# pytorch实现

- pytorch交叉熵多加入了一个softmax层
- 输入有两种形式
  - input: [batch_size, num_class]
  - target:[batch_size]
  - input:[batch_size, num_class, d1,d2, dk]，k为k-dimensional loss，而且dk必须为0-1之间的概率分布/0-num_class之间的数值
  - target:[batch_size, d1,d2,dk]
- 可以理解为每个单词都是一个类别，因此序列标注和预测都是在进行多分类任务

# 参考

- [NLP笔记：浅谈交叉熵（cross entropy）](https://blog.csdn.net/codename_cys/article/details/110288295)

# 博客内容

## 介绍

crossentropy损失函数主要用于**多分类任务**。它计算了模型输出与真实标签之间的**交叉熵损失**，可以作为模型优化的目标函数。

在多分类任务中，每个样本有多个可能的类别，而模型**输出**的是每个样本属于**每个类别的概率分布**。交叉熵损失函数可以度量模型输出的概率分布与真实标签之间的距离，从而指导模型优化。

## Pytorch库的用法

```py
class torch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')
```
### 参数介绍

- weight， 为一维张量，具体的大小为M，M为样本的标签数量，代表赋予的类别的权重
- ignore_index，int类型数据，用于指定忽略某个类别的索引。默认为 -100，表示不忽略任何类别。
- reduction：指定损失函数的计算方式。可选项包括：'none'（不返回每个样本的损失值）、'mean'（返回每个样本的平均损失值）、'sum'（返回每个样本的总损失值）。

### 具体例子

```py
import torch
import torch.nn as nn
batch_size = 32
class_num = 3
inputs = torch.rand(batch_size, class_num) # [32, 3]
target = torch.randint(0, 3, size=(batch_size,)) # [32]
softmax = nn.Softmax()
inputs = softmax(inputs)
loss_func = nn.CrossEntropyLoss()
predict = loss_func(inputs, target)
print(predict)
# 需要注意的是需要先定义损失函数/softmax函数，而且在设置size的时候需要额外多加入一个括号
```
### 模型输入

- inputs：模型的输出，形状为 (batch_size, class_num)，class_num 表示类别数。可以看作是每个样本被分到每个类别的概率值（这里一般需要用softmax等进行进行转化）。
- target：真实标签，形状为 (batch_size)，其中每个元素的值是样本所属的类别索引。

## 计算方法

#### 二分类交叉熵损失函数

$L=\frac{1}{N} \sum_i L_i=\frac{1}{N} \sum_i-\left[y_i \cdot \log \left(p_i\right)+\left(1-y_i\right) \cdot \log \left(1-p_i\right)\right]$

#### 参数介绍

- N，代表了N个样本
- $L_{i}$，为某个样本的对应损失函数的值
- $y_{i}$为样本的label数值，如果是就为1，不是就为0
- $p_{i}$为模型输出的概率分布(数值），位于0-1之间

#### 多分类交叉熵损失函数

$L=\frac{1}{N} \sum_i L_i=-\frac{1}{N} \sum_i \sum_{c=1}^M y_{i c} \log \left(p_{i c}\right)$

#### 参数介绍

- N，代表了N个样本
- M，为M个种类或者类别
- $y_{ic}$，代表的是第i个样本对于第C个种类的label数值
- $p_{ic}$，代表的是第i个样本对于第C个种类的概率分布/(数值）

## 优点

在使用反向传播，梯度下降优化的时候，模型取决于**学习率**（learning rate）和**偏导值**，而且学习率我们可以手工设置，因此我们从偏导数出发。偏导数越大，证明模型的效果越差，但也会让学习的速率越快，因此使用交叉熵损失函数，在模型效果较差的时候学习速度会较快，更容易收敛。

## 缺点

注重的任务为分类，更容易学习不同类别之间的信息，较为关心正确预测概率的准确性，容易忽略其他的标签的差异和联系。学习得到的特征较为松散。

## 参考

[损失函数｜交叉熵损失函数（知乎）](https://zhihu.com/tardis/zm/art/35709485?source_id=1003)
[维基百科交叉熵介绍](https://zh.wikipedia.org/wiki/%E4%BA%A4%E5%8F%89%E7%86%B5)