
# coding: utf-8

# In[8]:


# data analysis
import pandas as pd

class DataProcessing ():

    def processData(cleaned_data):
        mean_data = pd.DataFrame()
        std_data = pd.DataFrame()
        i = 0
        j = 49
        row_count = len(cleaned_data.index)

        # segmentation at 50%
        while row_count > 1:
            a = cleaned_data[i:i+100:].copy()
            b = cleaned_data[j:j+100:].copy()

            a.loc['mean'] = a.mean()
            a.loc['std'] = a.std()
            b.loc['mean'] = b.mean()
            b.loc['std'] = b.std()
            mean_data = mean_data.append(a.loc['mean'], ignore_index = True)
            mean_data = mean_data.append(b.loc['mean'], ignore_index = True)
            std_data = std_data.append(a.loc['std'], ignore_index = True)
            std_data = std_data.append(b.loc['std'], ignore_index = True)

            i += 100
            j += 100
            row_count -= 100

        mean_data.activity = mean_data.activity.round()
        # rearrangement of columns
        mean_data = mean_data.rename(index=str, columns={'acceleration_x': 'mean_acc_x', 'acceleration_y': 'mean_acc_y',
                                                         'acceleration_z': 'mean_acc_z', 'gyro_x': 'mean_gyro_x',
                                                         'gyro_y': 'mean_gyro_y', 'gyro_z': 'mean_gyro_z'})

        std_data = std_data.rename(index=str, columns={'acceleration_x': 'std_acc_x', 'acceleration_y': 'std_acc_y',
                                                         'acceleration_z': 'std_acc_z', 'gyro_x': 'std_gyro_x',
                                                         'gyro_y': 'std_gyro_y', 'gyro_z': 'std_gyro_z'})
        # combine features extracted into 1 
        activity = mean_data['activity'].copy()
        mean_data = mean_data.drop(['activity'], axis = 1)
        std_data = std_data.drop(['activity'], axis = 1)
        extracted_data = mean_data.join(std_data)
        extracted_data['activity'] = activity
        return extracted_data

