import pandas as pd


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, configurations, *args, **kwargs):
    df = pd.DataFrame()
    for dfs in data.values():
        df = pd.concat([df] + dfs)

    df[configurations['sort_column_name']] = df[configurations['sort_column_name_init']]

    return df