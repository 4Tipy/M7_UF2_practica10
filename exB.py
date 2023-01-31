import pandas as pd
import matplotlib.pyplot as plt


def func1():

    df = pd.read_csv('ciudades.csv', usecols=['City', 'Population']).head(10)
    data = df.to_dict('list')
    
    labels = data['City']
    sizes = data['Population']

    plt.pie(sizes, labels=labels)
    plt.title("primer grafico quesito")
    plt.show()

    return df


def func2():
    df2 = pd.read_csv('ciudades.csv', usecols=['City', 'Density KM2']).head(10)
    data = df2.to_dict('list')

    labels = data['City']
    sizes = data['Density M2']

    plt.pie(sizes, labels=labels)
    plt.title("primer grafico quesito")
    plt.show()

    return df
    return df2


def func3():
    df3 = pd.read_csv('ciudades.csv', usecols=['City', 'Density  M2']).head(10)
    return df3



