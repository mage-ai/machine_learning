from sklearn.preprocessing import (
    MaxAbsScaler,
    MinMaxScaler,
    Normalizer,
    PowerTransformer,
    QuantileTransformer,
    RobustScaler,
    StandardScaler,
    minmax_scale,
)

# Adjusted SCALERS to include instances except for minmax_scale which is handled separately
SCALERS = [
    ('max_abs_scaler', MaxAbsScaler(),),
    ('min_max_scaler', MinMaxScaler(),),
    ('normalizer', Normalizer(), dict(axis=0)),
    ('power_transformer', PowerTransformer(),),
    ('quantile_transformer', QuantileTransformer(),),
    ('robust_scaler', RobustScaler(),),
    ('standard_scaler', StandardScaler(),),
]


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(column, df, *args, **kwargs):
    columns = []

    for scaler_name, scaler, opts in SCALERS:
        # Use the instantiated scaler
        scaler.fit(df[[column]])
        col = f'{column}_{scaler_name}'
        df[col] = scaler.transform(df[[column]])
        columns.append(col)

    # Handling minmax_scale separately
    scaler_name = 'minmax_scale'
    col = f'{column}_{scaler_name}'
    df[col] = minmax_scale(df[[column]])
    columns.append(col)

    return df[columns]