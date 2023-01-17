import pandas as pd
from matplotlib import pyplot as plt


def mostrar():
    df = pd.read_csv('df_covid19_countries2.csv')
    df2 = df[['location', 'total_cases', 'date']]

    print(df2)

    """""

        df = pd.read_csv('df_covid19_countries2.csv')
    print(df.loc[df['location', 'date'] == 'Afghanistan'])

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
