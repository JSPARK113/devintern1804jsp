from .sub1 import func1

def func2(df1, df2):
    df = func1(df1, df2)

    df_res = pd.DataFrame(columns = ["time","value"])

    start = df.time.min()
    end = df.time.max()
    st_time = datetime.datetime(start.year, start.month, start.day, \
                                start.hour if start.minute//5*5+5 != 60 else start.hour+1, \
                                start.minute//5*5+5 if start.minute//5*5+5 != 60 else 0, 0)
    end_time = datetime.datetime(end.year, end.month, end.day, \
                                end.hour if end.minute//5*5+5 !=60 else end.hour+1 , \
                                end.minute//5*5+5 if end.minute//5*5+5 != 60 else 0, 0)

    i = st_time + datetime.timedelta(0,0,0,0,5,0)
    idx = []

    while i <= end_time:
        df_res0 = df[df['time'] < i]
        df_res.loc[len(df_res)] = df_res0.iloc[len(df_res0)-1]
        idx.append(i)
        i = i + datetime.timedelta(0,0,0,0,5,0)

    df_res['idx'] = idx

    return df_res
