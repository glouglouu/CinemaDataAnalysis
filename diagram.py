import numpy as np
import matplotlib.pyplot as plt

# Exemple de données avec NumPy
categories = np.array(['Catégorie A', 'Catégorie B', 'Catégorie C', 'Catégorie D'])
values = np.array([23, 45, 12, 34])

# Création du diagramme en bâtons
plt.bar(categories, values, color='skyblue')

# Ajouter des titres et des étiquettes
plt.title("Diagramme en bâtons simple avec NumPy")
plt.xlabel("Catégories")
plt.ylabel("Valeurs")

# Afficher le graphique
plt.show()
