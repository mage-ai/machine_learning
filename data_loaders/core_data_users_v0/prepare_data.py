import pandas as pd

from mage_ai.orchestration.triggers.api import trigger_pipeline


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(gdp, *args, **kwargs):
    remote_blocks = kwargs.get('remote_blocks', [])
    df = [pd.concat(dfs) for dfs in remote_blocks]

    return trigger_pipeline(
        'prepare_data', 
        check_status=True,
        error_on_failure=True,
        poll_interval=30,
        poll_timeout=None,
        verbose=True,
        remote_blocks=[
            dict(
                block_uuid='prepare_data/feature_engineering/add_and_combine_features', 
                execution_partition='4/20240414T062315_511477', 
                pipeline_uuid='core_data_users_v0', 
                repo_path='/home/src/default_repo/machine_learning',
            ),
        ],
        return_remote_blocks=True,
    )