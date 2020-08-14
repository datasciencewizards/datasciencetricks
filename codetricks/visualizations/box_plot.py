import pandas as pd 
import seaborn as sns

#basic seaborn setting to beautify
color = sns.color_palette("Set2", 6)
sns.set_context("paper", font_scale=0.85) 

#load sample data
df = pd.read_csv("Iris.csv")

#selecting columns to plot
df = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm']]

#creating box plots
ax = sns.boxplot(data=df, palette=color, linewidth = 0.95)
ax.set_xlabel("Features",fontsize=18)
ax.set_ylabel("Values",fontsize=18)
