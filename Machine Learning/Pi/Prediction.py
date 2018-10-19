
# coding: utf-8

# In[ ]:


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

def predict()

    filename_mlp = "Neural_Network_Model.sav"
    filename_rd = "Random_Forestry_Model.sav"
    data = pd.read_csv(r'/home/pi/Desktop/cleaned_dataset.csv')
    
    mlp_model = pickle.load(open(filenameMLP, 'rb'))
    rd_model = pickle.load(open(filenameRD, 'rb'))
    
    prediction_rd = rd_model.predict(data)
    
    # data scaling to improve accuracy of mlp
    scaler = StandardScaler()
    scaler.fit(data)
    
    prediction_mlp = mlp_model.predict(scaler.transform(data))
    
    predictions = prediction_mlp + prediction_rd
    
    mapping = { 1 : 'chicken', 2 : 'number7', 3 : 'sidestep', 4 : 'turnclap', 5 : 'wiper'}
    output = pd.DataFrame({'activity' : predictions})
    output = output.replace({'activity': mapping})   
    b = output.activity.mode()
    myFile = open('output.csv', 'w')  
    with myFile:  
        myFile.write(b[0])

