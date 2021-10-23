import numpy as np
import pandas as pd
#import geopandas as gdp

import tqdm
import matplotlib.pyplot as plt

allmn = pd.read_csv("./Data/allmn.csv",low_memory=False)

codes = pd.read_excel("./Data/MNCodebook.xlsx",sheet_name = 2,header=1)
codes.fillna(method="ffill")

#get data by judges

#unique_judges_raw = ["{}+{}".format(allmn.iloc[i].jlname,allmn.iloc[i].jfname.split(" ")[0]) for i in range(len(allmn))]
unique_judges = list(set([(x[0],str(x[1]))  for x in allmn[["jlname","jfname"]].to_numpy()]))

judges = {j:{"sentences":allmn[(allmn.jlname == j[0]) & (allmn.jfname == j[1])],"summaries":[]} for j in tqdm.tqdm(unique_judges)}

#offtype, 1-> 8, drop sex crimes (5)
#focus a few offense types
#severity, 1 -> 12
#focus just on severity?

#just do severity

#just do offtype

a =[]
for i in range(len(unique_judges)):
    a.append(len(judges[unique_judges[i]]["sentences"])<50)

def populate_summaries(judge_df, unique_judges, demographic_sig, criminality_sig):
    all_dsig = judge_df[unique_judges[1]]["sentences"][demographic_sig].unique()
    all_csig = judge_df[unique_judges[1]]["sentences"][criminality_sig].unique()
    for sig1 in all_csig:
        for sig2 in all_dsig:
            for k in unique_judges:
                temp = judge_df[k]['sentences']
                judge_df[k]['summaries'].append(temp[(temp[demographic_sig] == sig1) & (temp[criminality_sig] == sig2)]['time'].mean())

