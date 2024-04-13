if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    columns = [col for col in df.columns if any([c in col for c in [
        'number_of_email_theme_',
        'number_of_email_category_',
    ]])]

    for col in columns:
        df[col] = df[col].fillna(0)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'