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

# plot the result
print(grouped)
grouped.plot(kind="bar")
plt.show()