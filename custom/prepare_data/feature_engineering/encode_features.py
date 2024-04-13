import pandas as pd
from sklearn.preprocessing import (
    LabelEncoder,
    OneHotEncoder,
)


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(df, *args, **kwargs):
    label_encoder = LabelEncoder()
    label_encoder.fit(df['subject'])
    df['subject'] = label_encoder.transform(df['subject'])

    for col in [
        'gender',
        'country',
        'theme',
        'category',
    ]:
        encoder = OneHotEncoder()
        encoder.fit(df[[col]])
        
        df_ohe = pd.DataFrame(
            encoder.transform(df[[col]]).toarray(), 
            columns=encoder.get_feature_names_out([col]),
        )

        df = pd.concat([df.drop(columns=[col]), df_ohe], axis=1)

    return df