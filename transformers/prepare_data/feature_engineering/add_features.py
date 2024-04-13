import pandas as pd


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    number_of_emails = df.groupby('user_id', as_index=True)[['user_id']].count()
    number_of_emails.columns = ['number_of_emails']
    number_of_emails = number_of_emails.reset_index()
    df = pd.merge(df, number_of_emails, on=['user_id'])

    number_of_unsubscribes = df.groupby('user_id', as_index=True)[['unsubscribed']].agg(
        lambda x: x.value_counts().to_dict().get('yes', 0),
    )
    number_of_unsubscribes.columns = ['number_of_unsubscribes']
    number_of_unsubscribes = number_of_unsubscribes.reset_index()
    df = pd.merge(df, number_of_unsubscribes, on=['user_id'])

    themes = df['theme'].unique()

    def __build_theme(x, themes=themes):
        value_counts = x.value_counts().to_dict()
        return [value_counts.get(theme, 0) for theme in value_counts]

    number_of_themes = df.groupby('user_id', as_index=True)[['theme']].apply(__build_theme).apply(pd.Series)
    number_of_themes.columns = [f'number_of_email_theme_{theme}' for theme in themes]
    number_of_themes = number_of_themes.reset_index()
    df = pd.merge(df, number_of_themes, on=['user_id'])

    categories = df['category'].unique()

    def __build_category(x, categories=categories):
        value_counts = x.value_counts().to_dict()
        return [value_counts.get(category, 0) for category in value_counts]

    number_of_categories = df.groupby('user_id', as_index=True)[['category']].apply(__build_category).apply(pd.Series)
    number_of_categories.columns = [f'number_of_email_category_{category}' for category in categories]
    number_of_categories = number_of_categories.reset_index()
    df = pd.merge(df, number_of_categories, on=['user_id'])

    return df


@test
def test_columns(df, *args) -> None:
    assert len(df.columns) >= 25, 'Number of columns should be at least 25.'