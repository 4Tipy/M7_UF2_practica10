import pandas as pd
from matplotlib import pyplot as plt


def mostrar():
    df = pd.read_csv('df_covid19_countries2.csv')

    pais = df['location'].unique()
    paises = pais.head(10)
    fechas = pd.Series(pd.date_range("2020-02-24", "2020-12-31"))

    imprimir = df.groupby(['location', 'date'])['total_cases']

    columnas = df[['location', 'total_cases', 'date']].head(10)

    print(imprimir)
    print("----------------")
    print(columnas)
    print("----------------")
    print(paises)

    """""
    ('location', 'date')('total_cases')
        df = pd.read_csv('df_covid19_countries2.csv')
    print(df.loc[df['location', 'date'] == 'Afghanistan'])

        df2 = df[['location', 'total_cases', 'date']]
    df = pd.read_csv('df_covid19_countries2.csv', usecols=['location'])
    print(df.head(2))
    print("---------------------------")
    print(df.columns)
    print("---------------------------")
    print(pd.unique(df['location']))
    print("---------------------------")
    print(df['total_cases'].describe())
    print("---------------------------")
    
    arxiu = pd.read_csv("golejadors.csv")
    player_goals = arxiu[(arxiu['Golejadors'] == 'Messi')]
    
    print(player_goals)
    print(player_goals['Goals'])
    print(player_goals['Goals].sum())
    
    
    print(arxiu.groupby(by='Golejadors').mean()) para calcular la media
    
        print(df.groupby("location").total_cases.sum()) ta mal
    """


mostrar()
