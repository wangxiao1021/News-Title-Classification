
目的在于交流学习。

适用于[中文新闻文本标题分类](https://aistudio.baidu.com/aistudio/competition/detail/10)。

关于课程和比赛的其他心得体会：[山竹小果 BLOG](https://www.cnblogs.com/shona/p/12767622.html)

## 1. 方法

a. 使用[PaddlePalm](https://github.com/PaddlePaddle/PALM)框架搭建任务；

b. 训练不同的分类任务：

1) 简单分类（14个别类）

2) 粗细粒度分类：
       
粗粒度：分为7大类（例如，财经、股票、彩票较为相似，归为一类；体育类别和其他基本有比较大的差异，单独为一类）；
        
细粒度：上述每个粗粒度类别中分为1~3个小类；

实际上，粗细粒度分类带来的提升有限，可能在类别划分上需要改进；

c. 使用不同的预训练模型：

1) ernie_zh_base

2) bert_zh_base

3) roberta_zh_base

4) roberta_zh_large

使用不同的预训练模型训练上述任务，其中，roberta_zh_large的效果最佳；

d. 不同的模型融合/任务融合方法：

1) probs层面：将不同模型/任务的预测结果，即probs加权求和，再得到最后的预测结果；

2) labels层面：将不同模型/任务的预测结果进行bagging，即投票，得到最终预测结果；

其中probs层面的融合效果更佳；

e. 规则提取：

基于一些易分错、同时具备明显特征（包含特殊词汇，但网络却不易识别）的类别，例如：时尚类别（满**减**）提取规则；

1) 基于关键词匹配；

2) 基于正则表达式抽取；

将符合规则的样本强制分到对应类别，可以带来一定提升。
    
## 2. 代码结构

a. paddlepalm：框架

b. run_(bert/ernie...).py：模型训练

c. pred_*.py：模型预测

d. scripts：数据处理/模型融合/规则提取脚本

e. *cu：粗粒度分类相关

f. *xi：细粒度分类相关

g. evaluate.py：模型评价（其中一个评价脚本放在paddlepalm文件夹下）

h. *.sh：一些运行脚本
