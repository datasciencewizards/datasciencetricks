import pandas as pd

#read and print sample data
df = pd.DataFrame({'name' : ['Sheldon','Raj'], 
                   'location': ['Texas, USA', 'New Delhi, India']})

#splitting location into hometown and country
df[['hometown', 'country']] = df['location'].str.split(', ', expand=True)

#dropping location column
df = df.drop(columns=['location'])

#print final dataframe
print(df)
# >>>      name   hometown country
#    0  Sheldon      Texas     USA
#    1      Raj  New Delhi   India      
