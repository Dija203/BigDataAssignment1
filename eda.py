import sys 
import pandas as pd
import subprocess
import os 


print("Im in the eda.py")

file_path=sys.argv[1] # recive the file path argument from the load.py subprocess

try:
   df= pd.read_csv(file_path)
except FileNotFoundError:
   print("File path is wrong or the file dosnt exist")

eda_results_1= f"""
The number of null values
-----------------------------------
{df.isna().sum()[df.isna().sum()>0]}
-----------------------------------
"""

with open('eda-in-1.txt', 'w') as f:
   f.write(eda_results_1)
   f.close()

eda_results_2= f"""
-----------------------------------
The mean age {int(df['Age'].mean())}
-----------------------------------
"""

with open('eda-in-2.txt', 'w') as f:
   f.write(eda_results_2)
   f.close()


eda_results_3= f"""
-----------------------------------
Number of Males: {df['Gender'].value_counts()[0]}
Number of Femlaes: {df['Gender'].value_counts()[1]}
-----------------------------------
"""

with open('eda-in-3.txt', 'w') as f:
   f.write(eda_results_3)
   f.close()

eda_results_4= f"""
-----------------------------------
Min Purchase amount: {df['Purchase Amount (USD)'].min()}
Max Purchase amount: {df['Purchase Amount (USD)'].max()}
-----------------------------------
"""

with open('eda-in-4.txt', 'w') as f:
   f.write(eda_results_4)
   f.close()

   
print("EDA is done") 
subprocess.call(['python3', 'dpre.py', f'{file_path}'])

