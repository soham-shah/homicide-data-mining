# Question: Is there a correlation between homicide and time of year, location?
# Homicides per month for certain state(s) and year(s)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'Weapon', 'Incident', 'Crime Type', 'Crime Solved', 'Perpetrator Count', 'Perpetrator Race', 'Victim Race', 'Perpetrator Age', 'Victim Ethnicity', 'Perpetrator Ethnicity', 'Relationship','Record Source', 'Victim Age', 'Victim Sex', 'Perpetrator Sex'],axis=1))
#print(dataArr.head(n=10))

#year = dataArr.loc[dataArr['Year'] == 1980]
#state = dataArr.loc[dataArr['State'] == "Alaska"]

year = 2010,2011,2012,2013,2014
state = "District of Columbia", "Louisiana", "Missouri", "Maryland","South Carolina","Michigan","Tennessee","Florida","New Mexico","Nevada"

year_state = dataArr.loc[dataArr['Year'].isin(year) & (dataArr['State'].isin(state))]

#print year_state.head(n=1000)

# get count of each unique thing in month and sort based on Month
grouped = year_state.groupby("Month").size().reset_index()

grouped[0] = grouped[0].div(len(year)*len(state)).round(0)

months = {'March': 3, 'February': 2, 'August': 8, 'September': 9, 'April': 4, 'June': 6, 'July': 7, 'January': 1, 'May': 5, 'November': 11, 'December': 12, 'October': 10}
grouped["month_number"] = grouped["Month"].map(months)
grouped = grouped.sort_values("month_number", ascending=True)
print(grouped)

# plot the result
y_pos = np.arange(len(grouped["Month"]))
plt.bar(y_pos, grouped[0])
plt.xticks(y_pos, grouped["Month"])
plt.xticks(rotation=90)
plt.ylabel("Homicides")
plt.xlabel("Month")
plt.title("Homicides Per Month (2010-2014)")
#fix the viewport to grab everything
plt.tight_layout()
plt.show()

