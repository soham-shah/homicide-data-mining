import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# answer: Is there a correlation between the relationships between the victim and the perpetrator?

dataArr = pd.read_csv("../data/database.csv")
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year','Month', 'Incident', 'Crime Type', 'Crime Solved'],axis=1))
# print(dataArr.head(n=1))
dataArr = dataArr[dataArr["Relationship"] != "Unknown"]
grouped = dataArr.groupby("Relationship").size().reset_index()
# print(grouped.columns.values.tolist())
grouped = grouped.sort_values(0, ascending=False)

print(grouped)
grouped.plot(kind="bar")
# plt.bar(grouped[0],grouped[1])
# print(grouped[grouped.columns[0]])
plt.show()
