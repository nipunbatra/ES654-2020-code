### Questions

1. Complete the decision tree implementation in tree/base.py. **[5 marks]**
The code should be written in Python and not use existing libraries other than the ones already imported in the code. Your decision tree should work for four cases: i) discrete features, discrete output; ii) discrete features, real output; iii) real features, discrete output; real features, real output. Your decision tree should be able to use GiniIndex or InformationGain as the criteria for splitting. Your code should also be able to plot/display the decision tree. 

    > You should be editing the following files.
  
    - `metrics.py`: Complete the performance metrics functions in this file. 

    - `usage.py`: Run this file to check your solutions.

    - tree (Directory): Module for decision tree.
      - `base.py` : Complete Decision Tree Class.
      - `utils.py`: Complete all utility functions.
      - `__init__.py`: **Do not edit this**

    > You should run _usage.py_ to check your solutions. 

2. 
    a) Show the usage of *your decision tree* on the [IRIS](https://archive.ics.uci.edu/ml/datasets/Iris) dataset. The first 70% of the data should be used for training purposes and the remaining 30% for test purposes. Show the accuracy, per-class precision and recall of the decision tree you implemented on the test dataset. **[1 mark]**

    b) Use 5 fold cross-validation on the dataset. Using nested cross-validation find the optimum depth of the tree. **[2 marks]**
    
    > You should be editing `iris-experiments.py` for the code containing the experiments and 1.md for the plots/results and their analysis.

3. 
    a) Show the usage of your decision tree for the [real estate price prediction regression](https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set) problem. **[1 mark]**
    
    b) Compare the performance of your model with the decision tree module from scikit learn. **[1 mark]**
    
   > You should be editing `estate-experiments.py` for the code containing the experiments and 1.md for the plots/results and their analysis.
    
4. Create some fake data to do some experiments on the runtime complexity of your decision tree algorithm. Create a dataset with N samples and M binary features. Vary M and N to plot the time taken for: 1) learning the tree, 2) predicting for test data. How do these results compare with theoretical time complexity for decision tree creation and prediction. You should do the comparison for all the four cases of decision trees. **[2 marks]**	

    >You should be editing `experiments.py` for the code containing the experiments and 1.md for the plots and their analysis. 
	


You can write your queries about assignment 1 in this [Google Doc](https://docs.google.com/document/d/1F94IMZWgsdlNXAzkRMXOpcfg7RXhEcPuv37KtY391_M/edit?usp=sharing).
The Google Doc will be the **_only_** medium for query resolution.



 

