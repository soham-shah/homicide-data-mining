import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Question: Does a homicide get solved easier if the victim count and/or perpetrator count is more than one?

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year','Month', 'Incident', 'Crime Type', 'Victim Sex','Victim Age','Victim Race','Victim Ethnicity','Perpetrator Sex','Perpetrator Age','Perpetrator Race','Perpetrator Ethnicity','Relationship','Weapon','Record Source'],axis=1))

# add 1 to every data entry since number given is # of additional victims/perps

dataArr["Victim Count"] = dataArr["Victim Count"]+1
dataArr["Perpetrator Count"] = dataArr["Perpetrator Count"]+1
num_vic = dataArr["Victim Count"].value_counts()
num_perp = dataArr["Perpetrator Count"].value_counts()

x_pos = np.arange(len(num_vic))
x_pos2 = np.arange(len(num_vic)-1)
width = 0.25
fig = plt.figure()
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

rects1 = ax.bar(x_pos, num_vic[:], width, color='r')
rects2 = ax.bar(x_pos+width, num_perp[:], width, color='g')
rects12 = ax2.bar(x_pos2, num_vic[1:], width, color='r')
rects22 = ax2.bar(x_pos2+width, num_perp[1:], width, color='g')

ax.set_ylabel('Bin Size')
ax.set_xlabel('Number of Victims/Perpetrators')
ax.set_xticks(x_pos+width)
ax.set_xticklabels(('1','2','3','4','5','6','7','8','9','10','11'))
ax.legend((rects1[0], rects2[0]), ('Victims', 'Perpetrators'))

ax2.set_ylabel('Bin Size')
ax2.set_xlabel('Number of Victims/Perpetrators')
ax2.set_xticks(x_pos2+width)
ax2.set_xticklabels(('2','3','4','5','6','7','8','9','10','11'))
ax2.legend((rects12[0], rects22[0]), ('Victims', 'Perpetrators'))

# fix the viewport to grab everything
plt.tight_layout()
# Note, save your output to the plots folder. name it something
plt.savefig('../plots/vic_perp_count_1.png')

plt.show()
