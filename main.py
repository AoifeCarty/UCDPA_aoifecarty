import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Popular Movies TV shows from Prime Videos Netflix version_3.csv")
print(data.shape)
print(data.isna())
print(data.isna().sum())
newdata=data.dropna()
print(newdata.isna().sum())
print(newdata.info())

#Remove duplicate titles
ND2=newdata.sort_values('Title', ascending=True)
ND2=newdata.drop_duplicates(subset='Title')
print(ND2)
