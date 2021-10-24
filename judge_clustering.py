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

unique_judges = [j for j in unique_judges if len(allmn[(allmn.jlname == j[0]) & (allmn.jfname == j[1])]) > 30]

#compute statistics

#judge, year, crime type, race (num, average sentence), sex (num, average sentence )
unique_year = allmn.sentyear.unique()
pd_data = [[j,y] for j in unique_judges for y in unique_year]
summary_stats = pd.DataFrame(data = pd_data,columns=["judge","year"])

unique_race = allmn.race.unique()
race_label = {0:"Unk",1:"White",2:"Black",3:"Am Ind",4:"Hispanic",5:"Asian",6:"Other",7:"Unk"}

unique_sex = allmn.sex.unique()
sex_label = {0:"Unk",1:"male",2:"female"}

unique_offtype = allmn.offtype.unique()
ot_label = {1:"person",2:"property",3:"drugs",4:"other",5:"noncsc/sex grid",6:"DWI",7:"Weapons",8:"Other"}

#actual time served: "confine"

#set up summary stats df
for ot in unique_offtype:
    for r in unique_race:
        summary_stats["{}-{}-num".format(ot_label[ot],race_label[r])] = np.nan
        summary_stats["{}-{}-avg".format(ot_label[ot],race_label[r])] = np.nan
    for s in unique_sex:
        summary_stats["{}-{}-num".format(ot_label[ot],sex_label[s])] = np.nan
        summary_stats["{}-{}-avg".format(ot_label[ot],sex_label[s])] = np.nan

    summary_stats["{}-num".format(ot_label[ot])] = np.nan
    summary_stats["{}-avg".format(ot_label[ot])] = np.nan

for j in tqdm.tqdm(unique_judges):
    for y in tqdm.tqdm(unique_year):
        for ot in unique_offtype:
            sub_df = allmn[(allmn.jfname == j[1]) & (allmn.jlname == j[0]) & (allmn.sentyear == y) & (allmn.offtype == ot)]
            summary_idx = summary_stats[(summary_stats.judge == j ) & (summary_stats.year == y)].index[0]

            for r in unique_race:
                summary_stats.at[summary_idx,"{}-{}-num".format(ot_label[ot],race_label[r])] =  len(sub_df[sub_df.race == r])
                summary_stats.at[summary_idx,"{}-{}-avg".format(ot_label[ot],race_label[r])] = np.mean(sub_df[sub_df.race == r].confine)

            for s in unique_sex:
                summary_stats.at[summary_idx,"{}-{}-num".format(ot_label[ot],sex_label[s])] =  len(sub_df[sub_df.sex == s])
                summary_stats.at[summary_idx,"{}-{}-avg".format(ot_label[ot],sex_label[s])] = np.mean(sub_df[sub_df.sex == s].confine)

            summary_stats.at[summary_idx,"{}-num".format(ot_label[ot])] =  len(sub_df)
            summary_stats.at[summary_idx,"{}-avg".format(ot_label[ot])] = np.mean(sub_df.confine)

#now save
save_fp = "./Data/summary_stats_judge_per_year.csv"
summary_stats.to_csv(path_or_buf = save_fp)
