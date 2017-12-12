# Question: Is there a correlation between homicide and time of year, location?
# Homicides per month for a certain state and year

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'Weapon', 'Incident', 'Crime Type', 'Crime Solved', 'Perpetrator Count', 'Perpetrator Race', 'Victim Race', 'Perpetrator Age', 'Victim Ethnicity', 'Perpetrator Ethnicity', 'Relationship','Record Source', 'Victim Age', 'Victim Sex', 'Perpetrator Sex'],axis=1))
#print(dataArr.head(n=10))

#year = dataArr.loc[dataArr['Year'] == 1980]
#state = dataArr.loc[dataArr['State'] == "Alaska"]

year = 1980
state = "Alaska"

year_state = dataArr.loc[(dataArr['Year'] == year) & (dataArr['State'] == state)]

#print year_state.head(n=1000)

# get count of each unique thing in month and sort based on Month
grouped = year_state.groupby("Month").size().reset_index()

#print grouped

months = {'March': 3, 'February': 2, 'August': 8, 'September': 9, 'April': 4, 'June': 6, 'July': 7, 'January': 1, 'May': 5, 'November': 11, 'December': 12, 'October': 10}
grouped["month_number"] = grouped["Month"].map(months)
grouped = grouped.sort_values("month_number", ascending=True)
#print(grouped)

# plot the result
y_pos = np.arange(len(grouped["Month"]))
plt.scatter(y_pos, grouped[0])
plt.xticks(y_pos, grouped["Month"])
plt.xticks(rotation=90)
plt.ylabel("Homicides")
plt.xlabel("Month")
plt.title("Homicides Per Month {}-{}".format(state,year))
#fix the viewport to grab everything
plt.tight_layout()
plt.show()

