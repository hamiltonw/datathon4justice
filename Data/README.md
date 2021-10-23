# Census data

census_data.csv contains 2019 ACS (American Community Survey) data for the state of Minnesota. 

Data was pulled from https://api.census.gov/data.html on Oct. 23 2021.

Descriptors for variables are found in https://api.census.gov/data/2019/acs/acs5/profile/variables.html.

To read in the data via Python's pandas, you can use

```
import pandas as pd

censusmn = pd.read_csv("census_data.csv")
```
