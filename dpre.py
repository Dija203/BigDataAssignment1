import sys 
import pandas as pd
import numpy as np
import subprocess
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import minmax_scale


print("Im in the dpre.py")
file_path=sys.argv[1]

df= pd.read_csv(file_path)

categroy_na= df['Category'].value_counts().keys()[0] # get most frequent item
df['Category'].fillna(categroy_na, inplace=True)

color_na= df['Color'].value_counts().keys()[0] # get most frequent item
df['Color'].fillna(color_na, inplace=True)

season_na= df['Season'].value_counts().keys()[0] # get most frequent item
df['Season'].fillna(season_na, inplace=True)

rev_rating_na= df['Review Rating'].mean()
df['Review Rating'].fillna(rev_rating_na, inplace=True)

promo_na= df['Promo Code Used'].value_counts().keys()[0] # get most frequent item
df['Promo Code Used'].fillna(promo_na, inplace=True)


df.drop(columns=['Customer ID'], axis=1, inplace=True)

df['Review Rating']= np.round(df['Review Rating']) # convert it to 1,2,3,4 or 5 instead of floats

df['Age'].astype('int')
df['Age']= pd.cut(df['Age'], bins=[18,30,40,50,60,70], labels=['18-30','31-40','41-50','51-60','61-70']) 


enc= LabelEncoder()
df['Gender']= enc.fit_transform(df['Gender']) # male is 1 and female is 0
df['Discount Applied']= enc.fit_transform(df['Discount Applied']) # Yes is 1 and No is 0
df['Subscription Status']= enc.fit_transform(df['Subscription Status']) # Yes is 1 and No is 0
df['Promo Code Used']= enc.fit_transform(df['Promo Code Used']) # Yes is 1 and No is 0

df[['Purchase Amount (USD)', 'Previous Purchases', 'Review Rating']] = minmax_scale(df[['Purchase Amount (USD)', 'Previous Purchases', 'Review Rating']])

df= pd.get_dummies(df, dtype='int')

df.to_csv("res_dpre.csv")


print("Data cleaning is done")
subprocess.call(['python3', 'vis.py', f'{file_path}'])