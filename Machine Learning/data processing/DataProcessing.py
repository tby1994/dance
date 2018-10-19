
# coding: utf-8

# In[94]:


# data analysis
import pandas as pd

def DataProcessing():
    # read data
    cleaned_data = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\dataset.csv')

    mean_data = pd.DataFrame()
    std_data = pd.DataFrame()
    i = 0
    j = 54
    row_count = len(cleaned_data.index)

    # segmentation at 50% @ 55Hz 2s
    while row_count > 1:
        a = cleaned_data[i:i+110:].copy()
        b = cleaned_data[j:j+110:].copy()

        a.loc['mean'] = a.mean()
        a.loc['std'] = a.std()
        b.loc['mean'] = b.mean()
        b.loc['std'] = b.std()
        mean_data = mean_data.append(a.loc['mean'], ignore_index = True)
        mean_data = mean_data.append(b.loc['mean'], ignore_index = True)
        std_data = std_data.append(a.loc['std'], ignore_index = True)
        std_data = std_data.append(b.loc['std'], ignore_index = True)

        i += 110
        j += 110
        row_count -= 110

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
    # combine features extracted into 1 
    activity = mean_data['activity'].copy()
    mean_data = mean_data.drop(['activity'], axis = 1)
    std_data = std_data.drop(['activity'], axis = 1)
    extracted_data = mean_data.join(std_data)
    extracted_data['activity'] = activity

    extracted_data.to_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\extracted_dataset.csv',index=False)

#DataProcessing()
print("done")

'''
# In[75]:


bobby_chicken = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\bobby\chicken.csv')
bobby_number7 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\bobby\number7.csv')
bobby_sidestep = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\bobby\sidestep.csv')
bobby_turnclap = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\bobby\turnclap.csv')
bobby_turnclap2 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\bobby\turnclap2.csv')
bobby_wiper = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\bobby\wiper.csv')

beeyee_chicken = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\beeyee\chicken.csv')
beeyee_number7 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\beeyee\number7.csv')
beeyee_sidestep = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\beeyee\sidestep.csv')
beeyee_turnclap = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\beeyee\turnclap.csv')
beeyee_turnclap2 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\beeyee\turnclap2.csv')
beeyee_wiper = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\beeyee\wiper.csv')

henry_chicken = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\henry\chicken.csv')
henry_number7 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\henry\number7.csv')
henry_sidestep = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\henry\sidestep.csv')
henry_turnclap = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\henry\turnclap.csv')
henry_turnclap2 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\henry\turnclap2.csv')
henry_turnclap3 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\henry\turnclap3.csv')
henry_turnclap4 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\henry\turnclap4.csv')
henry_wiper = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\henry\wiper.csv')

kabir_chicken = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\kabir\chicken.csv')
kabir_number7 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\kabir\number7.csv')
kabir_sidestep = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\kabir\sidestep.csv')
kabir_turnclap = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\kabir\turnclap.csv')
kabir_turnclap2 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\kabir\turnclap2.csv')
kabir_wiper = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\kabir\wiper.csv')

zech_chicken = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\zech\chicken.csv')
zech_number7 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\zech\number7.csv')
zech_sidestep = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\zech\sidestep.csv')
zech_turnclap = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\zech\turnclap.csv')
zech_turnclap2 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\zech\turnclap2.csv')
zech_wiper = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\zech\wiper.csv')

hongjing_chicken = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\hongjing\chicken.csv')
hongjing_number7 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\hongjing\number7.csv')
hongjing_sidestep = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\hongjing\sidestep.csv')
hongjing_wiper = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\hongjing\wiper.csv')

# bobby_chicken = bobby_chicken.drop(['voltage', 'current', 'power', 'energy'], axis = 1).copy();
# bobby_number7 = bobby_number7.drop(['voltage', 'current', 'power', 'energy'], axis = 1).copy();

frames_chicken = [bobby_chicken, beeyee_chicken, henry_chicken, kabir_chicken, zech_chicken, hongjing_chicken]
frames_number7 = [bobby_number7, beeyee_number7, henry_chicken, kabir_number7, zech_number7, hongjing_number7]
frames_sidestep = [bobby_sidestep, beeyee_sidestep, henry_sidestep, kabir_sidestep, zech_sidestep, hongjing_sidestep]
frames_turnclap = [bobby_turnclap, bobby_turnclap2, beeyee_turnclap, beeyee_turnclap2, henry_turnclap,
                   henry_turnclap2, henry_turnclap3, henry_turnclap4, zech_turnclap, zech_turnclap2,]
frames_wiper = [bobby_wiper, beeyee_wiper, henry_wiper, kabir_wiper, zech_wiper, hongjing_wiper]

chicken_data = pd.concat(frames_chicken)
number7_data = pd.concat(frames_number7)
sidestep_data = pd.concat(frames_sidestep)
turnclap_data = pd.concat(frames_turnclap)
wiper_data = pd.concat(frames_wiper)

chicken_data['activity'] = 1;
number7_data['activity'] = 2;
sidestep_data['activity'] = 3;
turnclap_data['activity'] = 4;
wiper_data['activity'] = 5;

frames_result = [chicken_data, number7_data, sidestep_data, turnclap_data, wiper_data]

result = pd.concat(frames_result)

result = result.drop(['voltage', 'current', 'power', 'energy'], axis = 1).copy()

mapping = {'chicken': 1, 'number7': 2, 'sidestep' : 3, 'turnclap' : 4, 'wiper' : 5}

print('done')

result.to_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\dataset.csv', index=False)


# In[65]:


extracted_data = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\chicken_extracted_dataset.csv')

cleaned_data = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\dataset.csv')

extracted_data


# In[74]:


chicken = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\chicken_extracted_dataset.csv')
number7 = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\number7_extracted_dataset.csv')
sidestep = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\sidestep_extracted_dataset.csv')
turnclap = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\turnclap_extracted_dataset.csv')
wiper = pd.read_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\wiper_extracted_dataset.csv')


frames_result = [chicken_data, number7_data, sidestep_data, turnclap_data, wiper_data]

result = pd.concat(frames_result)
result.to_csv(r'C:\Users\User\Desktop\Study\Year 3\Sem 1\CG3002\DanceProject\Machine Learning\raw data\dataset.csv', index=False)
print("done")
'''
