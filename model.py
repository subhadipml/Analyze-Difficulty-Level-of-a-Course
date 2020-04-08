'''
Problem : Analyze the difficulty level of a particular course using clustering techniques
Dataset : Bachelor of Computer Applications
'''
#-------------------------------------------------#
# Import all required libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import pickle
#-------------------------------------------------#

# Load the dataset
dataset = pd.read_excel('dataset.xls')

# Print the number of rows and columns
print("The number of rows and columns : ")
print(dataset.shape)

# Print all coulumns name in the dataset
print("All coulumns name in the dataset : ")
print(dataset.columns)

# Remove all the non required columns
dataset = dataset.drop(columns=['Termid', 'Regd No', 'Height', 'Weight', 'ScholarType', 'Direction', 'Gender', 'Medium', 'CourseType', 'ProgramType'])

# Keep all the rows with MHRDName is 'Bachelor of Computer Applications'
dataset = dataset[dataset.MHRDName == 'Bachelor of Computer Applications']

# No need of MHRDName column... as we are already dealing with 'Bachelor of Computer Applications' department
dataset = dataset.drop(columns=['MHRDName'])

# Working with missing data
# Fill all the misiing value i.e. NaN with the mean
dataset = dataset.where(pd.notna(dataset), dataset.mean(), axis='columns')

# Print and Count unique values in column 'Grade' of the dataset
dataset['Grade'].unique(), dataset['Grade'].nunique()

#-----------------------------------------------------------------#
# Convert all the grades of the student to the lavel of difficulty
difficulty_level = []
easy = ['A','A+','O']
medium = ['B+','B','C','D']
difficul = ['E','F','R','M']
for row in dataset.Grade:
    if row in easy:
        difficulty_level.append('Easy')
    elif row in medium:
        difficulty_level.append('Medium')
    else:
        difficulty_level.append('Difficult')
#--------------------------------------------------------------------#

# Now I add a new column i.e. 'Difficulty_Level' to dataset
dataset['Difficulty_Level'] = difficulty_level

# Now no need of the 'Grade' column
dataset = dataset.drop(columns=['Course', 'Grade'])

# Actual shape of the dataset I will work
print("Actual shape of the dataset model will work on : ")
print(dataset.shape)

# Print the column name of the dataset useful for me
print("The column name of the dataset useful for model : ")
print(dataset.columns)

# converting the catrgorical data into numeric form
# 0 means Difficult
# 1 means Easy
# 2 means Medium
le = LabelEncoder()
dataset['Difficulty_Level'] = le.fit_transform(dataset['Difficulty_Level'])

# Plot pairwise relationships in a dataset
#sns.pairplot(dataset)

# Convert dataset to array
dataset = dataset.values

#---------------------------------------------------------#
# Plot the proportion of student with the difficulty level
Difficult = dataset[dataset[:, -1] == 0].shape[0]
Easy = dataset[dataset[:, -1] == 1].shape[0]
Medium = dataset[dataset[:, -1] == 2].shape[0]
plt.bar(10,Difficult,3, label="Difficult")
plt.bar(15,Easy,3, label="Easy")
plt.bar(20,Medium,3, label="Medium")
plt.legend()
plt.ylabel('Number of Student')
plt.title('Proportion of Students')
plt.show()
#-----------------------------------------------------------#

#------------------------------------------#
# Apply K Means Clustering Algorithms
km = KMeans(n_clusters=3)
y_km = km.fit(dataset[:, :-1])

#----------------------------------------#
# Pickling the Model
# To reuse, we can dump the model and load whenever or where-ever you want.
pickle.dump(km, open('km.sav', 'wb'))
#----------------------------------------#

y_km = km.predict(dataset[:, :-1])
# Print the predicted output
print("The predicted output : ")
print(y_km)
# Print the actual output
print("The actual output : ")
print(dataset[:, -1])
acc = accuracy_score(y_km, dataset[:, -1])
# Print the accuracy Score
print("The accuracy Score : ")
print(acc)
#-------------------------------------------#