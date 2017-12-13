import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question: Can we predict under what situation/conditions is a homicide most likely to be solved?
# This script plots the months homices occured

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State','Crime Solved', 'Incident', 'Crime Type', 'Victim Sex', 'Victim Age', 'Victim Race', 'Victim Ethnicity', 'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Perpetrator Ethnicity', 'Relationship','Victim Count','Perpetrator Count', 'Record Source'],axis=1))

year = 2010,2011,2012,2013,2014
year_sorted = dataArr.loc[dataArr['Year'].isin(year)]

# get count of each "Yes" and "No" for Crime Solved
grouped = year_sorted.groupby("Month").size().reset_index()
grouped = grouped.sort_values(0, ascending=False)

# print count for records
print(grouped)

# plot the result
y_pos = np.arange(len(grouped["Month"]))
plt.bar(y_pos, grouped[0])
plt.xticks(y_pos, grouped["Month"])
plt.xticks(rotation=90)
plt.title("Total Homicide Count (2010-2014)")
plt.xlabel("Month")
plt.ylabel("Number of Homicides")
# fix the viewport to grab everything
plt.tight_layout()
plt.show()
# Note, save your output to the plots folder. name it something 
#plt.savefig('../plots/month_1.png')
