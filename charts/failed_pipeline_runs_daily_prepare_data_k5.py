
@data_source
def d(df):
    return df[df['status'] == 'failed']
