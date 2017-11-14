import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Question: Does a homicide get solved easier if the victim count and/or perpetrator count is more than one?

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year','Month', 'Incident', 'Crime Type', 'Victim Sex','Victim Age','Victim Race','Victim Ethnicity','Perpetrator Sex','Perpetrator Age','Perpetrator Race','Relationship','Weapon','Record Source'],axis=1))

# add 1 to every data entry since number given is # of additional victims/perps
#print(dataArr.head(n=1))
dataArr = dataArr[dataArr["Victim Count"]+1]
#print(dataArr.head(n=1))
