"""
sub2에는 func2와 unit_test2 함수가 있습니다.

func2는 2개의 데이터프레임을 받아 시간 순서대로 합친 후, 5분 간격으로 샘플링한 결과를 반환합니다.
입력값은 데이터프레임 2개입니다.
결과는 데이터프레임 형식으로 'time', 'value', 'idx' 필드를 가지고 있습니다.

unit_test2 임의의 데이터 프레임 2개를 만든 후, func1 함수를 작동시켜 결과를 확인합니다.
입력값으로 데이터프레임의 길이 n을 받습니다.

"""


from .sub1 import func1
import pandas as pd
import datetime
import random

def func2(df1, df2):
    df = func1(df1, df2)
    """
    데이터 프레임 df1, df2를 순서대로 합친 후, 5분마다 샘플링합니다.
    샘플링 한 시간은 'idx' 열에 저장됩니다.
    """
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

def unit_test2(n):

    """
    임의의 데이터프레임을 2개 생성해 func2의 결과값을 반환해줍니다.
    입력값으로 데이터프레임의 길이 n을 받습니다.
    """

    start = datetime.datetime(2018, 4, 20, 0, 0, 0)
    end = datetime.datetime(2018, 4, 20, 4, 0, 0)

    data1_time = [start + (end - start) * random.random() for i in range(10)]
    data1_value = [random.random()*100 for i in range(10)]
    data2_time = [start + (end - start) * random.random() for i in range(10)]
    data2_value = [random.random()*100 for i in range(10)]

    df1 = pd.DataFrame({"time":data1_time,"value":data1_value})
    df2 = pd.DataFrame({"time":data2_time,"value":data2_value})

    df_res = func2(df1, df2)

    return df_res
