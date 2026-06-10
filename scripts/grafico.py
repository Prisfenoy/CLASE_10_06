# Librerias
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Cargamos los datos
datos = pd.read_csv("titanic.csv")

# Grafico 1
fig, ax = plt.subplots()
sns.countplot(x = "Sex", hue = "Survived", data = datos, ax = ax)
fig.savefig("plot.png")

# Grafico 2
fig, ax = plt.subplots()
sns.countplot(x = "Pclass", hue = "Survived", data = datos, ax = ax)
fig.savefig("plot2.png")
