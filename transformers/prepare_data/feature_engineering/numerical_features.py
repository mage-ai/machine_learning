from default_repo.machine_learning.utils.columns import get_numeric_columns


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    return [get_numeric_columns(df).tolist()]