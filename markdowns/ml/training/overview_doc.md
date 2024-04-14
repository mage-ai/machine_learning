# Train model

<br />

<img 
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/model%20training.png?raw=true"
    width="500" 
/>

<br />

## What

Use the training data to teach the machine learning model to make accurate predictions. Evaluate the trained model's performance on a test set.

## Why

The model needs to learn patterns from historical data in order to make predictions on new unseen data. Thorough evaluation is critical to assess the model's real-world performance before deploying it.

## How

1. Split dataset into a training set and a test set.
2. Select model architecture; SVM, decision tree, neural network, etc. Train model on data.
3. [Identify relevant model performance metrics](https://www.mage.ai/blog/definitive-guide-to-accuracy-precision-recall-for-product-developers). Evaluate performance metrics on test set. Use cross-validation, compare against baseline or simpler models, constant guess, randomly guessing an outcome (e.g. a coin flip is 50% correct), mode guess, etc.
4. Debug the model by identifying edge cases, if the model is overfitting the data, etc.
5. Explain predictions using techniques like [SHAP](https://www.mage.ai/blog/how-to-interpret-explain-machine-learning-models-using-shap-values), [confusion matrix](https://www.mage.ai/blog/guide-to-model-metrics-p1-matrix-performance), etc.
6. [Improve model](https://www.mage.ai/blog/how-to-improve-the-performance-of-a-machine-learning-(ML)-model) by iterating with hyperparameter tuning, feature engineering, ensembles, and use different models for different subsets of the dataset.