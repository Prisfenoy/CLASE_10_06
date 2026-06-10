import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
# Hola hola 
datos = pd.read_csv("titanic.csv")
# Hola hola 
fig, ax = plt.subplots()
sns.countplot(x = "Sex", hue = "Survived", data = datos, ax = ax)
fig.savefig("plot.png")
# Hola hola 
# Hola hola 
fig, ax = plt.subplots()
sns.countplot(x = "Sex", hue = "Pclass", data = datos, ax = ax)
fig.savefig("plot2.png")
