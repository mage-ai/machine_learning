import pandas as pd
from sklearn.preprocessing import LabelEncoder


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(data, configurations, *args, **kwargs):
    label_feature_name = configurations['label_feature_name']

    df = pd.DataFrame()
    for dfs_gdp in data.values():
        for df_partition in dfs_gdp:
            df = pd.concat([df, df_partition])

    label_encoder = LabelEncoder()
    X = df.drop(columns=[label_feature_name])
    y = df[[label_feature_name]]
    y[label_feature_name] = label_encoder.fit_transform(df[label_feature_name])

    return [
        label_encoder.classes_,
        X,
        y,
    ]