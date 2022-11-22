#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install matplotlib


# In[7]:


pip install seaborn


# In[94]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.show()


# In[95]:


diabetic_df = pd.read_csv('diabetic_data.csv')
diabetic_df.head()


# In[96]:


#using boxplot to compare Gender to Amount of Time Spent in the Hospital
#additionally considering race within each gender group  
sns.boxplot(x='gender', y='time_in_hospital', data=diabetic_df, hue='race', palette='dark') #hue adds the additonal variable. palette changes the color scheme
plt.title('Time Spent in Hospital Compared to Gender and Race')
plt.xlabel('Gender')
plt.ylabel('Time Spent in Hospital')
plt.plot()
plt.show()


# In[97]:


#using a histogram to understand how many patients fall into each A1C result category 
#no legend needed because there is a single variable/color
diabetes_race_df = diabetic_df.sort_values(by='A1Cresult')
plt.hist(diabetes_race_df['A1Cresult'], bins=25, align='mid', color='#330000') #change bin number and alignment to best fit bars
plt.xlabel("A1Cresult")
plt.ylabel("Number of Patients")
plt.title("Number of Patients Per Reported Race")
plt.plot()
plt.show()


# In[98]:


# using a lineplot to compare Number of Patients in Emergency compared to each Age Range
# additionally including comparisons between each race in the dataset
sns.lineplot(data=diabetic_df, x='age', y='number_emergency', hue='race', linewidth=.5, marker='o') 
plt.title('Age vs Number of Emergencies')
plt.xlabel('Age Ranges')
plt.ylabel('Number of Patients in Emergency')
plt.plot()
plt.show()


# In[99]:


#using a violoinplot to compare Diabetes Diagnosis alongside the number of medications a patient is taking
#additionally considering metformin, one of the more well known diabetes medications, to visualize the trt option
#overall includes densities at various y value ranges, in this circumstance, the number of medications

sns.violinplot(x='diabetesMed', y='num_medications',data=diabetic_df, color='#330000', hue='metformin')
plt.title('Comparison of the Number of Medications a Diabetic vs Non-Diabetic Patient Takes')
plt.xlabel('Diabetes Diagnosis')
plt.ylabel('Number of Medications')
plt.plot()
plt.show()


# In[ ]:




