import pandas as pd
from sklearn.preprocessing import LabelEncoder

#read and print sample data
df = pd.read_csv("data.csv")
print(df)
# >>>                 name  gender  height
#    0      Sheldon Cooper    Male     156
#    1  Leonard Hofstadter    Male     142
#    2               Penny  Female     145

#Initializing encoder function
label_encoder = LabelEncoder()

#Fitting encoder model
print (label_encoder.fit_transform(df["gender"]))
# >>>[1, 1, 0]
