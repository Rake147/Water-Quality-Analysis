#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# In[2]:


data=pd.read_csv('C:/Users/Rakesh/Datasets/water_potability.csv')


# In[3]:


data.head()


# In[4]:


data.isnull().sum()


# In[5]:


data=data.dropna()


# In[6]:


data.isnull().sum()


# In[7]:


plt.figure(figsize=(15,10))
sns.countplot(data.Potability)
plt.title("Distribution of Unsafe and Safe Water")
plt.show()


# In[10]:


import plotly.express as px
data=data
figure= px.histogram(data,x='ph', color='Potability', title='Factors Affecting Water Quality: PH')
figure.show()


# In[11]:


figure=px.histogram(data,x='Hardness',color='Potability',title='Factors Affecting Water Quality: Hardness')
figure.show()


# In[12]:


figure=px.histogram(data,x='Solids', color='Potability', title='Factors affecting Wates: Solids')
figure.show()


# In[13]:


figure=px.histogram(data,x='Chloramines', color='Potability', title='Factors affecting Wates: Chloramines')
figure.show()


# In[14]:


figure=px.histogram(data,x='Sulfate', color='Potability', title='Factors affecting Wates: Sulfate')
figure.show()


# In[15]:


figure=px.histogram(data,x='Conductivity', color='Potability', title='Factors affecting Wates: Conductivity')
figure.show()


# In[16]:


figure=px.histogram(data,x='Organic_carbon', color='Potability', title='Factors affecting Wates: Organic_carbon')
figure.show()


# In[17]:


figure=px.histogram(data,x='Trihalomethanes', color='Potability', title='Factors affecting Wates: Trihalomethanes')
figure.show()


# In[18]:


figure=px.histogram(data,x='Turbidity', color='Potability', title='Factors affecting Wates: Turbidity')
figure.show()


# In[26]:


get_ipython().system('pip install pycaret')


# In[23]:


correlation=data.corr()
correlation['ph'].sort_values(ascending=False)

