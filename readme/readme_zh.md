# 异常预测：一种具有显式延迟和预测范围的新方法
这是论文“异常预测：一种具有显式延迟和预测范围的新方法”的官方仓库

[简体中文](./readme_zh.md) [English](./readme.md)

论文链接: https://arxiv.org/abs/2408.04377

## 摘要
在时间序列数据中进行异常检测是各领域面临的关键挑战。传统方法通常专注于识别紧接着发生的异常，往往低估了诸如延迟时间和异常预测范围等时间动态的重要性，这些通常需要广泛的后续分析。本仓库引入了一种时间序列异常预测的新方法，将时间信息直接整合到预测结果中。我们提出了一个专门设计的新数据集，用于评估这种方法，并使用多种先进方法进行了全面的实验。结果表明，我们的方法在提供及时和准确的异常预测方面表现出色，为该领域未来的研究树立了新的基准。

## 显式延迟和预测范围的异常预测
![异常预测](./src/figure/anomaly_prediction.png)
*图 1：异常预测任务示意图。*

## 异常预测与异常检测的对比
![对比](./src/figure/comparison_ad_ap.png)
*图 2：异常预测与异常检测的对比。*

## 使用方法
要使用此仓库，请按照以下步骤操作：

1. 克隆仓库：
   ```bash
   git clone https://github.com/JiangYou2025/AnomalyPrediction.git

2. 打开 Anomaly_Prediction_Examples.ipynb：
   ```bash
   run all

## 示例

#### 使用全连接网络 (FCN) 对合成数据集 1 进行异常预测示例
![对比](./src/figure/synthetical_1_test_prediction_example_1.png)
![对比](./src/figure/synthetical_1_test_prediction_example_2.png)
![对比](./src/figure/synthetical_1_test_prediction_example_3.png)
*图 3：合成数据集 1 上的异常预测示例 1-9。*

#### 使用全连接网络 (FCN) 对合成数据集 10 进行异常预测示例
![对比](./src/figure/synthetical_10_test_prediction_example_1.png)
![对比](./src/figure/synthetical_10_test_prediction_example_2.png)
![对比](./src/figure/synthetical_10_test_prediction_example_3.png)
*图 4：合成数据集 10 上的异常预测示例 1-9。*

## 引用
在使用此论文或代码时，请引用：
   ```tex
   @inproceedings{you_2024_anomaly_prediction,
   author={You, Jiang and Cela, Arben and Natowicz, René and Ouanounou, Jacob and Siarry, Patrick},
   booktitle={2024 IEEE 20th International Conference on Intelligent Computer Communication and Processing (ICCP)}, 
   title={Anomaly Prediction: A Novel Approach with Explicit Delay and Horizon},
   year={2024},
   volume={},
   number={},
   pages={-},
   keywords={Time series;Anomaly Prediction;Anomaly Detection;U-Net;Transformers;},
   url={https://arxiv.org/abs/2408.04377}}
   ```
