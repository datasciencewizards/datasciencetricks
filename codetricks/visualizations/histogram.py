import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#sample data
df = pd.read_csv("cancer_data.csv")

#generating histogram of selected feature
feature = df['Age at diagnosis']
n, bins, patches = plt.hist(feature, bins = 10)

#ploting histogram
plt.xlabel('Age at diagnosis')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.grid(True)
plt.show()
