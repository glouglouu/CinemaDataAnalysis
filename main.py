import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

problematic_lines = []

try:
    df = pd.read_csv("./salle_de_cinema_ile-de-france.csv", on_bad_lines='warn', encoding='utf-8', sep=';')
except pd.errors.ParserError as e:
    print(f"Erreur lors de la lecture : {e}")
finally:
    if problematic_lines: print("Lignes problématiques capturées :", problematic_lines)
    
    # print(df.head())
    
    # important_columns = ['fauteuils', 'écrans','entrées 2021', 'entrées 2022']
    # df_selected = df[important_columns]

    # print(df_selected.describe())
    
    # print(df['régionCNC'])
        
    # print(df['régionCNC'].value_counts())
    
    
#     region1_data = df[df['régionCNC'] == 1]
#     region2_data = df[df['régionCNC'] == 2]
    
#     entree_par_fauteuil = ['fauteuils', 'entrées 2022']   
    
#     df_describe1 = region1_data[entree_par_fauteuil].describe()
#     df_describe2 = region2_data[entree_par_fauteuil].describe()

#     print (df_describe1, df_describe2)
    
#     nbr_fauteuils_1 = df_describe1.iloc[0, 0]
#     nbr_entrees_1 = df_describe1.iloc[0, 1]
#     moy1 = nbr_entrees_1/nbr_fauteuils_1
    
#     nbr_fauteuils_2 = df_describe2.iloc[0, 0]
#     nbr_entrees_2 = df_describe2.iloc[0, 1]
#     moy2 = nbr_entrees_2/nbr_fauteuils_2
    
#     print("Moyenne d'entrées par fauteuil en 2022, region 1: ", moy1)
#     print("Moyenne d'entrées par fauteuil en 2022, region 2: ", moy2)
    
# categories = np.array(['Region1', 'Region2'])
# values = np.array([moy1, moy2])

# plt.bar(categories, values, color='skyblue')

# plt.title("Diagramme des moyennes d'entrées par fauteuil en 2022, par région")
# plt.xlabel("Regions")
# plt.ylabel("Moyenne d'entrées par fauteuil")

# plt.show()

# if 'entrées 2021' in df.columns:
#     dfDuck = df.drop(columns=['entrées 2021'])
#     print(dfDuck.columns)
    
# dfRelation1 = df[['écrans','entrées 2022']]
# dfRelation2 = df[['fauteuils','entrées 2022']]

# correlation = dfRelation1.corr()
# correlation2 = dfRelation2.corr()

# print(correlation)
# print(correlation2)

# dfRelation1.plot(kind='scatter', x='écrans', y='entrées 2022')
# plt.show()

# dfRelation2.plot(kind='scatter', x='fauteuils', y='entrées 2022')
# plt.show()

dfExplicatives  = df[['écrans', 'fauteuils', 'population de la commune']]
dfCibles = df[['entrées 2022']]

print(dfExplicatives.head())





