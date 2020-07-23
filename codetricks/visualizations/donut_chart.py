"""

Viz #2 - Donut Chart

"""

import pandas as pd
import matplotlib.pyplot as plt

#read sample data
df = pd.read_csv("cancer_data.csv")

#getting value counts of feature to analyze
vals= df['Performance Status'].value_counts()

#customizing labels and colors
labels = ['Good','Moderate','Poor']
colors = ['green','orange','red']

#generating pie plot (added some params to beautify)
plt.pie(vals, wedgeprops=dict(width=0.6), startangle=90,
        labels = labels, colors=colors, autopct="%.2f%%")

#display plot (shared in adjoining image)
plt.show()
