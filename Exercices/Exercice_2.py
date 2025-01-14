import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../salle_de_cinema_ile-de-france.csv", on_bad_lines='skip', encoding='utf-8', sep=';')

#Question 1

region1_data = df[df['régionCNC'] == 1]
region2_data = df[df['régionCNC'] == 2]

entree_par_fauteuil = ['fauteuils', 'entrées 2022']   

df_describe1 = region1_data[entree_par_fauteuil].describe()
df_describe2 = region2_data[entree_par_fauteuil].describe()

print (df_describe1, df_describe2)


nbr_fauteuils_1 = df_describe1.iloc[0, 0]
nbr_entrees_1 = df_describe1.iloc[0, 1]
moy1 = nbr_entrees_1/nbr_fauteuils_1

nbr_fauteuils_2 = df_describe2.iloc[0, 0]
nbr_entrees_2 = df_describe2.iloc[0, 1]
moy2 = nbr_entrees_2/nbr_fauteuils_2

print("Moyenne d'entrées par fauteuil en 2022, region 1: ", moy1)
print("Moyenne d'entrées par fauteuil en 2022, region 2: ", moy2)

#Question 2 => voir notes.txt


#Question 3
    
categories = np.array(['Region1', 'Region2'])
values = np.array([moy1, moy2])

plt.bar(categories, values, color='skyblue')

plt.title("Diagramme des moyennes d'entrées par fauteuil en 2022, par région")
plt.xlabel("Regions")
plt.ylabel("Moyenne d'entrées par fauteuil")

plt.show()