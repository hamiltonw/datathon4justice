#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly as plt
import plotly.express as px
import json
from urllib.request import urlopen
import pandas as pd
import geopandas as gpd
import folium

county_bound = gpd.read_file('bdry_counties.gpkg')
census_data = pd.read_csv('census_data.csv')
case_data = pd.read_csv('allmn.csv')


# In[2]:


mean_hi = census_data[['DP03_0087E', 'county']]
#total households on food stamps DP03_0074E
#mean family income DP03_0087E


# In[3]:


sentance_data = case_data[['confine', 'time', 'county', 'race']]
sentance_data['over/under max time'] = sentance_data['confine']-sentance_data['time']
#confine is in months


# In[4]:


sentance_data


# In[5]:


#find na values
na_valus = sentance_data[sentance_data['time'].isna()==True].index
#drop na values
cleaned_sentance_data=sentance_data.drop(na_valus)
#test to see if it worked
sum(cleaned_sentance_data['time'].isna())


# In[6]:


sentance_data


# In[7]:



income_sentance_data = mean_hi.merge(sentance_data, on='county')
#make it readable
income_sentance_data = income_sentance_data.rename(columns={'DP03_0087E': 'mean family income'})

income_sentance_data


# In[ ]:





# In[8]:


county_bound = county_bound.rename(columns={'COUNTY_FIP': 'county'})
county_bound["county"] = pd.to_numeric(county_bound["county"])

bound_income_sentance_data = county_bound.merge(income_sentance_data, on='county')


# In[9]:


bound_income_sentance_data


# In[10]:


bound_income_sentance_data.plot(column='mean family income')


# In[ ]:


bound_income_sentance_data.plot(column='mean family income', cmap='Blues')


# In[14]:


sum(bound_income_sentance_data['mean family income'].isna())


# In[ ]:




