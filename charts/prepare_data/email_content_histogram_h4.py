columns = ['number of buttons']
col = list(filter(lambda x: df_1[x].dtype == float or df_1[x].dtype == int, columns))[0]
x = df_1[col]
