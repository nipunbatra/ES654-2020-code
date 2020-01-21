import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from linearRegression.linearRegression import LinearRegression

from metrics import *

np.random.seed(42)

N = 30
P = 5
X = pd.DataFrame(np.random.randn(N, P))
y = pd.Series(np.random.randn(N))

LR = LinearRegression()
LR.fit(X, y)
y_hat = LR.predict(X)
LR.plot()

print('RMSE: ', rmse(y_hat, y))
print('MAE: ', mae(y_hat, y))