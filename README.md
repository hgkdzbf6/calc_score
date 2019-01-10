# calc_score

## 想法
基于[PyDiff](https://github.com/Fnjn/PyDiff.git)算法进行修改，计算出一个分数，用来比较pattern字符串和源字符串str的差异程度，用百分数表示。

## 核心思路：
最终分数和以下因素有关系
1. 字符长度
2. 错误字符位置，如果更靠前说明更不重要，靠后说明更重要
3. 错误字符类型

初步想法是，基础分数是100%，然后根据失配的情况，分别减去相应的分数。

1. 字符长度：
- sigmoid(abs(len(str) - len(pattern)))
2. 错误字符位置
- sigmoid(index*2/(len(str)/len(str)))
3. 错误字符类型
- 暂时不弄吧

