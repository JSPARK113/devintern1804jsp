
"""
sub1에는 func1과 unit_test1 함수가 있습니다.

func1은 2개의 데이터프레임을 시간 순서대로 합치는 함수입니다.
입력값은 데이터프레임 2개입니다.
결과는 데이터프레임 형식으로 'time', 'value' 필드를 가지고 있습니다.

unit_test1은 임의의 데이터 프레임 2개를 만든 후, func1 함수를 작동시켜 결과를 확인합니다.
입력값으로 데이터프레임의 길이 n을 받습니다.
"""

import pandas as import pd
import pandas as pd
import datetime
import random

def func1(df1, df2):
    """
    데이터프레임 df1과 df2를 시간 순서대로 합치는 함수입니다.
    """

    df = pd.merge(df1, df2, how='outer').sort_values(by='time')
    df = df.reset_index(drop=True)

    return df

def unit_test1(n):
    """
    임의의 데이터프레임을 2개 생성해 func1의 결과값을 반환해줍니다.
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

    df = func1(df1, df2)

    return df
