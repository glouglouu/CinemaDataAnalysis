from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd

df = pd.read_csv("./salle_de_cinema_ile-de-france.csv", on_bad_lines='skip', encoding='utf-8', sep=';')
analyseDf = df['entrées 2021'].describe()
X = df[['écrans', 'fauteuils', 'population de la commune']]  
y = df['entrées 2022'].fillna(analyseDf['mean'])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Coefficient de détermination (R²): {r2}")
print(f"Erreur moyenne absolue (MAE): {mae}")

