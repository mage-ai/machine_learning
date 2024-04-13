from mage_ai.orchestration.triggers.api import trigger_pipeline
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def trigger(*args, **kwargs):
    trigger_pipeline(
        'prepare_data', 
        variables=dict(
            trigger=dict(
                upstream_blocks=[
                    dict(
                        pipeline_uuid='core_data_users_v0',
                        block_uuid='prepare_data/feature_engineering/add_and_combine_features',
                        execution_partition=kwargs.get('execution_partition'),
                    ),
                ],
            ),
        ),           
        check_status=True,
        error_on_failure=True,
        poll_interval=30,
        poll_timeout=None,
        verbose=True,
    )
