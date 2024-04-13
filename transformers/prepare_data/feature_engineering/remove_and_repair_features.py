if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.columns = [col.lower().replace(' ', '_') for col in data.columns]
    return data


@test
def test_lowercase(df, *args) -> None:
    assert list(df.columns) == [col.lower().replace(' ', '_') for col in df.columns], 'Column names need to be lowercase.'

@test
def test_underscore(df, *args) -> None:
    assert all([' ' not in col for col in df.columns]), 'Column names cannot have any spaces.'