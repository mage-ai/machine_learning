import pandas as pd
from default_repo.machine_learning.utils.columns import get_numeric_columns


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(df_numbers, df_categories, number_columns, *args, **kwargs):
    df = pd.concat([
        df_categories.drop(columns=get_numeric_columns(df_categories)), 
        df_numbers,
    ], axis=1)
    return df