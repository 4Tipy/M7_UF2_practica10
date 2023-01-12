import pandas as pd
from matplotlib import pyplot as plt


def mostrar():
    df = pd.read_csv('df_covid19_countries2.csv', usecols=['location'])
    print(df.head(50))
    print("-----------------")
    print(df.groupby("location").total_cases.sum())


    """""
    print(df.head(2))
    print("---------------------------")
    print(df.columns)
    print("---------------------------")
    print(pd.unique(df['location']))
    print("---------------------------")
    print(df['total_cases'].describe())
    print("---------------------------")
    """


mostrar()
