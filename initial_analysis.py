#import packages

import numpy as np
import pandas as pd
import geopandas as gdp

import matplotlib.pyplot as plt

allmn = pd.read_csv("./Data/allmn.csv",low_memory=False)

codes = pd.read_excel("./Data/MNCodebook.xlsx",sheet_name = 2,header=1)
codes.fillna(method="ffill")

#get data by judges


unique_judges = np.unique(["{}.{}".format(allmn.iloc[i].jlname,allmn.iloc[i].jfname) for i in range(len(allmn))])
judges = {j:{"sentences":[],"summaries":[]} for j in unique_judges}

for i in range(len(allmn)):
    jname = "{}.{}".format(allmn.iloc[i].jlname,allmn.iloc[i].jfname)
    judges[jname]["sentences"].append(allmn.iloc[i].to_numpy())
