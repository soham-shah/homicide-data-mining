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

#------------Correlation Analysis---------#
solved = num_solv[0]
not_solved = num_solv[1]
total = dataArr["Victim Count"].count()
one_vic = num_vic[1]
rest_vic = total - one_vic
one_perp = num_perp[1]
rest_perp = total - one_perp
two_vic = num_vic[2]
rest2_vic = total - two_vic
two_perp = num_perp[2]
rest2_perp = total - two_perp
#print solved
#print total
#print two_vic
#print rest2_vic
# ----------------------------------------------------------------------------

#LIFT:1 Victim or 1 Perp-------------------------------------------------------
#VICTIMS- Lift
#returns full data array, only need first obj
one_vic_solved = dataArr[(dataArr["Victim Count"]==1) & (dataArr["Crime Solved"]=="Yes")].count()
one_vic_not_solved = dataArr[(dataArr["Victim Count"]==1) & (dataArr["Crime Solved"]=="No")].count()
rest_vic_solved = dataArr[(dataArr["Victim Count"]!=1) & (dataArr["Crime Solved"]=="Yes")].count()
rest_vic_not_solved = dataArr[(dataArr["Victim Count"]!=1) & (dataArr["Crime Solved"]=="No")].count()
# print one_vic_solved[0]
# print one_vic_not_solved[0]
# print rest_vic_solved[0]
# print rest_vic_not_solved[0]

#PERPS- Lift
one_perp_solved = dataArr[(dataArr["Perpetrator Count"]==1) & (dataArr["Crime Solved"]=="Yes")].count()
one_perp_not_solved = dataArr[(dataArr["Perpetrator Count"]==1) & (dataArr["Crime Solved"]=="No")].count()
rest_perp_solved = dataArr[(dataArr["Perpetrator Count"]!=1) & (dataArr["Crime Solved"]=="Yes")].count()
rest_perp_not_solved = dataArr[(dataArr["Perpetrator Count"]!=1) & (dataArr["Crime Solved"]=="No")].count()
# print one_perp_solved[0]
# print one_perp_not_solved[0]
# print rest_perp_solved[0]
# print rest_perp_not_solved[0]
lift_one_perp_solved = (float(one_perp_solved[0])/total)/((float(solved)/total)*(float(one_perp)/total))
lift_one_perp_not_solved = (float(one_perp_not_solved[0])/total)/((float(not_solved)/total)*(float(one_perp)/total))
lift_rest_perp_solved = (float(rest_perp_solved[0])/total)/((float(solved)/total)*(float(rest_perp)/total))
lift_rest_perp_not_solved = (float(rest_perp_not_solved[0])/total)/((float(not_solved)/total)*(float(rest_perp)/total))
# print lift_one_perp_solved
# print lift_one_perp_not_solved
# print lift_rest_perp_solved
# print lift_rest_perp_not_solved
# ----------------------------------------------------------------------------

# LIFT:2 Victim or 2 Perp-------------------------------------------------------
# VICTIMS- Lift
#returns full data array, only need first obj
two_vic_solved = dataArr[(dataArr["Victim Count"]==2) & (dataArr["Crime Solved"]=="Yes")].count()
two_vic_not_solved = dataArr[(dataArr["Victim Count"]==2) & (dataArr["Crime Solved"]=="No")].count()
rest2_vic_solved = dataArr[(dataArr["Victim Count"]!=2) & (dataArr["Crime Solved"]=="Yes")].count()
rest2_vic_not_solved = dataArr[(dataArr["Victim Count"]!=2) & (dataArr["Crime Solved"]=="No")].count()
# print two_vic_solved[0]
# print two_vic_not_solved[0]
# print rest2_vic_solved[0]
# print rest2_vic_not_solved[0]
lift_two_vic_solved = (float(two_vic_solved[0])/total)/((float(solved)/total)*(float(two_vic)/total))
lift_two_vic_not_solved = (float(two_vic_not_solved[0])/total)/((float(not_solved)/total)*(float(two_vic)/total))
lift_rest2_vic_solved = (float(rest2_vic_solved[0])/total)/((float(solved)/total)*(float(rest2_vic)/total))
lift_rest2_vic_not_solved = (float(rest2_vic_not_solved[0])/total)/((float(not_solved)/total)*(float(rest2_vic)/total))
# print lift_two_vic_solved
# print lift_two_vic_not_solved
# print lift_rest2_vic_solved
# print lift_rest2_vic_not_solved
# ---------------------------------------------------------------------------

#CHI:1 Victim-----------------------------------------------------------------
#VICTIM- Chi
# e_one_solved = float(one_vic)*solved/total
# print e_one_solved
# e_one_not_solved = float(one_vic)*not_solved/total
# print e_one_not_solved
# e_rest_solved = float(rest_vic)*solved/total
# print e_rest_solved
# e_rest_not_solved = float(rest_vic)*not_solved/total
# print e_rest_not_solved
#
# chi_vic = (one_vic_solved[0]-e_one_solved)*(one_vic_solved[0]-e_one_solved)/e_one_solved +(one_vic_not_solved[0]-e_one_not_solved)*(one_vic_not_solved[0]-e_one_not_solved)/e_one_not_solved +(rest_vic_solved[0]-e_rest_solved)*(rest_vic_solved[0]-e_rest_solved)/e_rest_solved+(rest_vic_not_solved[0]-e_rest_not_solved)*(rest_vic_not_solved[0]-e_rest_not_solved)/e_rest_not_solved
# print chi_vic
# ---------------------------------------------------------------------------
