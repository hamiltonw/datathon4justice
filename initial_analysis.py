#import packages

import numpy as np
import pandas as pd
import geopandas as gdp

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
