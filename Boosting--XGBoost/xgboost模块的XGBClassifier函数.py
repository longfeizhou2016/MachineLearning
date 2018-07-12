# -*- coding: utf-8 -*-

### load module
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from xgboost import plot_importance

### load datasets
digits = datasets.load_digits()

### data analysis
print(digits.data.shape)
print(digits.target.shape)

print(digits.target.value_counts())
### data split 
x_train,x_test,y_train,y_test = train_test_split(digits.data,
                                                 digits.target,
                                                 test_size = 0.3,
                                                 random_state = 33)

### fit model for train data
model = XGBClassifier(learning_rate=0.1,
                      n_estimators=1000,         # 树的个数--1000棵树建立xgboost
                      max_depth=6,               # 树的深度
                      min_child_weight = 1,      # 叶子节点最小权重
                      gamma=0.,                  # 惩罚项中叶子结点个数前的参数
                      subsample=0.8,             # 随机选择80%样本建立决策树
                      colsample_btree=0.8,       # 随机选择80%特征建立决策树
                      objective='multi:softmax', # 损失函数
                      scale_pos_weight=1,        # 解决样本个数不平衡的问题(二分类)
                      random_state=27            # 随机数
                      )
model.fit(x_train,y_train)

### plot feature importance
fig,ax = plt.subplots(figsize=(15,15))
plot_importance(model,
                height=0.5,
                ax=ax,
                max_num_features=64)
plt.show()

### make prediction for test data
y_pred = model.predict(x_test)

### model evaluate 
accuracy = accuracy_score(y_test,y_pred)
print("accuarcy: %.2f%%" % (accuracy*100.0))
"""
95.74%
"""