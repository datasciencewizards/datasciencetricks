import matplotlib.pyplot as plt
import pandas as pd
 
#read data
df = pd.read_csv("https://raw.githubusercontent.com/datasciencewizards/datasciencetricks/master/data/AAPL_2014.csv")

#using date as x-axis
x = pd.to_datetime(df['Date'])

#using closing price as y-axis
y = df['Close']

#plotting the data
plt.plot(x,y)
plt.title('Apple Stock 2014')
plt.xlabel("Time")
plt.ylabel("Price ($)")
plt.show()
