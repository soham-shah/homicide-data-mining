import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question: Can we predict under what situation/conditions is a homicide most likely to be solved?
# This script plots the perps sex male or female

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year','Month', 'Incident', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Age', 'Victim Race', 'Victim Ethnicity', 'Perpetrator Age', 'Perpetrator Race', 'Perpetrator Ethnicity', 'Relationship','Victim Count','Weapon','Perpetrator Count', 'Record Source'],axis=1))
# print(dataArr.head(n=1))

# remove rows where the perps's sex is unknown
dataArr = dataArr[dataArr["Perpetrator Sex"] != "Unknown"]

# get count of "Male" and "Female" for Perpetrator Sex
grouped = dataArr.groupby("Perpetrator Sex").size().reset_index()
grouped = grouped.sort_values(0, ascending=False)

# print count for records
print(grouped)

# plot the result
y_pos = np.arange(len(grouped["Perpetrator Sex"]))
plt.bar(y_pos, grouped[0])
plt.xticks(y_pos, grouped["Perpetrator Sex"])
plt.xticks(rotation=90)
# fix the viewport to grab everything
plt.tight_layout()

# Note, save your output to the plots folder. name it something 
plt.savefig('../plots/perpsex_1.png')
