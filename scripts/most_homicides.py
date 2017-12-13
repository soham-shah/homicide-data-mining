# Question: Is there a correlation between homicide and time of year, location?

#Most homicides in past 5 years adjusted for population

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataArr = pd.read_csv("../data/database.csv")
popArr = pd.read_csv("~/Downloads/PEP_2014_PEPANNRES/PEP_2014_PEPANNRES_with_ann.csv")


# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'Weapon', 'Incident', 'Crime Type', 'Crime Solved', 'Perpetrator Count', 'Perpetrator Race', 'Victim Race', 'Perpetrator Age', 'Victim Ethnicity', 'Perpetrator Ethnicity', 'Relationship','Record Source', 'Victim Age', 'Victim Sex', 'Perpetrator Sex'],axis=1))
popArr = (popArr.drop(['GEO.id', 'GEO.id2','rescen42010','resbase42010'],axis=1))

#Drop rows 
popArr.drop(popArr.index[0:6], inplace=True)
popArr = popArr.reset_index()

popArr[['respop72010', 'respop72011','respop72012','respop72013','respop72014']] = popArr[['respop72010', 'respop72011','respop72012','respop72013','respop72014']].astype(float)
popArr['population'] = popArr.sum(axis=1) 

#Clean up
popArr = popArr.drop(['respop72010', 'respop72011','respop72012','respop72013','respop72014'],axis=1)         

#Average population over 5 years and per 10k people
popArr['population'] = popArr['population'].div(50000).round(0)

year = 2010,2011,2012,2013,2014

yearDF = dataArr.loc[dataArr['Year'].isin(year)]

# get count of each unique thing in state and sort based on state
grouped = yearDF.groupby("State").size().reset_index()

popArr['homicides'] = grouped[0]
popArr['truth'] = (popArr['homicides']/popArr['population']).round(1)

#print (popArr.head(n=100))

#print (grouped.head(n=100))

popArr= popArr.sort_values('truth', ascending=False)

y_pos = np.arange(len(popArr['GEO.display-label']))
plt.bar(y_pos, popArr['truth'])
plt.title('Number of Homicides Reported per 10k People (2010-2014)')
plt.xticks(y_pos, popArr['GEO.display-label'])
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.20)
plt.show()