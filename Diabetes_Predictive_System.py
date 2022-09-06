# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:23:09 2022

@author: kevin
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

Diabetes_Dataset = pd.read_csv("C:/Users/kevin/Downloads/DiabetesDataset.csv")
Diabetes_Dataset.head()
Diabetes_Dataset.shape
Diabetes_Dataset.describe()
Diabetes_Dataset['Outcome'].value_counts()
Diabetes_Dataset.groupby('Outcome').mean()

x = Diabetes_Dataset.drop(columns = 'Outcome', axis=1)
y = Diabetes_Dataset['Outcome']
print(x)
print(y)

scaler = StandardScaler()
scaler.fit(x)
Standardized_data = scaler.transform(x)
print(Standardized_data)
x = Standardized_data
y = Diabetes_Dataset['Outcome']
print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, stratify=y, random_state=2)
print(x.shape, x_train.shape, x_test.shape)

classifier = svm.SVC(kernel='linear')
classifier.fit(x_train, y_train)

x_train_prediction = classifier.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)
print('accuracy score of the training data:', training_data_accuracy)

x_test_prediction = classifier.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)
print('accuracy score of the training data:', test_data_accuracy)

input_data = (1,189,60,23,846,30.1,0.398,59)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
std_data = scaler.transform(input_data_reshaped)
print(std_data)
prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0 == 0]):
 print ('the person is not diabetic')
else:
  print('the person is diabetic')




