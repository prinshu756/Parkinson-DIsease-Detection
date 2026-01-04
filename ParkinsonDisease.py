import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import time

#Data loading

data = pd.read_csv('Parkinsson disease.csv')
plt.figure(figsize=(13 , 12))
data['status'].value_counts().plot(kind='bar')
plt.title('Distribution of Parkinson\'s Disease Status')
plt.xlabel('Status (0: No PD, 1: PD)')
plt.ylabel('Count')
plt.show()