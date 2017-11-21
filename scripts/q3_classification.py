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
num_solv = dataArr["Crime Solved"].value_counts() #breakdown by solved or not
num_vic = dataArr["Victim Count"].value_counts() #breakdown by num of vic
num_perp = dataArr["Perpetrator Count"].value_counts() #breakdown by num of perps

#------------Bayes Analysis- variables to use to solve---------#
solved = num_solv[0]
not_solved = num_solv[1]
total = dataArr["Victim Count"].count()
one_vic = num_vic[1]
one_perp = num_perp[1]
rest_vic = total - one_vic
rest_perp = total - one_perp


one_vic_solved = dataArr[(dataArr["Victim Count"]==1) & (dataArr["Crime Solved"]=="Yes")].count()
one_vic_not_solved = dataArr[(dataArr["Victim Count"]==1) & (dataArr["Crime Solved"]=="No")].count()
rest_vic_solved = dataArr[(dataArr["Victim Count"]!=1) & (dataArr["Crime Solved"]=="Yes")].count()
rest_vic_not_solved = dataArr[(dataArr["Victim Count"]!=1) & (dataArr["Crime Solved"]=="No")].count()

one_perp_solved = dataArr[(dataArr["Perpetrator Count"]==1) & (dataArr["Crime Solved"]=="Yes")].count()
one_perp_not_solved = dataArr[(dataArr["Perpetrator Count"]==1) & (dataArr["Crime Solved"]=="No")].count()
rest_perp_solved = dataArr[(dataArr["Perpetrator Count"]!=1) & (dataArr["Crime Solved"]=="Yes")].count()
rest_perp_not_solved = dataArr[(dataArr["Perpetrator Count"]!=1) & (dataArr["Crime Solved"]=="No")].count()
# ----------------------------------------------------------------------------

#BAYES: Classes- C1: solved, C2: not solved. X=(1 Victim, 1 Perp)---------------
# P(crime solved = "yes")
P_solved_yes = float(solved)/total
# P(crime solved = "no")
P_solved_no = float(not_solved)/total
# P(victim count = 1|crime solved = "yes")
P_1_vic_solved_yes = float(one_vic_solved[0])/solved
# P(victim count = 1|crime solved = "no")
P_1_vic_solved_no = float(one_vic_not_solved[0])/not_solved
# P(perp count = 1|crime solved = "yes")
P_1_perp_solved_yes = float(one_perp_solved[0])/solved
# P(perp count = 1|crime solved = "no")
P_1_perp_solved_no = float(one_perp_not_solved[0])/not_solved
# P(X|crime solved = "yes")
P1Yes = P_1_vic_solved_yes * P_1_perp_solved_yes * P_solved_yes
# P(X|crime solved = "no")
P1No = P_1_vic_solved_no * P_1_perp_solved_no * P_solved_no

print P1Yes
print P1No
# ----------------------------------------------------------------------------

#BAYES: Classes- C1: solved, C2: not solved. X=(!1 Victim, !2 Perp)---------------
# P(crime solved = "yes")
P_solved_yes = float(solved)/total
# P(crime solved = "no")
P_solved_no = float(not_solved)/total
# P(victim count = 1|crime solved = "yes")
P_rest_vic_solved_yes = float(rest_vic_solved[0])/solved
# P(victim count = 1|crime solved = "no")
P_rest_vic_solved_no = float(rest_vic_not_solved[0])/not_solved
# P(perp count = 1|crime solved = "yes")
P_rest_perp_solved_yes = float(rest_perp_solved[0])/solved
# P(perp count = 1|crime solved = "no")
P_rest_perp_solved_no = float(rest_perp_not_solved[0])/not_solved
# P(X|crime solved = "yes")
PrestYes = P_rest_vic_solved_yes * P_rest_perp_solved_yes * P_solved_yes
# P(X|crime solved = "no")
PrestNo = P_rest_vic_solved_no * P_rest_perp_solved_no * P_solved_no

print PrestYes
print PrestNo
# ----------------------------------------------------------------------------
