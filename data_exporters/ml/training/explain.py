import joblib
import os

import matplotlib.pyplot as plt
import numpy as np
import shap

from mage_ai.settings.repo import get_repo_path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, evaluation,  *args, **kwargs):
    label_classes, X, y = data

    best_model = None
    best_roc_auc = None

    for model_file_path, metrics in evaluation:
        model_name = os.path.basename(model_file_path)
        with open(model_file_path, 'rb') as f:
            model = joblib.load(f)

        # Plotting ROC Curve
        plt.figure(figsize=(10, 7))
        fpr = metrics['false_positive_rates']
        tpr = metrics['true_positive_rates']
        roc_auc = metrics['roc_auc']
        plt.plot(fpr, tpr, label=f"ROC curve (area = {roc_auc:.2f})")
        plt.plot([0, 1], [0, 1], 'k--')  # Random guess line
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'{model_name} Receiver Operating Characteristic (ROC) Curve')
        plt.legend(loc="lower right")
        plt.grid(True)
        plt.show()

        # Plotting Precision-Recall Curve
        precision_points = metrics['precision_points']
        recall_points = metrics['recall_points']
        threshold_points = metrics['threshold_points']
        plt.figure(figsize=(10, 7))
        plt.plot(threshold_points, precision_points[:-1], 'b--', label='Precision')
        plt.plot(threshold_points, recall_points[:-1], 'g-', label='Recall')
        plt.xlabel('Threshold')
        plt.ylabel('Precision/Recall')
        plt.title(f'{model_name} Precision-Recall Curve')
        plt.legend(loc="best")
        plt.grid(True)
        plt.show()

        # Bar plot for accuracy, f1, precision, and recall
        scalar_metrics = ['accuracy', 'f1', 'precision', 'recall']
        values = [metrics[metric] for metric in scalar_metrics]

        plt.figure(figsize=(8, 5))
        bar_positions = range(len(scalar_metrics))
        plt.bar(bar_positions, values, color='skyblue')
        plt.xticks(bar_positions, scalar_metrics)
        plt.ylabel('Score')
        plt.title(f'{model_name} Evaluation Metrics Overview')
        plt.ylim(0, 1)  # Assuming these metrics are scaled between 0 and 1
        plt.show()

        # Confusion matrix
        confusion_matrix = metrics['confusion_matrix']
        cm = np.array(metrics['confusion_matrix'])
        fig, ax = plt.subplots(figsize=(5, 5))  # Adjust size as needed
        cax = ax.matshow(cm, cmap=plt.cm.Blues)
        fig.colorbar(cax)

        ax.set_xticklabels([''] + ['Negative', 'Positive'])
        ax.set_yticklabels([''] + ['Negative', 'Positive'])
        ax.set_xlabel('Predicted')
        ax.set_ylabel('True')
        ax.set_title(f'{model_name} Confusion Matrix')

        # Loop over data dimensions and create text annotations.
        thresh = cm.max() / 2.  # Threshold for text color
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(j, i, format(cm[i, j], 'd'),
                        ha="center", va="center",
                        color="white" if cm[i, j] > thresh else "black")

        plt.show()

        # SHAP
        # Load JS visualization code to notebook
        shap.initjs()

        # Assuming your XGBoost model is named `model` and your features DataFrame is named X
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X)  # Replace X with your actual features DataFrame

        # Summary plot
        shap.summary_plot(shap_values, X, plot_type="bar")

        # For a detailed view of the first prediction
        shap.force_plot(explainer.expected_value, shap_values[0,:], X.iloc[0,:])

        if best_model is None or roc_auc > best_roc_auc:
            best_model = model
            best_model_name = model_name
            best_roc_auc = roc_auc
            
    print(f'Best model (best_model_name): {best_roc_auc} ROC AUC')

    model_file_path = os.path.join(
        get_repo_path(), 
        'models', 
        'ml', 
        'production',
        'v0', 
        kwargs.get('ds', 'now'),
        f'model.joblib',
    )
    os.makedirs(os.path.dirname(model_file_path), exist_ok=True)

    with open(model_file_path, 'wb') as f:
        joblib.dump(model, f, compress='zlib')

    return [
        model_file_path,
        best_model_name,
        best_roc_auc,
    ]