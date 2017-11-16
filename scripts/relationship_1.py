import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question: Is there a correlation between the relationships between the victim and the perpetrator?

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year','Month', 'Incident', 'Crime Type', 'Crime Solved'],axis=1))
# print(dataArr.head(n=1))

# remove rows where the relationship is unknown
dataArr = dataArr[dataArr["Relationship"] != "Unknown"]

# get count of each uniqie thing in Relationship and sort
grouped = dataArr.groupby("Relationship").size().reset_index()
grouped = grouped.sort_values(0, ascending=False)
print(grouped)

# plot the result
y_pos = np.arange(len(grouped["Relationship"]))
plt.bar(y_pos, grouped[0])
plt.xticks(y_pos, grouped["Relationship"])
plt.xticks(rotation=90)
# fix the viewport to grab everything
plt.tight_layout()

# Note, save your output to the plots folder. name it something 
plt.savefig('../plots/relationship_1.png')
