import pandas as pd


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(user_profiles, email_content, user_emails, *args, **kwargs):
    df = pd.merge(user_profiles, user_emails, left_on=['id'], right_on=['user_id'], how='left')
    email_content.loc[:, 'email_id'] = email_content['id']
    df = pd.merge(df, email_content.drop(columns=['id']), left_on=['email_id'], right_on=['email_id'], how='left')

    return df


@test
def test_rows(df, *args) -> None:
    assert len(df.index) >= 11_972 is not None, 'There should be at least 11,972 rows.'


@test
def test_columns(df, *args) -> None:
    assert len(df.columns) == 18 is not None, 'There should be 18 columns'