import pandas as pd


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(gdp, *args, **kwargs):
    return [pd.concat(dfs) for dfs in kwargs.get('remote_blocks', [])]
    # trigger_pipeline(
    #     'prepare_data', 
    #     variables=dict(
    #         trigger=dict(
    #             upstream_blocks=[
    #                 dict(
    #                     pipeline_uuid='core_data_users_v0',
    #                     block_uuid='prepare_data/feature_engineering/add_and_combine_features',
    #                     execution_partition=kwargs.get('execution_partition'),
    #                 ),
    #             ],
    #         ),
    #     ),           
    #     check_status=True,
    #     error_on_failure=True,
    #     poll_interval=30,
    #     poll_timeout=None,
    #     verbose=True,
    # )