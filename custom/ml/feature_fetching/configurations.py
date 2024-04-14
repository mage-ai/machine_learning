if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    return dict(
        label_feature_name='unsubscribed',
        sort_column_name='email_delivered_at',
        sort_column_name_init='delivered at',
        uuid_column='user_id',
    )