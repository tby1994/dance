
# coding: utf-8

# In[80]:


# scale the data points
from sklearn.preprocessing import StandardScaler 

# Neural Network model
from sklearn.neural_network import MLPClassifier

# Importation of  model
import pickle

# data analysis
import pandas as pd

# scale the data points
from sklearn.preprocessing import StandardScaler 

import csv

def predict():

    filename_mlp = "Neural_Network_Model.sav"
    filename_svm = "SVM.sav"
    filename_rd = "RD.sav"
#     data = pd.read_csv(r'/home/pi/3002/main/test_dataset.csv')
    data = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\extracted data\test_dataset.csv')
    
    mlp_model = pickle.load(open(filename_mlp, 'rb'))
    svm_model = pickle.load(open(filename_svm, 'rb'))
    rd_model = pickle.load(open(filename_rd, 'rb'))
    
    prediction_mlp = mlp_model.predict(data).tolist()
    prediction_svm = svm_model.predict(data).tolist()
    prediction_rd = rd_model.predict(data).tolist()
    predictions = prediction_mlp + prediction_svm + prediction_rd
    
    mapping = { 1 : 'chicken', 2 : 'number7', 3 : 'sidestep', 4 : 'turnclap', 5 : 'wiper'}
    output = pd.DataFrame({'activity' : predictions})
    output = output.replace({'activity': mapping})
    
    b = output.activity.mode()
    return b[0]

