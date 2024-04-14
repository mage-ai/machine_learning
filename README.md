# [The definitive end-to-end machine learning (ML lifecycle) guide and tutorial for data engineers](https://www.notion.so/mageai/The-definitive-end-to-end-machine-learning-ML-lifecycle-guide-and-tutorial-for-data-engineers-ea24db5e562044c29d7227a67e70fd56?pvs=4)

<img src="https://github.com/mage-ai/assets/blob/main/machine-learning/mage-ml-guide.png?raw=true" />

## TLDR

1. Define problem
1. Prepare data
1. Train and evaluate
1. Deploy and integrate
1. Observe
1. Experiment
1. Retrain

<img src="https://github.com/mage-ai/assets/blob/main/machine-learning/ml.jpg?raw=true" />

---

## Setup

1. Clone the repository: `git clone https://github.com/mage-ai/machine_learning.git`.
    1. Stay in the same directory that you executed this command in; don’t change directory.

1. Run Docker:
    ```bash
    docker run -it -p 6789:6789 -v $(pwd):/home/src mageai/mageai /app/run_app.sh mage start machine_learning
    ```

    If you don’t use MacOS or Linux, check out other examples in Mage’s [quick start guide](https://docs.mage.ai/getting-started/setup).

1. Open a browser and go to [http://localhost:6789](http://localhost:6789).

---

## 🕵️‍♀️ Define problem

Clearly state the business problem you're trying to solve with machine learning and your hypothesis for how it can be solved.

1. Open pipeline [`define_problem`](http://localhost:6789/pipelines/define_problem/edit).

1. Define the problem and your hypothesis.

<video src="https://github.com/mage-ai/assets/assets/1066980/23d45e9e-cd03-4598-973d-590008788eb6"></video>

---

## 💾 Prepare data

Collect data from various sources, generate additional training data if needed, and
perform feature engineering to transform the raw data into a set of useful input features.

1. The pipeline [`core_data_users_v0`](http://localhost:6789/pipelines/core_data_users_v0/edit)
   contains 3 tables that are joined together.

1. Pipeline [`prepare_data`](http://localhost:6789/pipelines/prepare_data/edit) is used in multiple
   other pipeline to perform data preparation on input datasets.

    For example, the [`ml_training`](http://localhost:6789/pipelines/ml_training/edit)
    pipeline that’s responsible for training an ML model will first run the above 2 pipelines to
    build the training set that’s used to train and test the model.

### Collecting and combining core user data

<video src="https://github.com/mage-ai/assets/assets/1066980/06334154-96c1-48ae-9045-615175184ffa"></video>

### Feature engineering

<video src="https://github.com/mage-ai/assets/assets/1066980/5c8749aa-630e-4622-b7a9-35273feda140"></video>

---

## 🦾 Train and evaluate

Use the training data to teach the machine learning model to make accurate predictions.
Evaluate the trained model's performance on a test set.


1. The [`ml_training`](http://localhost:6789/pipelines/ml_training/edit) pipeline takes in a
    training set and trains an XGBoost classifier to predict in what scenarios a user would unsubscribe
    from a marketing email.

1. This pipeline will also evaluate the model’s performance on a test data set.
    It’ll provide visualizations and explain which features are important using SHAP values.

1. Finally, this pipeline will serialize the model and its weights to disk to be used during
    the inference phase.

<video src="https://github.com/mage-ai/assets/assets/1066980/5a4d86f8-3f0b-41c2-9127-99620bd5fe0e"></video>

---

## 🤖 Deploy and integrate

Deploy the trained model to a production environment to generate predictions on new data,
either in real-time via an API or in batch pipelines.
Integrate the model's predictions with other business applications.

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
    Use the [`ML playground`](http://localhost:6789/pipelines/ml_playground/edit)
    to interact with this model and make online predictions.

### Feature store and fetching

<video src="https://github.com/mage-ai/assets/assets/1066980/7deeee51-0fcb-44bf-8192-ae48b2bac0c7"></video>

### Batch offline predictions

<video src="https://github.com/mage-ai/assets/assets/1066980/0ce55744-8058-4b79-8699-d09c16f6aa0e"></video>

### Real-time online predictions

1. The pipeline used for online inference is called
    [`ml_inference_online`](http://localhost:6789/pipelines/ml_inference_online/edit).

1. Before interacting with the online predictions pipeline, you must first create an API trigger for
    [`ml_inference_online`](http://localhost:6789/pipelines/ml_inference_online/edit) pipeline.
    You can follow the [general instructions](https://docs.mage.ai/orchestration/triggers/trigger-pipeline-api)
    to create an API trigger.

1. The video below is for the pipeline named
    [`ml_playground`](http://localhost:6789/pipelines/ml_playground/edit), which contains
    [no-code UI interactions](https://docs.mage.ai/interactions/overview) to make it easy to
    play around with the online predictions.

<video src="https://github.com/mage-ai/assets/assets/1066980/f101bda8-603b-47bb-ae88-7c825dbdba08"></video>

---

## 🔭 Observe

Monitor the deployed model's prediction performance, latency, and system health in the production environment.

*Example coming soon.*

<img src="https://github.com/mage-ai/assets/blob/main/machine-learning/observe.png?raw=true" />

---

## 🧪 Experiment

Conduct controlled experiments like A/B tests to measure the impact of the model's predictions on
business metrics. Compare the new model's performance to a control model or previous model versions.

*Example coming soon.*

<img src="https://github.com/mage-ai/assets/blob/main/machine-learning/experiment.png?raw=true" />

---

## 🏋️ Retrain

Continuously gather new training data and retrain the model periodically to maintain and
improve prediction performance.

1. Every 2 hours, the retraining pipeline named
    [`ml_retraining_model`](http://localhost:6789/pipelines/ml_retraining_model/edit) will run.

1. The retraining pipeline triggers the [`ml_training`](http://localhost:6789/pipelines/ml_training/edit)
    pipeline if the following contrived condition is met:

    The number of partitions created for the `core_data.users_v0` data product is divisible by 4.

<video src="https://github.com/mage-ai/assets/assets/1066980/885eec0f-71b2-4485-87b1-e0931ec16537"></video>

---

## Conclusion

<img
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/ml%20tools.jpg?raw=true"
/>
