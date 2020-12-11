#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Library Pandas
import pandas as pd


# In[48]:


#Loading Dataset
raw_df = pd.read_csv('youtube_dataset.csv',encoding='iso-8859-1')
raw_df.head()


# In[56]:


#selecting top 1000 rows
first_1000=raw_df.iloc[:1000]
print(first_1000)


# In[60]:


#CAlculating distribution of channel type
A = raw_df['channeltype'].value_counts()
print(A)


# In[82]:


#Defining function to extract top 1000 rows and show distribution of channel type

def  distribution_channel_type(dataframe, number_of_rows):
     dataframe = dataframe.iloc[:number_of_rows]
     youtube = dataframe['channeltype'].value_counts()
     return youtube
distribution_channel_type(raw_df,1000)


# In[45]:


# Selecting top 1000 rows
Loaded_csv = raw_df.iloc[:1000]
# Converting to csv file
Loaded_csv.to_csv('top1000.csv')


# In[ ]:




