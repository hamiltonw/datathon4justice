import numpy as np
import pandas as pd
#import geopandas as gdp

import tqdm
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

allmn = pd.read_csv("./Data/allmn.csv",low_memory=False)

codes = pd.read_excel("./Data/MNCodebook.xlsx",sheet_name = 2,header=1)
codes.fillna(method="ffill")

#get data by judges

#unique_judges_raw = ["{}+{}".format(allmn.iloc[i].jlname,allmn.iloc[i].jfname.split(" ")[0]) for i in range(len(allmn))]
unique_judges = list(set([(x[0],str(x[1]))  for x in allmn[["jlname","jfname"]].to_numpy()]))

judges = {j:{"sentences":allmn[(allmn.jlname == j[0]) & (allmn.jfname == j[1])],"summaries":[]} for j in tqdm.tqdm(unique_judges)}

#Get judges with>50 cases only
a =[]
for i in range(len(unique_judges)):
    if len(judges[unique_judges[i]]["sentences"])>50:
        a.append(unique_judges[i])

#Populate the summaries of the judges with the normalized sentence per criminality factor per demographic factor
def populate_summaries(judge_df, unique_judges, demographic_sig, criminality_sig):
    #Inputs:
    #   judge_df: data frame of the judges
    #   unique_judges: all judges names to access judges_df
    #   demographic_sig: demographic factor to split sentences by
    #   criminality sig: criminality factor to split sentences by
    #Ouput:
    #   populates judges data frame with vector of normalized sentences 
    all_dsig = judge_df[unique_judges[1]]["sentences"][demographic_sig].unique()
    all_csig = judge_df[unique_judges[1]]["sentences"][criminality_sig].unique()
    for sig1 in all_csig:
        for sig2 in all_dsig:
            temp_mean = allmn[(allmn[demographic_sig] == sig1) & (allmn[criminality_sig] == sig2)]['confine'].mean()
            for k in unique_judges:
                temp = judge_df[k]['sentences']
                temp2 = temp[(temp[demographic_sig] == sig1) & (temp[criminality_sig] == sig2)]['confine'].mean()/temp_mean
                #populate judges with none of these cases with just the mean
                if np.isnan(temp2):
                    judge_df[k]['summaries'].append(1)
                else:
                    judge_df[k]['summaries'].append(temp2)


#Find averages    
populate_summaries(judges, a, "race", "severity")

all_summaries = np.empty([len(a),len(judges[a[1]]['summaries'])])
i = 0
for val in a:
    all_summaries[i,:] = judges[val]['summaries']
    i +=1 

#yay cluster
kmeans = KMeans(n_clusters=2, random_state=0).fit(all_summaries)

for val in np.where(kmeans.labels_ ==1):

for val in np.where(kmeans.labels ==0):
