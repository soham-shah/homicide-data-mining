Homicide Rates Analysis

Team Members
- Soham Shah
- Girish Ramkumar
- Deekshitha Thumma
- Nhi Nguyen

Project
Analyze the Kaggle homicide reports dataset

Questions:
1.Can we predict if a homicide is likely to be solved given the homicide's conditions?
2.Can we predict the relationship between the victim and the perpetrator?
3.Does a homicide get solved easier if the victim count and/or perpetrator count is more than one?
4.Is there a correlation between homicide and time of year, location?

Within Scripts Folder:

* "avg_deaths.py" calculates the distribution of homicides per state
    
    *Output: Graph of total homicides submitted per state for a certain selection of years

* "homicides_per_month_state.py" calculates the average number of homicide cases reported
   
   *Output: Graph of average number of homicide cases reported for a selection of states and years  

* "month_1.py" calculates and plots a histogram of distribution of homicides per month from 1980-2014 in order of frequency  
   
   *Output: "month_2.png" in plots folder and Prints out distribution numbers

* "most_homicides.py" calculates the distribution of homicides per state from 2010-2014 adjusted for population (every 10k people)
   
   *Output: Bar chart of rate of homicides submitted per 10,000 people for every state from 2010-2014

* "perpage_1.py" calculates  and plots a histogram of the distribution of the attribute Perpetrator Age
   
   *Output: "perpage.png" in plots folder and Prints out distribution numbers 

* "perpsex_1.py" calculates and plots a histogram of distribution of the attribute Perpetrator Sex
   
   *Output: "perpsex_1.png" in plots folder and Prints out distribution numbers

* "q1_classification.py" creates two decision trees, one using information gain and one using gini index using the attributes Month, Victim Age, Victim Sex, Victim Race, Weapon, and Crime Solved. It then exports the dot file for drawing the tree and draws the tree.
   
   *Output: "gini_decision_tree.dot", "gini_decision_tree.txt", "gini_decision_tree.png", "info_gain_decision_tree.dot", "info_gain_decision_tree.txt", "info_gain_decision_tree.png" in plots folder

* "q2_all.py" _____
   
   *Output: ____

* "q2_bayes.py" _____
   
   *Output: ____

* "q2_classification.py" _____
   
   *Output: ____

* "q2_correlation.py" _____
   
   *Output: ____

* "q2_relationship_1.py" _____
   
   *Output: ____

* "q2_relationship_2.py" _____
   
   *Output: ____

* "q2_relationship_3.py" _____
   
   *Output: ____

* "q3_basic.py" calculates and plots a histogram of ____
   
   *Output: "vic_perp_count_1.png" in plots folder

* "q3_classification.py" uses Bayes _____  and prints the _____ 
   
   *Output: Prints out ____

* "q3_correlation.py" finds the correlation between the attributes Victim Count and Perpetrator Count
   
   *Output: Prints out _____

* "relationship_1.py" calculates and plots a histogram of the distribution of the attribute Relationship
   
   *Output: "relationship_1.png" in plots folder

* "solved_1.py" calculates and plots a histogram of distribution of the attribute Crime Solved
   
   *Output: "solved_1.png" in plots folder and Prints out distribution numbers

* "time_1.py" calculates and plots a histogram of distribution of homicides per month from 1980-2014 in order of time
   
   *Output: "month_2.png" in plots folder

* "perpsex_1.py" calculates and plots a histogram of distribution of the attribute Perpetrator Sex
   
   *Output: "perpsex_1.png" in plots folder and Prints out distribution numbers

* "victimage_1.py" calculates and plots a histogram of distribution of the attribute Victim Age
   
   *Output: "victimage_1.png" in plots folder and Prints out distribution numbers

* "victimrace_1.py" calculates and plots a histogram of distribution of the attribute Victim Race
   
   *Output: "victimrace_1.png" in plots folder and Prints out distribution numbers

* "victimsex_1.py" calculates and plots a histogram of distribution of the attribute Victim Sex
   
   *Output: "victimsex_1.png" in plots folder and Prints out distribution numbers

* "weapon_1.py" calculates and plots a histogram of distribution of the attribute Weapon
   
   *Output: "weapon_1.png" in plots folder and Prints out distribution numbers


Within Plots Folder:
All the plots that ours scripts export or cropped plots

Within Data Folder:
Kaggle homicide dataset
US Census Bureau dataset
