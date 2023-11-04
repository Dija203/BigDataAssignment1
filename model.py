import subprocess
import sys
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("res_dpre.csv")
# Generate some random data for demonstration
X = df[["Gender", "Purchase Amount (USD)", "Subscription Status", "Age_18-30", "Age_31-40", "Age_41-50", "Age_51-60", "Age_61-70", "Category_Accessories", "Category_Clothing", "Category_Footwear", "Category_Outerwear", "Shipping Type_2-Day Shipping", "Shipping Type_Express", "Shipping Type_Free Shipping", "Shipping Type_Next Day Air", "Shipping Type_Standard", "Shipping Type_Store Pickup", "Payment Method_Bank Transfer", "Payment Method_Cash", "Payment Method_Credit Card", "Payment Method_Debit Card", "Payment Method_PayPal", "Payment Method_Venmo", "Frequency of Purchases_Annually", "Frequency of Purchases_Bi-Weekly", "Frequency of Purchases_Every 3 Months", "Frequency of Purchases_Fortnightly", "Frequency of Purchases_Monthly", "Frequency of Purchases_Quarterly", "Frequency of Purchases_Weekly"]].values

# Define the number of clusters (k) and create a KMeans model
k = 3
kmeans = KMeans(n_clusters=k, random_state=0)

# Fit the KMeans model to your data
kmeans.fit(X)

# Get cluster assignments for each data point
labels = kmeans.labels_

# collecting similar clusters together
center_0 = []
center_1 = []
center_2 = []

for i in range(len(labels)):
    if labels[i] == 0:
        center_0.append(i)
    elif labels[i] == 1:
        center_1.append(i)
    else:
        center_2.append(i)



# Combine the lists into a list of tuples
combined_data = list(zip(center_0, center_1, center_2))

# Define the file name for the output text file
output_file = 'k.txt'

# Write the data to the text file with headers
with open(output_file, 'w') as file:
    file.write(f"Total in C0 {sum(center_0)} \n")  # Write headers
    file.write(f"Total in C1 {sum(center_1)} \n")  
    file.write(f"Total in C2 {sum(center_2)}\n") 
    file.write("C_0\tC_1\tC_2\n")  # Write headers
    for row in combined_data:
        file.write('\t'.join(map(str, row)) + '\n')

print(f"Data has been written to {output_file}")


