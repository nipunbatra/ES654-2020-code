
class AdaBoostClassifier():
    def __init__(self, base_estimator, n_estimators=50, learning_rate=1.0): # Optional Arguments: Type of estimator
        '''
        :param base_estimator: The base estimator model from which the boosted ensemble is built (e.g., DecisionTree, LinearRegression). If None, then the base estimator is DecisionTreeRegressor(max_depth=3).
                               You can pass the object of the estimator class
        :param n_estimators: The maximum number of estimators at which boosting is terminated. In case of perfect fit, the learning procedure is stopped early.
        :param learning_rate: Learning rate shrinks the contribution of each classifier by learning_rate. There is a trade-off between learning_rate and n_estimators.
        '''

        pass

    def fit(self, X, y):
        """
        Function to train and construct the AdaBoostClassifier
        Inputs:
        X: pd.DataFrame with rows as samples and columns as features (shape of X is N X P) where N is the number of samples and P is the number of columns.
        y: pd.Series with rows corresponding to output variable (shape of Y is N)
        """
        pass

    def predict(self, X):
        """
        Funtion to run the AdaBoostClassifier on a data point
        Input:
        X: pd.DataFrame with rows as samples and columns as features
        Output:
        y: pd.Series with rows corresponding to output variable. THe output variable in a row is the prediction for sample in corresponding row in X.
        """
        pass

    def plot(self):
        """
        Function to plot for the AdaBoostClassifier

        """
        pass


class AdaBoostRegressor():
    def __init__(self, base_estimator, n_estimators=50, learning_rate=1.0):
        '''
        :param base_estimator: The base estimator model from which the boosted ensemble is built (e.g., DecisionTree). If None, then the base estimator is DecisionTreeRegressor(max_depth=3).
                               You can pass the object of the estimator class
        :param n_estimators: The maximum number of estimators at which boosting is terminated. In case of perfect fit, the learning procedure is stopped early.
        :param learning_rate: Learning rate shrinks the contribution of each regressor by learning_rate. There is a trade-off between learning_rate and n_estimators.
        '''

        pass


    def fit(self, X, y):
        """
        Function to train and construct the AdaBoostRegressor
        Inputs:
        X: pd.DataFrame with rows as samples and columns as features (shape of X is N X P) where N is the number of samples and P is the number of columns.
        y: pd.Series with rows corresponding to output variable (shape of Y is N)
        """
        pass

    def predict(self, X):
        """
        Funtion to run the AdaBoostRegressor on a data point
        Input:
        X: pd.DataFrame with rows as samples and columns as features
        Output:
        y: pd.Series with rows corresponding to output variable. THe output variable in a row is the prediction for sample in corresponding row in X.
        """
        pass

    def plot(self):
        """
        Function to plot for the AdaBoostRegressor

        """
        pass
