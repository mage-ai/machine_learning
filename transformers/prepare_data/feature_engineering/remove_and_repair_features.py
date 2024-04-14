import dateutil.parser
import math

import pandas as pd

from mage_ai.data_preparation.models.global_data_product import GlobalDataProduct


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


DATETIME_COLUMNS = [
    'date_joined',
    'delivered_at',
    'created_at',
]


@transformer
def transform(*args, **kwargs):
    remote_blocks = kwargs.get('remote_blocks', [])

    if remote_blocks:
        df = pd.DataFrame()
        for remote_block_outputs in remote_blocks:
            for remote_block_output in remote_block_outputs:
                df = pd.concat([df, remote_block_output])
    else:
        global_data_product = GlobalDataProduct.get('core_data_users_v0')
        df = list(global_data_product.get_outputs().values())[0][0]
    
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    df = df.drop(columns=['id'])

    for col in DATETIME_COLUMNS:
        df[col] = df[col].apply(lambda x: dateutil.parser.parse(x).timestamp() if x else None)
        min_value = df[col].min()
        df[col] = df[col].apply(
            lambda x: x - min_value if x else None,
        )

    return df


# @test
# def test_lowercase(df, *args) -> None:
#     assert list(df.columns) == [col.lower().replace(' ', '_') for col in df.columns], 'Column names need to be lowercase.'

# @test
# def test_underscore(df, *args) -> None:
#     assert all([' ' not in col for col in df.columns]), 'Column names cannot have any spaces.'int