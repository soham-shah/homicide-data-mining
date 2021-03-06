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

'''x1 = dataArr["Victim Age"]
x2 = dataArr["Victim Sex"]
x3 = dataArr["Perpetrator Age"]
x4 = dataArr["Perpetrator Sex"]
x5 = dataArr["Weapon"]
y = dataArr["Crime Solved"]'''

#X is array of attributes (Victim Age, Victim Sex, Perp Age, Perp Sex, Y is class label
x = (dataArr.drop(['Relationship'],axis=1))
y = dataArr["Relationship"]

#Split into training set and testing set (test set is 30% whole set, training set is 70%)
X_train, X_test, y_train, y_test = train_test_split( x, y, test_size = 0.3, random_state = 100)


rf_probas = RandomForestClassifier().fit(X_train, y_train).predict_proba(X_test)
lr_probas = LogisticRegression().fit(X_train, y_train).predict_proba(X_test)
nb_probas = GaussianNB().fit(X_train, y_train).predict_proba(X_test)
sv_scores = LinearSVC().fit(X_train, y_train).decision_function(X_test)

probas_list = [rf_probas, lr_probas, nb_probas, sv_scores]
clf_names=['Random Forest',
           'Logistic Regression',
           'Gaussian Naive Bayes',
           'Support Vector Machine']

skplt.metrics.plot_calibration_curve(y_test,
                                     probas_list=probas_list,
                                     clf_names=clf_names,
                                     n_bins=10)
# plt.show()
plt.savefig('../plots/q2_allComp.png')