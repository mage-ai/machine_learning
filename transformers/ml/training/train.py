import joblib
import os

import xgboost as xgb

from mage_ai.settings.repo import get_repo_path


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(configurations, training_set, split_indexes, *args, **kwargs):
    train_index, test_index = split_indexes
    label_classes, X, y = training_set

    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    hyperparameters = configurations['hyperparameters'].copy()
    hyperparameters.update(
        objective='binary:logistic',
        subsample=1.0,
        tree_method='auto',
        use_label_encoder=True,
        verbosity=3,   
    )
    model = xgb.XGBClassifier(**hyperparameters)
    model.fit(
        X_train,
        y_train,
        verbose=True,
    )

    split_index = kwargs.get('split_index', 0)
    model_file_path = os.path.join(
        get_repo_path(), 
        'models', 
        'ml', 
        kwargs['ds']
        f'model_{split_index}.joblib',
    )
    os.makedirs(os.path.dirname(model_file_path), exist_ok=True)

    with open(model_file_path, 'wb') as f:
        joblib.dump(model, f, compress='zlib')

    return [
        [
            model_file_path,
            label_classes,
            X_test,
            y_test,
        ]
    ]