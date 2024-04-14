import pandas as pd

from default_repo.machine_learning.custom.ml.inference.online.predictions import (
    transform_custom as predict,
)

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    probability = kwargs.get('probability', False)
    user_ids = kwargs.get('user_ids', [1, 5, 100])

    y_pred = predict(probability=probability, user_ids=user_ids)
    columns = ['unsubscribed']
    if probability:
        columns = ['no', 'yes']
    else:
        y_pred = ['no' if 0 == v else 1 for v in y_pred]

    df = pd.concat([
        pd.DataFrame(user_ids, columns=['user_id']),
        pd.DataFrame(y_pred, columns=columns),
    ], axis=1)

    return df