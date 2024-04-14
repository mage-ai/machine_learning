import joblib
from typing import List

import pandas as pd

from mage_ai.data_preparation.models.global_data_product import GlobalDataProduct


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def fetch_features(user_ids: List[int], global_data_product_uuid: str):
    global_data_product = GlobalDataProduct.get(global_data_product_uuid)
    user_feature_store = global_data_product.get_outputs()

    df_features, user_id_dicts = user_feature_store['ml/feature_fetching/user_features']
    df_user_ids = pd.DataFrame(user_id_dicts)
    df_user_ids.columns = ['user_id']
    df_user_ids['user_id'] = df_user_ids['user_id'].apply(lambda x: int(x.replace('user_id_', '')))
    df = pd.concat([df_user_ids, df_features], axis=1)

    return df[df['user_id'].isin(user_ids)]


def load_model(model_training_global_data_product_uuid: str):
    global_data_product = GlobalDataProduct.get(model_training_global_data_product_uuid)
    model_file_path, _a, _b = global_data_product.get_outputs()['ml/training/explain']

    with open(model_file_path, 'rb') as f:
        model = joblib.load(f)
        
        return model


@custom
def transform_custom(*args, **kwargs):
    df = fetch_features(
        user_ids=kwargs.get('user_ids'), 
        global_data_product_uuid=kwargs.get('global_data_product_uuid', 'user_feature_store'),
    )

    model = load_model(kwargs.get('model_training_global_data_product_uuid', 'ml_model_training'))

    if kwargs.get('probability'):
        y_pred = model.predict_proba(df)
    else:
        y_pred = model.predict(df)

    return y_pred