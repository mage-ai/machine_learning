# [The definitive end-to-end machine learning (ML lifecycle) guide and tutorial for data engineers](https://www.notion.so/mageai/The-definitive-end-to-end-machine-learning-ML-lifecycle-guide-and-tutorial-for-data-engineers-ea24db5e562044c29d7227a67e70fd56?pvs=4)

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/mage-ml-guide.png?raw=true"
    width="500"
/>

# TLDR

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/ml.jpg?raw=true"
    width="500"
/>

1. Define problem
1. Prepare data
1. Train and evaluate
1. Deploy and integrate
1. Observe
1. Experiment
1. Retrain

<br />

# 🕵️‍♀️ Define problem

Clearly state the business problem you're trying to solve with machine learning and your hypothesis for how it can be solved.

[![Everything Is AWESOME](https://i.stack.imgur.com/q3ceS.png)](https://youtu.be/StTqXEQ2l-Y?t=35s "Everything Is AWESOME")

1. Open pipeline [`define_problem`](http://localhost:6789/pipelines/define_problem/edit).
1. Define the problem and your hypothesis.

<br />

# 💾 Prepare data

Collect data from various sources, generate additional training data if needed, and
perform feature engineering to transform the raw data into a set of useful input features.

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/data%20preparation%201.png?raw=true"
    width="500"
/>

1. The pipeline [`core_data_users_v0`](http://localhost:6789/pipelines/core_data_users_v0/edit)
   contains 3 tables that are joined together.
1. Pipeline [`prepare_data`](http://localhost:6789/pipelines/prepare_data/edit) is used in multiple
   other pipeline to perform data preparation on input datasets.
   1. For example, the [`ml_training`](http://localhost:6789/pipelines/ml_training/edit)
      pipeline that’s responsible for training an ML model will first run the above 2 pipelines to
      build the training set that’s used to train and test the model.

<br />

# 🦾 Train and evaluate

Use the training data to teach the machine learning model to make accurate predictions.
Evaluate the trained model's performance on a test set.

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/model%20training.png?raw=true"
    width="500"
/>

1. The [`ml_training`](http://localhost:6789/pipelines/ml_training/edit) pipeline takes in a
   training set and trains an XGBoost classifier to predict in what scenarios a user would unsubscribe
   from a marketing email.
1. This pipeline will also evaluate the model’s performance on a test data set.
   It’ll provide visualizations and explain which features are important using SHAP values.
1. Finally, this pipeline will serialize the model and its weights to disk to be used during
   the inference phase.

<br />

# 🤖 Deploy and integrate

Deploy the trained model to a production environment to generate predictions on new data,
either in real-time via an API or in batch pipelines.
Integrate the model's predictions with other business applications.

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/deploy%20model.png?raw=true"
    width="500"
/>

1. Once the model is done training and has been packaged for deployment, before we can use it to
   make predictions, we’ll need to setup our feature store that’ll serve user features on-demand
   when making a prediction.
1. Use the [`ml_feature_fetching`](http://localhost:6789/pipelines/ml_feature_fetching/edit)
   pipeline to prepare the features for each user ahead of time before progressing to the inference
   phase.
1. The [`ml_inference_offline`](http://localhost:6789/pipelines/ml_inference_offline/edit)
   pipeline is responsible for making batch predictions offline on the entire set of users.
1. The [`ml_inference_online`](http://localhost:6789/pipelines/ml_inference_online/edit)
   pipeline serves real-time model predictions and can be interacted with via an API request.
   1. Use the [`ML playground`](http://localhost:6789/pipelines/ml_playground/edit)
      to interact with this model and make online predictions.

<br />

# 🔭 Observe

Monitor the deployed model's prediction performance, latency, and system health in the production environment.

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/observe.png?raw=true"
    width="500"
/>

<br />

# 🧪 Experiment

Conduct controlled experiments like A/B tests to measure the impact of the model's predictions on
business metrics. Compare the new model's performance to a control model or previous model versions.

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/experiment.png?raw=true"
    width="500"
/>

<br />

# 🏋️ Retrain

Continuously gather new training data and retrain the model periodically to maintain and
improve prediction performance.

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/retrain.png?raw=true"
    width="500"
/>

<br />

# Conclusion

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/ml%20tools.jpg?raw=true"
/>
