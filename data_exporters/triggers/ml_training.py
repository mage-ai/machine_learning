from mage_ai.orchestration.triggers.api import trigger_pipeline
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def trigger(*args, **kwargs):
    return trigger_pipeline(
        'ml_training', 
        check_status=True,
        error_on_failure=True,
        poll_interval=60,
        poll_timeout=None,
        verbose=True,
    )
