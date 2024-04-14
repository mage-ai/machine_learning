from mage_ai.orchestration.triggers.api import trigger_pipeline
from mage_ai.settings.repo import get_repo_path


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    result = trigger_pipeline(
        'prepare_data', 
        check_status=True,
        error_on_failure=True,
        poll_interval=30,
        poll_timeout=None,
        verbose=True,
        remote_blocks=[
            dict(
                block_uuid='ml/feature_fetching/delivered_at_retain', 
                execution_partition=kwargs.get('execution_partition'), 
                pipeline_uuid='ml_feature_fetching', 
                repo_path=get_repo_path(),
            ),
        ],
        return_remote_blocks=True,
    )

    remote_block = result[-1].get('remote_blocks', [])[-1]

    if remote_block:
        return remote_block.get_outputs()

    return []