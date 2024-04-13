import numpy as np
import pandas as pd


def get_numeric_columns(df: pd.DataFrame) -> pd.Index:
    return df.select_dtypes(include=[np.number]).columns