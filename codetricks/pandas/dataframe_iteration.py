import pandas as pd

#read and print sample data
df = pd.read_csv("data.csv")
print(df)
# >>>     name    hometown country
#    0  Sheldon       Texas     USA
#    1  Leonard  New Jersey     USA

#using iterrows to print specific info
for index,row in df.iterrows():
    print(row["name"])
# >>>Sheldon
#    Leonard
             
#using itertuples to print all info
for row in df.itertuples():
    print(row)
# >>>Pandas(Index=0, name='Sheldon', hometown='Texas', country='USA')
#    Pandas(Index=1, name='Leonard', hometown='New Jersey', country='USA') 
