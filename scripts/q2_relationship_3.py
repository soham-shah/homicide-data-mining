import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question: Is there a correlation between the relationships between the victim and the perpetrator?
# Check the stats on how many crimes are solved based on relationship. 

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year','Month', 'Incident', 'Crime Type'],axis=1))
print(dataArr.head(n=1))

# remove rows where the relationship is unknown
# dataArr = dataArr[dataArr["Relationship"] != "Unknown"]

def condition(value):
    if value != "Acquaintance" and value != "Stranger":
        return "Family"
    return value

dataArr['Relationship'] = dataArr['Relationship'].apply(condition)

# get count of each uniqie thing in Relationship and sort
grouped = dataArr.groupby("Victim Age").size()#.reset_index()
grouped = grouped.sort_values(0, ascending=False)
print(grouped)
# plot the result

# plt.pie(grouped[0], labels=grouped["Relationship"], autopct='%.2f')


# plt.ylabel("Homicides")
# plt.xlabel("Relationship")
# plt.title("Homicides By Relationship Type")

# plt.tight_layout()

# Note, save your output to the plots folder. name it something 
# plt.savefig('../plots/q2_relationship_3.png')
