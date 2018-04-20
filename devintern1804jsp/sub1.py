import pandas as import pd

def func1(df1, df2):

    df = pd.merge(df1, df2, how='outer').sort_values(by='time')
    df = df.reset_index(drop=True)

    return df_res
