
# coding: utf-8

# In[4]:


# data analysis
import pandas as pd

# Neural Network model
from sklearn.neural_network import MLPClassifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# split train and test data
from sklearn.model_selection import train_test_split

# scale the data points
from sklearn.preprocessing import StandardScaler 

# Exportation of  model
import pickle

# Evalute the speed of model
import datetime

import random

# read data
data = pd.read_csv(r'/home/pi/Desktop/cleaned_dataset.csv')
#data = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\cleaned_dataset.csv')

filenameMLP = "Neural_Network_Finalized_Model.sav"
filenameSVC = "SUpport_Vector_Machines_Model.sav"
filenameRD = "Random_Forestry_Model.sav"
filenameDT = "Decision_Tree_Model.sav"

X = data.drop(['activity'], axis = 1)
y = data['activity']
X1 = X
y1 = y

test_data_ratio = random.random()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_data_ratio)
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size = test_data_ratio)

scaler = StandardScaler()
scaler.fit(X_test)
X_test = scaler.transform(X_test)

mlp_model = pickle.load(open(filenameMLP, 'rb'))
svc_model = pickle.load(open(filenameSVC, 'rb'))
rd_model = pickle.load(open(filenameRD, 'rb'))
dt_model = pickle.load(open(filenameDT, 'rb'))

print("The amount of test data: ", int(len(data.index) * test_data_ratio))

a = datetime.datetime.now()
print("The testing accuracy for imported Neural Network is ", mlp_model.score(X_test, y_test))
b = datetime.datetime.now()
c = b - a
print("time taken for Neural Network = ", c)

a = datetime.datetime.now()
print("The testing accuracy for imported Support Vector Machines is ", svc_model.score(X1_test, y1_test))
b = datetime.datetime.now()
c = b - a
print("time taken for Support Vector Machines = ", c)

a = datetime.datetime.now()
print("The testing accuracy for imported Random Forestry is ", rd_model.score(X1_test, y1_test))
b = datetime.datetime.now()
c = b - a
print("time taken for Random Forestry = ", c)

a = datetime.datetime.now()
print("The testing accuracy for imported Decision Tree is ", dt_model.score(X1_test, y1_test))
b = datetime.datetime.now()
c = b - a
print("time taken for Decision Tree = ", c)


print(data.head())

