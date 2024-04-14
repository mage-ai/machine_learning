import joblib
import os

import pandas as pd


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(user_feature_store, model_training, *args, **kwargs):
    model_file_path = list(model_training.values())[0][0]
    with open(model_file_path, 'rb') as f:
        model = joblib.load(f)
        
    df_features, user_id_dicts = user_feature_store['ml/feature_fetching/user_features']
    df_user_ids = pd.DataFrame(user_id_dicts)
    df_user_ids.columns = ['user_id']
    df_user_ids['user_id'] = df_user_ids['user_id'].apply(lambda x: int(x.replace('user_id_', '')))
    df = pd.concat([df_user_ids, df_features], axis=1)

    y_pred = model.predict(df)
    df_user_ids['prediction'] = y_pred
    
    return df_user_ids