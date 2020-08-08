import pandas as pd
import matplotlib.pyplot as plt

#load sample data
df = pd.read_csv("advertising_data.csv")

#data to scatter
x = df['TV']
y = df['sales']

#plotting data
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel("Money spent on TV Ads ($)")
plt.ylabel("Sales ($)")
plt.show()
