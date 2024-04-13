import pandas as pd


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(dfs, *args, **kwargs):
    return pd.concat(dfs, axis=1)