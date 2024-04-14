import json
import requests


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    pipeline_uuid = kwargs.get('pipeline_uuid', 'ml_inference_online')
    block_uuid = kwargs.get('block_uuid', 'ml/inference/online/predictions')
    project = kwargs.get('project', 'machine_learning')
    variables = kwargs.get('variables', dict(
        probability=kwargs.get('probability', False),
        user_ids=kwargs.get('user_ids', [1, 5, 100]),
    ))

    record = kwargs.get('record', True)
    store_variables = kwargs.get('store_variables', True)
    run_upstream_blocks = kwargs.get('run_upstream_blocks', False)
    incomplete_only = kwargs.get('incomplete_only', False)

    token = kwargs.get('token', 'ec6bdfb8b27f4dc2a2c03d28b2de2876')

    # Define the URL of the API endpoint
    url = 'http://localhost:6789/api/runs'

    # Define the request payload as a dictionary
    payload = dict(
        run=dict(
            pipeline_uuid=pipeline_uuid, 
            block_uuid=block_uuid, 
            project=project, 
            variables=variables,
            record=record,
            store_variables=store_variables,
            run_upstream_blocks=run_upstream_blocks,
            incomplete_only=incomplete_only,
        ),
    )

    # Define the request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    # Make the POST request
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    print(json.dumps(response.json(), indent=2))