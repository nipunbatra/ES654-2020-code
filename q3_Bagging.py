"""
The current code given is for the Assignment 2.
> Classification
> Regression
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from metrics import *

from ensemble.bagging import BaggingClassifier
from ensemble.bagging import BaggingRegressor
from tree.base import DecisionTree
from linearRegression.linearRegression import LinearRegression 

########### RandomForestClassifier ###################

N = 30
P = 5
X = pd.DataFrame(np.random.randn(N, P))
y = pd.Series(np.random.randint(P, size = N), dtype="category")

for criteria in ['information_gain', 'gini_index']:
    tree = DecisionTree(criterion=criteria)
    Classifier_BG = BaggingClassifier(base_estimator=tree)
    Classifier_BG.fit(X, y)
    y_hat = Classifier_BG.predict(X)
    Classifier_BG.plot()
    print('Criteria :', criteria)
    print('Accuracy: ', accuracy(y_hat, y))
    for cls in y.unique():
        print('Precision: ', precision(y_hat, y, cls))
        print('Recall: ', recall(y_hat, y, cls))

########### RandomForestRegressor ###################

N = 30
P = 5
X = pd.DataFrame(np.random.randn(N, P))
y = pd.Series(np.random.randn(N))

LR = LinearRegression()
Regressor_BG = BaggingRegressor(base_estimator=LR)
Regressor_BG.fit(X, y)
y_hat = Regressor_BG.predict(X)
Regressor_BG.plot()
print('Criteria :', criteria)
print('RMSE: ', rmse(y_hat, y))
print('MAE: ', mae(y_hat, y))