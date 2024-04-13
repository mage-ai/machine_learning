import dateutil.parser
import math

import pandas as pd

from mage_ai.data_preparation.models.pipeline import Pipeline


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


DATETIME_COLUMNS = [
    'date_joined',
    'delivered_at',
    'created_at',
]


@transformer
def transform(*args, **kwargs):
    df = pd.DataFrame()

    trigger = kwargs.get('trigger', {})
    upstream_blocks = trigger.get('upstream_blocks', [])
    for opts in upstream_blocks:
        pipeline = Pipeline.get(opts['pipeline_uuid'])
        block_uuid = opts['block_uuid']
        block = pipeline.get_block(block_uuid)

        execution_partition = opts.get('execution_partition')
        variable_uuids = block.output_variables(execution_partition=execution_partition)
        for variable_uuid in variable_uuids:
            output = pipeline.get_block_variable(block_uuid, variable_uuid, partition=execution_partition)
            df = pd.concat([df, output])
    
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    df = df.drop(columns=['id'])

    for col in DATETIME_COLUMNS:
        df[col] = df[col].apply(lambda x: dateutil.parser.parse(x).timestamp() if x else None)
        min_value = df[col].min()
        df[col] = df[col].apply(
            lambda x: x - min_value if x else None,
        )

    return df


@test
def test_lowercase(df, *args) -> None:
    assert list(df.columns) == [col.lower().replace(' ', '_') for col in df.columns], 'Column names need to be lowercase.'

@test
def test_underscore(df, *args) -> None:
    assert all([' ' not in col for col in df.columns]), 'Column names cannot have any spaces.'