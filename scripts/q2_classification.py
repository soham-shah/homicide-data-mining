import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import tree
from pprint import pprint

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
    if value != "Acquaintance" and value != "Stranger":
        return "Family"
    return value

dataArr['Relationship'] = dataArr['Relationship'].apply(condition)
# dataArr["Relationship"] = dataArr["Relationship"].map({"Acquaintance":0,"Stranger":1,"Family":2})
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

# Decision Tree Classifier using information gain (entropy)
dt_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth=6, min_samples_leaf=5)
dt_entropy.fit(X_train, y_train)

# Decision Tree Classifier using gini index
dt_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=6, min_samples_leaf=5)
dt_gini.fit(X_train, y_train)

#Now use our entropy decision tree on the test set to do our prediction! "X_test" can be replaced with just one row if we want to predict one scenario
y_pred_entropy = dt_entropy.predict(X_test)
print("Decision Tree prediction using information gain:")
print(y_pred_entropy)

#Now use our gini index decision tree on the test set to do our prediction! 
y_pred_gini = dt_gini.predict(X_test)
print("Decision Tree prediction using gini index:")
print(y_pred_gini)

#Accuracy for info gain prediction
print ("Accuracy for information gain decision tree is ", accuracy_score(y_test,y_pred_entropy)*100)

#Accuracy for info gain prediction
print ("Accuracy for gini decision tree is ", accuracy_score(y_test,y_pred_gini)*100)

#any situation you want to try after traininging and testing
# print("Special sample/situation")
# sample = {'Month': [10], 'Victim Sex': [0],'Victim Age': [72], 'Victim Race': [2],'Weapon': [14]}
# sample_test = pd.DataFrame(sample)
# print(sample_test)
# sample_prediction = dt_entropy.predict(sample_test)
# print("Decision Tree prediction using information gain for special sample:", sample_prediction)

# #confusion matrix for information gain decision tree
# confusion_matrix_entropy = pd.DataFrame(
#     confusion_matrix(y_test, y_pred_entropy),
#     columns=['Predicted Unolved', 'Predicted Solved'],
#     index=['True Unsolved', 'True Solved']
# )
# print("Confusion Matrix for information gain Decision tree:")
# print(confusion_matrix_entropy)

# #confusion matrix for gini index decision tree
# confusion_matrix_gini = pd.DataFrame(
#     confusion_matrix(y_test, y_pred_gini),
#     columns=['Predicted Unolved', 'Predicted Solved'],
#     index=['True Unsolved', 'True Solved']
# )
# print("Confusion Matrix for gini Decision tree:")
# print(confusion_matrix_entropy)

#generates text file for the informationg ain decision tree in which you copy the contents and put into http://webgraphviz.com/ to generate graph of tree
with open("../plots/q2_info_gain_decision_tree.txt", "w") as f:
    f = tree.export_graphviz(dt_entropy, feature_names=x.columns.values,out_file=f)
with open("../plots/q2_info_gain_decision_tree.dot", "w") as f:
    f = tree.export_graphviz(dt_entropy, feature_names=x.columns.values,out_file=f)


#generates text file for the gini index decision tree in which you copy the contents and put into http://webgraphviz.com/ to generate graph of tree
with open("../plots/q2_gini_decision_tree.txt", "w") as f:
    f = tree.export_graphviz(dt_gini, feature_names=x.columns.values,out_file=f)
with open("../plots/q2_gini_decision_tree.dot", "w") as f:
    f = tree.export_graphviz(dt_gini, feature_names=x.columns.values,out_file=f)
print("Done")
