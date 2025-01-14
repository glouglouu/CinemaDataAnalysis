import pandas as pd

#Question 1

df = pd.read_csv("../salle_de_cinema_ile-de-france.csv", on_bad_lines='warn', encoding='utf-8', sep=';')

#Question 2-3 => voir notes.txt

#Question 4

print(df.head())

#Question 5

important_columns = ['fauteuils', 'écrans','entrées 2021', 'entrées 2022']
df_selected = df[important_columns]

print(df_selected.describe())

    
