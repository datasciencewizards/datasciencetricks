import pandas as pd
import seaborn as sns

#load sample data
df = pd.read_csv("cancer_data.csv")

#remapping values
maps = {0: "No", 1: "Yes"}
df = df.replace({"Smoking":maps, "Obesity":maps})

#seaborn setting to beautify
sns.set(style="whitegrid")

#create point plot
sns.pointplot(data = df, x="Obesity", y="Age at diagnosis",
              hue="Smoking", dodge=True, height=6, aspect=.5)
