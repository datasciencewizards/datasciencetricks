import pandas as pd
import matplotlib.pyplot as plt

#load sample data
df = pd.read_csv("cancer_data.csv")

#segment of data to visualize on y-axis
y = df['Total Proteins (g/dL)'][:5]

#patients name on x-axis 
x = ['Patient 1', 'Patient 2', 'Patient 3', 'Patient 4', 'Patient 5']

#plotting bar chart and displaying
plt.bar(x, y)
plt.title('Bar Chart')
plt.ylabel('Proteins (g/dL)')
plt.show()
