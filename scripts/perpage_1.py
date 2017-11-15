import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question: Can we predict under what situation/conditions is a homicide most likely to be solved?
# This script prints the statistical analysis for the Perpetrator Age

dataArr = pd.read_csv("../data/database.csv")

# remove these columns
dataArr = (dataArr.drop(['Record ID', 'Agency Code','Agency Name','Agency Type','City', 'State', 'Year','Month', 'Incident', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Race', 'Victim Ethnicity', 'Perpetrator Sex', 'Victim Age', 'Perpetrator Race', 'Perpetrator Ethnicity', 'Relationship','Victim Count','Weapon','Perpetrator Count', 'Record Source'],axis=1))

# remove rows where the perps's age is 0 or above 100
dataArr = dataArr[dataArr["Perpetrator Age"] != 0]
dataArr = dataArr[dataArr["Perpetrator Age"] <= 100]

# remove header and replace with "0" for easy print statement
#dataArr.columns = range(dataArr.shape[1])

#find stats
dataObj = np.size(dataArr)
dataMin = np.min(dataArr)
dataMax = np.max(dataArr)
dataMean = np.mean(dataArr)
dataStd = np.std(dataArr)
dataQ1 = np.percentile(dataArr, 25)
dataMedian = np.median(dataArr)
dataQ3 = np.percentile(dataArr, 75)
dataIQR = dataQ3 - dataQ1

# print stats for records
print("Number of Objects: {} \n Min: {} \n Max: {} \n Mean: {} \n Standard Deviation: {} \n Q1: {} \n Median: {} \n Q3: {} \n IQR: {}".format(dataObj, dataMin, dataMax, dataMean, dataStd, dataQ1, dataMedian, dataQ3, dataIQR))

# make boxplot
pd.DataFrame.boxplot(dataArr)

# Note, save your output to the plots folder. name it something 
plt.savefig('../plots/perpage_1.png')
