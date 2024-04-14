import pandas as pd


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(df, configurations, *args, **kwargs):
    label_feature_name = configurations['label_feature_name']
    uuid_column = configurations['uuid_column']
    sort_column_name = configurations['sort_column_name']

    df = df.sort_values(
        sort_column_name,
    ).groupby(
        uuid_column,
    ).last().reset_index()

    metadatas = [dict(block_uuid=f'{uuid_column}_{int(user_id)}') for user_id in df[uuid_column]]

    return [
        df.drop(columns=[
            label_feature_name,
            sort_column_name,
            uuid_column,
        ]),
        metadatas,
    ]


# @test
# def test_correct_sort(df, *args, **kwargs):
#     dfu = df[df['user_id'] == 1]
#     assert len(dfu.index) == 1, 'There should only be 1 row per user.'
    
#     assert dfu['email_delivered_at'][0] == '2012-05-15', 'User ID 1’s most recent email was delivered on 2012-05-15.'