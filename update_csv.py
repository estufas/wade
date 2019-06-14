import pandas as pd
import os
basedir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(basedir,'computerRank10.csv'))
# print(df.head())
# corrected_time_dseries = df['0']+' '+df['Time']
# print(df.head())
# df['Time']= corrected_time_dseries
# print(corrected_time_dseries.head())
df.drop(['Distance','District'],inplace=True,axis=1)
df.rename(index=str, columns={"Meeting": "Meeting_Name","0": "Day"},inplace=True)
df.to_csv(os.path.join(basedir,'cleaned_data.csv'))
