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
#import geoplot


# In[2]:


county_bound = gpd.read_file('bdry_counties.gpkg')
data = pd.read_csv('allmn.csv')


# In[3]:


county_bound.plot()


# In[4]:


## give each CTY_NAME a number based on if statment
def judge_dis(df, COUNTY_NAM):
    df['Court_Dis'] = ' '
    i=0
    while i < len(df[COUNTY_NAM]):
        if df[COUNTY_NAM][i] in ['Carver', 'Dakota', 'Goodhue', 'LeSueur', 'McLeod', 'Scott', 'Sibley']:
            df['Court_Dis'][i]='First District'
            
        if df[COUNTY_NAM][i] in ['Ramsey']:
            df['Court_Dis'][i]='Second District'
            
        if df[COUNTY_NAM][i] in ['Dodge', 'Fillmore', 'Freeborn', 
                                 'Houston', 'Mower', 'Olmsted', 
                                 'Rice', 'Steele', 'Wabasha', 'Waseca', 
                                 'Winona']:
            df['Court_Dis'][i]='Third District'
            
        if df[COUNTY_NAM][i] in ['Hennepin']:
            df['Court_Dis'][i]='Fourth District'
        
        if df[COUNTY_NAM][i] in ['Blue Earth', 'Brown', 
                                 'Cottonwood', 'Faribault', 
                                 'Jackson', 'Lincoln', 'Lyon',
                                 'Martin', 'Murray', 'Nicollet',
                                 'Nobles', 'Pipestone', 'Redwood',
                                 'Rock', 'Watonwan']:
            df['Court_Dis'][i]='Fifth District'
            
        if df[COUNTY_NAM][i] in ['Carlton', 'Cook', 'Lake',
                                 'St. Louis']:
            df['Court_Dis'][i]='Sixth District'
        
        if df[COUNTY_NAM][i] in ['Becker', 'Benton', 'Clay',
                                 'Douglas', 'Mille Lacs',
                                 'Morrison', 'Otter Tail',
                                 'Stearns', 'Todd', 'Wadena']:
            df['Court_Dis'][i]='Seventh District'
            
        if df[COUNTY_NAM][i] in ['Big Stone', 'Chippewa', 'Grant',
                                 'Kandiyohi', 'Lac qui Parle',
                                 'Meeker', 'Pope', 'Renville',
                                 'Stevens', 'Swift', 'Traverse',
                                 'Wilkin', 'Yellow Medicine']:
            df['Court_Dis'][i]='Eighth District'
        
        if df[COUNTY_NAM][i] in ['Aitkin', 'Beltrami', 'Cass',
                                 'Clearwater', 'Crow Wing',
                                 'Hubbard', 'Itasca', 'Kittson',
                                 'Koochiching', 'Lake of the Woods',
                                 'Mahnomen', 'Marshall', 'Norman',
                                 'Pennington', 'Polk', 'Red Lake',
                                 'Roseau']:
            df['Court_Dis'][i]='Ninth District'
            
        if df[COUNTY_NAM][i] in ['Anoka', 'Chisago', 'Isanti',
                                 'Kanabec', 'Pine', 'Sherburne',
                                 'Washington', 'Wright']:
            df['Court_Dis'][i]='Tenth District'
        i=i+1
    
    return(df)
    


# In[5]:


judge_dis(county_bound, 'COUNTY_NAM')


# In[11]:


judge_dist = county_bound.dissolve('Court_Dis')


# In[14]:


judge_dist.plot()


# In[ ]:




