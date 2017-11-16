import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Question: s there a correlation between homicide and time of year, location?

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year', 'Incident', 'Crime Type', 'Crime Solved'],axis=1))
# print(dataArr.head(n=1))

# get count of each unique thing in month and sort based on Month
grouped = dataArr.groupby("Month").size().reset_index()
months = {'March': 3, 'February': 2, 'August': 8, 'September': 9, 'April': 4, 'June': 6, 'July': 7, 'January': 1, 'May': 5, 'November': 11, 'December': 12, 'October': 10}
grouped["month_number"] = grouped["Month"].map(months)
grouped = grouped.sort_values("month_number", ascending=True)
# print(grouped)

# plot the result
y_pos = np.arange(len(grouped["Month"]))
plt.bar(y_pos, grouped[0])
plt.xticks(y_pos, grouped["Month"])
plt.xticks(rotation=90)
plt.ylabel("Homicides")
plt.xlabel("Month")
plt.title("Homicides Per Month 1980-2014")
# fix the viewport to grab everything
plt.tight_layout()

# Note, save your output to the plots folder. name it something 
plt.savefig('../plots/month_1.png')
