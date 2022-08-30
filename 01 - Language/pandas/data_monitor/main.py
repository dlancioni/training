# https://pandas.pydata.org/docs/user_guide/merging.html

import os
import numpy as np
import pandas as pd

def get_base(level):
    data = {"Level" :[level, level, level, level, level],"BusinessLine" :["CLEARING","DCS", "FUTURES", "PB", "SPG"]}
    cols = ["Level","BusinessLine"]
    df = pd.DataFrame(data, columns=cols)
    return df

def get_empty(level):
    level = f"Level {level}"
    data = {"BusinessLine" :["CLEARING","DCS", "FUTURES", "PB", "SPG"], level :[0, 0, 0, 0, 0]}
    cols = ["BusinessLine", level]
    df = pd.DataFrame(data, columns=cols)
    return df

def get_timed(level, dt, tm):

    col_bl = "BusinessLine"
    col_lv = f"Level {level}"
       
    file_name = f"PS RiskDB Data Monitor {dt} {tm}.csv"
    path = f"c:\\lancid\\data\\PS RiskDB Data Monitor {dt}\\{file_name}"
    df1 = pd.read_csv(path, ",")
   
    df1 = df1[[col_bl, col_lv]]
    df1 = df1[df1[col_lv] == "On"]
    df1 = df1.groupby([col_bl])[col_lv].count().reset_index()
    
    df2 = get_empty(level)
    df = df1.set_index(col_bl).combine_first(df2.set_index(col_bl)).reset_index()

    df.rename(columns={col_lv:tm}, inplace=True)
    
    return df


def main(dt, tms):
    result = []
    for level in [1]:
        df1 = get_base(level)
        for tm in tms:
            df2 = get_timed(level, dt, tm)
            df1 = pd.merge(df1, df2, on="BusinessLine")
        result.append(df1)
    result = pd.concat(result)
    return result

os.system("cls")
dt = "20220826"
tms = ["0700", "0800", "0900"]
result = main(dt,tms)
print(result)
