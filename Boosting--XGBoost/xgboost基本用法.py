# -*- coding: utf-8 -*-

### 载入数据
from sklearn import datasets    # 载入数据集
digits = datasets.load_digits() # 载入mnist数据集
print(digits.data.shape)        # 打印输入空间维度
print(digits.target.shape)      # 打印输出空间维度

### 数据分割
from sklearn.model_selection import train_test_split                 # 载入数据分割函数train_test_split
x_train,x_test,y_train,y_test = train_test_split(digits.data,        # 特征空间
                                                 digits.target,      # 输出空间
                                                 test_size = 0.3,    # 测试集占30%
                                                 random_state = 33)  # 为了复现实验，设置一个随机数

### 建立模型
from xgboost import XGBClassifier
model = XGBClassifier()               # 载入模型
model.fit(x_train,y_train)            # 训练模型（训练集）
y_pred = model.predict(x_test)        # 模型预测（测试集）

### 性能度量
from sklearn.metrics import accuracy_score   # 准确率
accuracy = accuracy_score(y_test,y_pred)     
print("accuarcy: %.2f%%" % (accuracy*100.0))

from sklearn import metrics
# 混淆矩阵
confusion = metrics.confusion_matrix(y_test,y_pred)
print(confusion)
print(confusion[1,1])

### 特征重要性
import matplotlib.pyplot as plt
from xgboost import plot_importance
fig,ax = plt.subplots(figsize=(10,15))
plot_importance(model,height=0.5,max_num_features=64,ax=ax)
plt.show()
