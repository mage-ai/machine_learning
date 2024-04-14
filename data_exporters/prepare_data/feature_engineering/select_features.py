import pandas as pd
from default_repo.machine_learning.utils.columns import get_numeric_columns


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(number_columns, df_numbers, df_categories, *args, **kwargs):
    columns_to_drop = [col for col in get_numeric_columns(df_categories) if 'user_id' != col]

    df = pd.concat([
        df_categories.drop(columns=columns_to_drop), 
        df_numbers,
    ], axis=1)
    
    return df