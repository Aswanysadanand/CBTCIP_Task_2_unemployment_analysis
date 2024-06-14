#!/usr/bin/env python
# coding: utf-8

# CIPHERBYTE TECHNOLOGIES DATA SCIENCE INTERNSHIP

# MAY - JUNE 2024

# TASK 2

# UNEMPLOYMENT ANALYSIS WITH PYTHON

# #importing necessary libraries

# In[16]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# #loading datasets

# In[17]:


df=pd.read_excel("Downloads/Unemployment_in_india.xlsx")


# In[18]:


df


# #checking sum of null values

# In[19]:


df.isnull().sum()


# In[20]:


# Separate categorical and numerical columns
categorical_columns = df.select_dtypes(include=['object', 'category']).columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Print the lists of categorical and numerical columns
print("Categorical columns:", categorical_columns)
print("Numerical columns:", numerical_columns)


# #Extract month from date column

# In[21]:


# Convert the 'date_column' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month and create a new column 'month'
df['month'] = df['Date'].dt.month


# In[22]:


#removing unwanted columns


# In[23]:


cols_to_drop=['Date','Frequency']


# In[24]:


df.drop(cols_to_drop,axis=1,inplace=True)


# In[25]:


from sklearn.preprocessing import LabelEncoder


# In[26]:


encoder = LabelEncoder()

# Fit and transform the 'Location_Type' column
df['Area'] = encoder.fit_transform(df['Area'])


# In[27]:


df['month']=encoder.fit_transform(df['month'])


# 0 for rural
# 1 for urban

# 

# #renaming columns

# In[37]:


df.rename(columns={'Estimated Unemployment Rate (%)': 'estimated_unemployment_rate', 'Estimated Labour Participation Rate (%)': 'estimated_labour_participation_rate','Estimated Employed':'estimated_employed'}, inplace=True)


# In[38]:


df


# In[29]:


#data analysis


# #Distribution of Estimated unemployment Rate by State

# In[40]:


plt.figure(figsize=(10, 6))
sns.boxplot(y='Region', x='estimated_unemployment_rate', data=df)
plt.ylabel('Region')
plt.xlabel('estimated_unemployment_rate(%)')
plt.title('Distribution of Estimated unemployment Rate by State')
plt.show()


# #Count of Estimated employed by Region

# In[67]:


plt.figure(figsize=(10, 6))
sns.countplot(y='Region', data=df)
plt.ylabel('Region')
plt.xlabel('estimated_employed')
plt.title('Count of Estimated employed by Region')
plt.show()


# #Count of Estimated Employed by month

# In[57]:


plt.figure(figsize=(10, 6))
sns.countplot(x='month', data=df)
plt.xlabel('month')
plt.ylabel('estimated_employed')
plt.title('Count of Estimated Employed by month')
plt.show()


# #Distribution of Estimated Labour Participation Rate by State

# In[54]:


# Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(y='Region', x='estimated_labour_participation_rate', data=df)
plt.ylabel('Region')
plt.xlabel('estimated_labour_participation_rate')
plt.title('Distribution of Estimated Labour Participation Rate by State')
plt.show()


# In[ ]:


#Distribution of month by Region


# In[66]:


plt.figure(figsize=(10, 6))
sns.countplot(x='Region', data=df)
plt.xlabel('Region')
plt.ylabel('month')
plt.title('Distribution of month by Region')
plt.show()


# #Distribution of area

# In[63]:


snd.countplot(data=df, x="Area")
plt.show()


# #CONCLUSION
# 
# 1.Estimated unemployment rate is higher in Tripura and lower in Odisha.
# 2.Estimated employees is almost same in many of the states, but lower in Chandigarh.
# 3.The number of estimated emplyees is higher in the month of May and June.
# 4.The Estimated Labour Participation Rate is higher in Telangana and lower in Bihar.
# 5.The Unemployment rate is higher in urban areas when compared to rural areas.
# 

# In[ ]:




