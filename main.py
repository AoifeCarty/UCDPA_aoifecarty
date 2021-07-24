import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import openpyxl

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
my_array=np.array(ND2)
print(my_array)

#Removed Unused Columns and add Total Column
finaldata=ND2.drop(['Unnamed: 0','Netflix','Amazon Prime Video'],axis=1)
finaldata.IMDb=finaldata.IMDb.astype(float)
finaldata['Rotten Tomatoes'] = finaldata['Rotten Tomatoes'].astype(float)
print(finaldata.info())
TotalScore=finaldata['IMDb']+finaldata['Rotten Tomatoes']
finaldata['TotalScore']=TotalScore
print(finaldata)

#Analytics & Charts
print(finaldata.iloc[finaldata['TotalScore'].idxmax()])
print(finaldata.iloc[finaldata['TotalScore'].idxmin()])
print(finaldata.groupby('Rating').first())

#Bar Chart No. of Movies
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])
x=['18+','16+','13+','7+','All']
y=finaldata['Rating'].value_counts()
addlabels(x,y)
plt.bar(x,y, color='hotpink')
plt.xlabel('Rating')
plt.ylabel('No. of Movies')
plt.title('Number of Movies by Age Rating')
plt.show()

sns.scatterplot(x='IMDb',
                y='Year',
                data=finaldata)
plt.show()
sns.scatterplot(x='Rotten Tomatoes',
                y='Year',
                data=finaldata)
plt.show()

sns.scatterplot(x='IMDb',
                y='Rotten Tomatoes',
                data=finaldata)
plt.show()


#Selecting Top 10
Top10TS=(finaldata.sort_values(by=['TotalScore'],ascending=False).head(10))

Top10IMDb=(ND2.sort_values(by=['IMDb'],ascending=False).head(10))
print(Top10IMDb)
Top10RT=(ND2.sort_values(by=['Rotten Tomatoes'],ascending=False).head(10))
print(Top10RT)
Top10IMDb.to_excel(r'C:\Users\aoife\exportIMDb.xlsx', index=False, header=True)
Top10RT.to_excel(r'C:\Users\aoife\exportRT.xlsx', index=False, header=True)
#API
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=amzn&apikey=QA2KXC8ZF2YYNVEV'
r = requests.get(url)
company_overview = r.json()
print(company_overview)
#Adding Second data set and merge
data2=pd.read_csv('Prime TV Shows.csv')
Mergedata=pd.merge(data2, finaldata, left_index=True, right_index=True)
print(Mergedata)
print(Mergedata.info())
