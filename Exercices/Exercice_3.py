import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../salle_de_cinema_ile-de-france.csv", on_bad_lines='warn', encoding='utf-8', sep=';')
   
#Question 1

if 'entrées 2021' in df.columns:
    dfDuck = df.drop(columns=['entrées 2021'])
    print(dfDuck.columns)

#Question 2

dfRelation1 = df[['écrans','entrées 2022']]
dfRelation2 = df[['fauteuils','entrées 2022']]

correlation = dfRelation1.corr()
correlation2 = dfRelation2.corr()

print(correlation)
print(correlation2)

#Question 3

dfRelation1.plot(kind='scatter', x='écrans', y='entrées 2022')
plt.show()

dfRelation2.plot(kind='scatter', x='fauteuils', y='entrées 2022')
plt.show()

dfExplicatives  = df[['écrans', 'fauteuils', 'population de la commune']]
dfCibles = df[['entrées 2022']]

print(dfExplicatives.head())

#Question 4 => voir notes.txt









