
class BaggingClassifier():
    def __init__(self, base_estimator, n_estimators=100):
        '''
        :param base_estimator: The base estimator model from which the bagged ensemble is built (e.g., DecisionTree, LinearRegression). If None, then the base estimator is DecisionTreeRegressor(max_depth=3).
                               You can pass the object of the estimator class
        :param n_estimators: The number of estimators/models in ensemble.
        :param criterion: The function to measure the quality of a split.
        :param max_depth: The maximum depth of the tree.
        '''

        pass

    def fit(self, X, y):
        """
        Function to train and construct the BaggingClassifier
        Inputs:
        X: pd.DataFrame with rows as samples and columns as features (shape of X is N X P) where N is the number of samples and P is the number of columns.
        y: pd.Series with rows corresponding to output variable (shape of Y is N)
        """
        pass

    def predict(self, X):
        """
        Funtion to run the BaggingClassifier on a data point
        Input:
        X: pd.DataFrame with rows as samples and columns as features
        Output:
        y: pd.Series with rows corresponding to output variable. THe output variable in a row is the prediction for sample in corresponding row in X.
        """
        pass

    def plot(self):
        """
        Function to plot for the BaggingClassifier

        """
        pass



class BaggingRegressor():
    def __init__(self, base_estimator, n_estimators=100):
        '''
        :param base_estimator: The base estimator model from which the bagged ensemble is built (e.g., DecisionTree, LinearRegression). If None, then the base estimator is DecisionTreeRegressor(max_depth=3).
                               You can pass the object of the estimator class
        :param n_estimators: The number of trees in the forest.
        :param criterion: The function to measure the quality of a split.
        :param max_depth: The maximum depth of the tree.
        '''

        pass

    def fit(self, X, y):
        """
        Function to train and construct the BaggingRegressor
        Inputs:
        X: pd.DataFrame with rows as samples and columns as features (shape of X is N X P) where N is the number of samples and P is the number of columns.
        y: pd.Series with rows corresponding to output variable (shape of Y is N)
        """
        pass

    def predict(self, X):
        """
        Funtion to run the BaggingRegressor on a data point
        Input:
        X: pd.DataFrame with rows as samples and columns as features
        Output:
        y: pd.Series with rows corresponding to output variable. THe output variable in a row is the prediction for sample in corresponding row in X.
        """
        pass

    def plot(self):
        """
        Function to plot for the BaggingRegressor

        """
        pass