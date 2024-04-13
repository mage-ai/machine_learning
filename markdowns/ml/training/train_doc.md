# Train model

Select model architecture; SVM, decision tree, neural network, etc. Train model on data.

We’ll use a decision tree called XGBoost.

The label feature we’re predicting is the column `unsubscribed`, which has 2 values `no` and `yes`. 
This is a classification problem so we’ll use `XGBClassifier` from the XGBoost library.