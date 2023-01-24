import pandas as pd
import matplotlib.pyplot as plt


def func1():
    df = pd.read_csv('ciudades.csv', usecols=['City', 'Population']).head(10)
    print(df)
    return df


def func2():
    df2 = pd.read_csv('ciudades.csv', usecols=['City', 'Density KM2']).head(10)
    print(df2)
    return df2


def func3():
    df3 = pd.read_csv('ciudades.csv', usecols=['City', 'Density  M2']).head(10)
    print(df3)
    return df3


def func4():
    plt.pie(func1(), func2(), func3())
    plt.show()
