"""
The current code given is for the Assignment 2.
> Classification
> Regression
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from metrics import *

from ensemble.ADABoost import AdaBoostClassifier
from ensemble.ADABoost import AdaBoostRegressor
from tree.base import DecisionTree
from linearRegression.linearRegression import LinearRegression 

np.random.seed(42)

########### AdaBoostClassifier ###################

N = 30
P = 5
X = pd.DataFrame({i:pd.Series(np.random.randint(P, size = N), dtype="category") for i in range(5)})
y = pd.Series(np.random.randint(P, size = N), dtype="category")

for criteria in ['information_gain', 'gini_index']:
    tree = DecisionTree(criterion=criteria)
    Classifier_AB = AdaBoostClassifier(base_estimator=tree)
    Classifier_AB.fit(X, y)
    y_hat = Classifier_AB.predict(X)
    Classifier_AB.plot()
    print('Criteria :', criteria)
    print('Accuracy: ', accuracy(y_hat, y))
    for cls in y.unique():
        print('Precision: ', precision(y_hat, y, cls))
        print('Recall: ', recall(y_hat, y, cls))

########### AdaBoostRegressor ###################

N = 30
P = 5
X = pd.DataFrame({i:pd.Series(np.random.randint(P, size = N), dtype="category") for i in range(5)})
y = pd.Series(np.random.randn(N))

LR = LinearRegression()
Regressor_AB = AdaBoostRegressor(base_estimator=LR)
Regressor_AB.fit(X, y)
y_hat = Regressor_AB.predict(X)
Regressor_AB.plot()
print('Criteria :', criteria)
print('RMSE: ', rmse(y_hat, y))
print('MAE: ', mae(y_hat, y))