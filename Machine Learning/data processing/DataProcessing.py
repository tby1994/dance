
# coding: utf-8

# In[8]:


# data analysis
import pandas as pd

from sklearn import preprocessing

# data segmentation: 2 second, 80% overlapping, 55Hz
def data_processing(filename):
    # read data
    cleaned_data = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\%s_dataset.csv' %filename)
    activity = cleaned_data['activity'].copy()
    cleaned_data = pd.DataFrame(preprocessing.scale(cleaned_data.drop(['activity', 'voltage', 'current', 'power', 'energy'], 
                                                                      axis=1)),
                                                   columns=['AcX 1', 'AcY 1', 'AcZ 1', 'GyX 1', 'GyY 1', 'GyZ 1', 
                                                            'AcX 2', 'AcY 2', 'AcZ 2', 'GyX 2', 'GyY 2', 'GyZ 2',
                                                            'AcX 3', 'AcY 3', 'AcZ 3', 'GyX 3', 'GyY 3', 'GyZ 3'])
    
    cleaned_data['activity'] = activity
    mean_data = pd.DataFrame()
    std_data = pd.DataFrame()
    var_data = pd.DataFrame()
    i = 0
    row_count = len(cleaned_data.index)

    # segmentation at 80% @ 55Hz 2s
    while i + 110 <=  row_count:
        a = cleaned_data[i:i+110:].copy()

        a.loc['mean'] = a.mean()
        a.loc['std'] = a.std()
        a.loc['var'] = a.var()
        mean_data = mean_data.append(a.loc['mean'], ignore_index=True)
        std_data = std_data.append(a.loc['std'], ignore_index=True)
#        var_data = var_data.append(a.loc['var'], ignore_index=True)
        i += 21
    mean_data.activity = mean_data.activity.round()
    # rearrangement of columns
    mean_data = mean_data.rename(index=str, columns={'AcX 1': 'mean_AcX 1', 'AcY 1': 'mean_AcY 1', 'AcZ 1': 'mean_AcZ 1', 
                                                      'GyX 1': 'mean_GyX 1', 'GyY 1': 'mean_GyY 1', 'GyZ 1': 'mean_GyZ 1',
                                                      'AcX 2': 'mean_AcX 2', 'AcY 2': 'mean_AcY 2', 'AcZ 2': 'mean_AcZ 2', 
                                                      'GyX 2': 'mean_GyX 2', 'GyY 2': 'mean_GyY 2', 'GyZ 2': 'mean_GyZ 2',
                                                      'AcX 3': 'mean_AcX 3', 'AcY 3': 'mean_AcY 3', 'AcZ 3': 'mean_AcZ 3', 
                                                      'GyX 3': 'mean_GyX 3', 'GyY 3': 'mean_GyY 3', 'GyZ 3': 'mean_GyZ 3',})

    std_data = std_data.rename(index=str, columns=  {'AcX 1': 'std_AcX 1', 'AcY 1': 'std_AcY 1', 'AcZ 1': 'std_AcZ 1', 
                                                     'GyX 1': 'std_GyX 1', 'GyY 1': 'std_GyY 1', 'GyZ 1': 'std_GyZ 1',
                                                     'AcX 2': 'std_AcX 2', 'AcY 2': 'std_AcY 2', 'AcZ 2': 'std_AcZ 2', 
                                                     'GyX 2': 'std_GyX 2', 'GyY 2': 'std_GyY 2', 'GyZ 2': 'std_GyZ 2',
                                                     'AcX 3': 'std_AcX 3', 'AcY 3': 'std_AcY 3', 'AcZ 3': 'std_AcZ 3', 
                                                     'GyX 3': 'std_GyX 3', 'GyY 3': 'std_GyY 3', 'GyZ 3': 'std_GyZ 3',})
    
#     var_data = var_data.rename(index=str, columns=  {'AcX 1': 'var_AcX 1', 'AcY 1': 'var_AcY 1', 'AcZ 1': 'var_AcZ 1', 
#                                                      'GyX 1': 'var_GyX 1', 'GyY 1': 'var_GyY 1', 'GyZ 1': 'var_GyZ 1',
#                                                      'AcX 2': 'var_AcX 2', 'AcY 2': 'var_AcY 2', 'AcZ 2': 'var_AcZ 2', 
#                                                      'GyX 2': 'var_GyX 2', 'GyY 2': 'var_GyY 2', 'GyZ 2': 'var_GyZ 2',
#                                                      'AcX 3': 'var_AcX 3', 'AcY 3': 'var_AcY 3', 'AcZ 3': 'var_AcZ 3', 
#                                                      'GyX 3': 'var_GyX 3', 'GyY 3': 'var_GyY 3', 'GyZ 3': 'var_GyZ 3',})   
    # combine features extracted into 1 
    activity = mean_data['activity'].copy()
    mean_data = mean_data.drop(['activity'], axis=1)
    std_data = std_data.drop(['activity'], axis=1)
#     var_data = var_data.drop(['activity'], axis=1)
#     extracted_data = mean_data.join(std_data).join(var_data)
    extracted_data = mean_data.join(std_data)
    extracted_data['activity'] = activity
    
    extracted_data.to_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\extracted data\%s_extracted_dataset.csv' %filename,index=False)
    

