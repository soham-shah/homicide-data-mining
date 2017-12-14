import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import tree
from pprint import pprint
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
import scikitplot as skplt

# Question: Can we predict under what situation/conditions is a homicide most likely to be solved?
# This script does decision tree classification
# Resources http://dataaspirant.com/2017/02/01/decision-tree-algorithm-python-with-scikit-learn/ , http://benalexkeen.com/decision-tree-classifier-in-python-using-scikit-learn/, https://dataaspirant.com/2017/04/21/visualize-decision-tree-python-graphviz/

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year','Incident', 'Crime Type', 'Victim Ethnicity', 'Perpetrator Race', 'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Ethnicity', 'Victim Count','Perpetrator Count', 'Record Source'],axis=1))
    
# Columns we are working with: Victim Age, Victim Sex, Victim Race, Month, Weapon, Crime Solved, relationship

#remove all rows where any of the attributes are not filled in correctely or are unknown
dataArr = dataArr[dataArr["Victim Age"] != 0]
dataArr = dataArr[dataArr["Victim Age"] <= 100]
dataArr = dataArr[dataArr["Victim Sex"] != "Unknown"]
dataArr = dataArr[dataArr["Victim Race"] != "Unknown"]
dataArr = dataArr[dataArr["Weapon"] != "Unknown"]
dataArr = dataArr[dataArr["Relationship"] != "Unknown"]

def condition(value):
    if value != "Stranger":
        return "Acquaintance"
    return value

dataArr['Relationship'] = dataArr['Relationship'].apply(condition)
dataArr["Relationship"] = dataArr["Relationship"].map({"Acquaintance":0,"Stranger":1})
#replace all categorical data with numerical data
dataArr['Victim Sex'] = dataArr['Victim Sex'].map({'Male': 0, 'Female': 1})
dataArr['Victim Race'] = dataArr['Victim Race'].map({'White': 0, 'Black': 1, 'Asian/Pacific Islander': 2, 'Native American/Alaska Native': 3})
dataArr['Weapon'] = dataArr['Weapon'].map({'Handgun': 0, 'Knife': 1, 'Blunt Object': 2, 'Firearm': 3, 'Shotgun': 4, 'Rifle': 5, 'Strangulation': 6, 'Fire': 7, 'Suffocation': 8, 'Gun': 9, 'Drugs': 10, 'Drowning': 11, 'Explosives': 12, 'Poison': 13, 'Fall': 14})
dataArr['Month'] = dataArr['Month'].map({'January': 0, 'February': 1, 'March': 2, 'April': 3, 'May': 4, 'June': 5, 'July': 6, 'August': 7, 'September': 8, 'October': 9, 'November': 10, 'December': 11})
dataArr["Crime Solved"] = dataArr["Crime Solved"].map({"No":0,"Yes":1})
print(dataArr.head(n=1))

print("correlation of Relationship and Victim Age", dataArr["Relationship"].corr(dataArr["Victim Age"], method='pearson'))
print("correlation of Relationship and Victim Sex", dataArr["Relationship"].corr(dataArr["Victim Sex"], method='pearson'))
print("correlation of Relationship and Race", dataArr["Relationship"].corr(dataArr["Victim Race"], method='pearson'))
print("correlation of Relationship and Weapon", dataArr["Relationship"].corr(dataArr["Weapon"], method='pearson'))
print("correlation of Relationship and Month", dataArr["Relationship"].corr(dataArr["Month"], method='pearson'))
print("correlation of Relationship and Crime Solved", dataArr["Relationship"].corr(dataArr["Crime Solved"], method='pearson'))



