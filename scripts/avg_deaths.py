# Question: Is there a correlation between homicide and time of year, location?\

#Which states have the most homicides ocurred in the past?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'Weapon', 'Incident', 'Crime Type', 'Crime Solved', 'Perpetrator Count', 'Perpetrator Race', 'Victim Race', 'Perpetrator Age', 'Victim Ethnicity', 'Perpetrator Ethnicity', 'Relationship','Record Source', 'Victim Age', 'Victim Sex', 'Perpetrator Sex'],axis=1))

# df['column_name'].isin(some_values)

year = 1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014

# Make a data frame that is populated with the variables we want

year_state = dataArr.loc[dataArr['Year'].isin(year)]

#print(year_state.head(n=1000))

# get count of each unique thing in state and sort based on state
grouped = year_state.groupby("State").size().reset_index()

#print (grouped)

#Get average over n years, this gives us number of deaths per year NOT ACCOUNTING FOR OUTLIER YEARS
grouped[0] = grouped[0].div(len(year)).round(0)
grouped = grouped.sort_values(0, ascending=False)

y_pos = np.arange(len(grouped['State']))
plt.bar(y_pos, grouped[0])
plt.title('Average Annual Deaths per State')
plt.xticks(y_pos, grouped["State"])
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.20)
plt.show()

