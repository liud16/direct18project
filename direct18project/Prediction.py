# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:30:47 2018

@author: sarth
"""

import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import utils
from mpl_toolkits.mplot3d import Axes3D

pd.set_option('display.float_format', lambda x: '%.6f' % x)

# Reading the DataFile
df = pd.read_csv('afm_datafile_v3.csv')

# Deciding parametes
test_size = 0.2 # Test size 
k = 5 # Number of nieghbors
weights = 'distance' # uniform or distance based weights for knn

# Concentration is in nM in Original dataset - converting to uM for making better plots
df['concentration'] = df['concentration'] * 1e6 


#------------------------------- NO USER INPUT BELOW THIS --------------------------

# Train-Test split
df_train, df_test = train_test_split(df, test_size = test_size, random_state = 15)

# Converting label type from continous to Multiclass for knn
lab_enc = preprocessing.LabelEncoder()
encoded_ROD = lab_enc.fit_transform(df_train['ROD'])
utils.multiclass.type_of_target(encoded_ROD)

# KNN fit here
knn = KNeighborsClassifier(n_neighbors = k, weights = weights)
knn.fit(df_train[['concentration', 'pH']], encoded_ROD)

# Predicting Ratio of order to disorder (ROD) for test data set
testing_pred = knn.predict(df_test[['concentration', 'pH']])

#Printing the predictions for Ratio of Order to Disorder for Test set 
print (testing_pred)

levels,labels = pd.factorize(df_train.Kind)
y = levels

# Plotting Training data set wrt to concentration, pH and ROD with 'Kind' as color levels
plt.figure(dpi = 300)
ax = Axes3D(plt.gcf())
ax.scatter(df_train.concentration, df_train.pH, df_train.ROD, zdir = 'z', c = y, s = 100, depthshade = False, edgecolor = 'k')
ax.set_xlabel('Peptide Concentration (uM)')
ax.set_ylabel('pH')
ax.set_zlabel('Order-Disorder Ratio')
ax.set_title('Training Data', fontsize = 15)

# Plotting Actual ROD vs Predicted values for specific concentration and pH from KNN for Test data set 
plt.figure(dpi = 300)
ax = Axes3D(plt.gcf())
ax.scatter(df_test.concentration, df_test.pH, testing_pred, zdir = 'z', c = 'r', marker = '*', s = 70, depthshade = False, label = 'Prediction')
ax.scatter(df_test.concentration, df_test.pH, df_test.ROD, zdir = 'z', c = 'b', marker = 'o', s = 100, depthshade = False, label = 'Actual', edgecolor = 'k')
ax.set_xlabel('Peptide Concentration (uM)')
ax.set_ylabel('pH')
ax.set_zlabel('Order-Disorder Ratio')
ax.set_title('Testing Data vs Prediction', fontsize = 15)
ax.legend(loc = 'best')
