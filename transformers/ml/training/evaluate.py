import joblib
import numpy as np
import pandas as pd
import random
from sklearn.metrics import (
    accuracy_score,
    auc,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    model_file_path, label_classes, X_dicts, y_dicts = data
    X_test = pd.DataFrame(X_dicts)
    y_test = pd.DataFrame(y_dicts)
    y_test = y_test[y_test.columns[0]].to_numpy()
    label_classes = pd.Series(label_classes)

    with open(model_file_path, 'rb') as f:
        model = joblib.load(f)

    n_label_classes = len(label_classes)
    print(X_test)
    y_pred = model.predict(X_test)

    print('Sample predictions:')
    for i in y_pred[:10]:
        print(f'    {float(i)}')
    print('\n')

    if np.issubdtype(label_classes.dtype, int):
        label_indices = label_classes
    else:
        label_indices = np.array(range(n_label_classes))

    target_names = [str(label) for label in label_classes]
    try:
        classification_report_result = classification_report(
            y_test,
            y_pred,
            target_names=target_names,
        )
    except ValueError as err:
        print(f'Error occurred during classification report: {err}')
        classification_report_result = ''

    accuracy = accuracy_score(y_test, y_pred)
    confusion_matrix_result = confusion_matrix(y_test, y_pred)
    average_score_method = 'macro' if n_label_classes == 2 else 'weighted'
    precision = precision_score(y_test, y_pred, average=average_score_method)
    recall = recall_score(y_test, y_pred, average=average_score_method)
    f1 = f1_score(y_test, y_pred, average=average_score_method)

    constant_prediction = random.choice(list(label_indices))
    constant_guesses = [idx for idx in y_test if idx == constant_prediction]
    constant_guess = len(constant_guesses) / len(y_test)

    random_guesses = [idx for idx in y_test if idx == random.choice(list(label_indices))]
    random_guess = len(random_guesses) / len(y_test)

    mode = max(set(y_test), key=y_test.tolist().count)
    mode_guess = accuracy_score(y_test, np.full((len(y_test), 1), mode))

    y_pred_prob = None
    if n_label_classes == 2:
        y_pred_prob = model.predict_proba(X_test)

    if n_label_classes == 2 and y_pred_prob is not None:
        y_pred_prob_pos = [t[1] for t in y_pred_prob]
        roc_auc = roc_auc_score(y_test, y_pred)
        precision_points, \
        recall_points, \
        threshold_points = precision_recall_curve(
            y_test,
            y_pred_prob_pos,
            pos_label=label_indices[1],
        )
        fpr, tpr, roc_thresholds = roc_curve(
            y_test,
            y_pred_prob_pos,
            pos_label=label_indices[1],
        )
        auc_score = auc(fpr, tpr)
    else:
        roc_auc = None
        (
            precision_points,
            recall_points,
            threshold_points,
        ) = (np.array([]), np.array([]), np.array([]))
        fpr, tpr, roc_thresholds = (np.array([]), np.array([]), np.array([]))
        auc_score = None

    metrics = dict(
        accuracy=accuracy,
        auc_score=auc_score,
        classification_report=classification_report_result,
        confusion_matrix=confusion_matrix_result,
        constant_guess=constant_guess,
        f1=f1,
        false_positive_rates=fpr,
        mode_guess=mode_guess,
        number_of_test_examples=len(y_test),
        precision=precision,
        precision_points=precision_points,
        random_guess=random_guess,
        recall=recall,
        recall_points=recall_points,
        roc_auc=roc_auc,
        roc_thresholds=roc_thresholds,
        target_names=target_names,
        threshold_points=threshold_points,
        true_positive_rates=tpr,
    )

    return [
        [
            model_file_path,
            metrics,
        ],
    ]