import pandas as pd
import seaborn as sns

#load sample data
df = pd.read_csv("cancer_data.csv")

#remapping values
gen = {0: "Female", 1: "Male"}
df = df.replace({"Gender": gen})

#create violin plot
plot = sns.catplot(data=df, x="Gender", y="Age at diagnosis", 
                   hue="Alcohol", kind="violin", split=True)

#adding appropriate labels
plot._legend.set_title('Alcoholic')
new_labels = ['No', 'Yes']
for t,l in zip(plot._legend.texts,new_labels): t.set_text(l)
