Q1 a) Implement Adaboost on Decision Stump (depth -1 tree]. You could use Decision Tree learnt in assignment #1 or sklearn decision tree and solve it for the case of real input and discrete output.

Q1 b) Implement AdaBoostClassifier on Iris data set. Fix a random seed of 42. Shuffle the dataset according to this random seed. Use the first 60% of the data for training and last 40% of the data set for testing. Using sepal width and petal width as the two features, plot the decision surfaces as done for Q1a) and compare the accuracy of AdaBoostClassifier using 3 estimators over decision stump.  

Q2 a) Implement LinearRegression() to implement linear regression with option of fit_intercept and method as normal equation.

Q2 b) Timing for LinearRegression(). What is the time complexity of solving linear regression using normal equations? Vary the number of samples and number of features to verify if the theoretical complexity matches empirical evidence.

Q2 c) Implement LinearRegression() on RealEstate dataset (as done earlier in assignment 1). Use 5-fold cross-validation. Plot the learnt coefficients across the five folds and calculate the train and test MAE across each of the fold.

Q3 a) Implement Bagging(BaseModel, num_estimators): where base model could be DecisionTree (or sklearn decision tree) you have implemented. In a later assignment, you would have to implement the above over LinearRegression() also.

Q3 b) Reproduce slides 13 to 17 from ensemble learning lecture. This would involve running Bagging(DecisionTree(), 5) on the dataset shown in lecture slides (real input and discrete output).

Q4 a) Implement RandomForest(DecisionTree(), num_estimators)

Q4 b) Generate the plots for Iris data set. Fix a random seed of 42. Shuffle the dataset according to this random seed. Use the first 60% of the data for training and last 40% of the data set for testing. Using sepal width and petal width as the two features.


Doubts about the assignment may be clarified here: https://docs.google.com/document/d/1oA-N4g7fBNLDlD3fHR5fKdaoInqHOB9qc9dZGKLTFII/edit?usp=sharing
