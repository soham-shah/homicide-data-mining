import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question: Can we predict under what situation/conditions is a homicide most likely to be solved?
# This script plots the crimes solved or not solved

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year','Month', 'Incident', 'Crime Type', 'Victim Sex', 'Victim Age', 'Victim Race', 'Victim Ethnicity', 'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Perpetrator Ethnicity', 'Relationship','Victim Count','Perpetrator Count', 'Record Source'],axis=1))
# print(dataArr.head(n=1))

# remove rows where the relationship is unknown
#dataArr = dataArr[dataArr["Relationship"] != "Unknown"]

# get count of each "Yes" and "No" for Crime Solved
grouped = dataArr.groupby("Crime Solved").size().reset_index()
grouped = grouped.sort_values(0, ascending=False)

# print count for records
print(grouped)

# plot the result
y_pos = np.arange(len(grouped["Crime Solved"]))
plt.bar(y_pos, grouped[0])
plt.xticks(y_pos, grouped["Crime Solved"])
plt.xticks(rotation=90)
# fix the viewport to grab everything
plt.tight_layout()

# Note, save your output to the plots folder. name it something 
plt.savefig('../plots/solved_1.png')
