import subprocess
import sys
import pandas as pd
import matplotlib.pyplot as plt

# to show where we are
print("I am in vis.py")

# the file path that was passed in load.py
file_path=sys.argv[1]

#open the csv file after cleaning
df = pd.read_csv("res_dpre.csv")


# List of column names you want to sum for the first plot
columns_to_sum = ['Age_18-30', 'Age_31-40', 'Age_41-50', 'Age_51-60', 'Age_61-70']

# Select and sum the specified columns
age_ranges = df[columns_to_sum].sum()
# Define labels for the pie chart
labels = age_ranges.index
# Define sizes (the counts of each age range)
sizes = age_ranges.values
# Define colors for the slices
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'darkorange']

# Create a figure with a 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(24, 24))

# Plot the first pie chart in the upper-left subplot
axes[0, 0].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
axes[0, 0].set_title("Distribution of Age Ranges")
axes[0, 0].axis('equal')  # Equal aspect ratio ensures that the pie chart is circular

# List of column names you want to sum for the second plot
columns_to_sum2 = ['Payment Method_Bank Transfer', 'Payment Method_Cash', 'Payment Method_Credit Card', 'Payment Method_Debit Card', 'Payment Method_PayPal', 'Payment Method_Venmo']

# Select and sum the specified columns
payment_variations = df[columns_to_sum2].sum()

# Create the second bar chart in the upper-right subplot
axes[0, 1].bar(payment_variations.index, payment_variations.values, color='yellowgreen')
axes[0, 1].set_title("Distribution of Payment Methods")
axes[0, 1].set_xlabel("Payment Methods")
axes[0, 1].set_ylabel("Count")
axes[0, 1].tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability

# List of column names you want to sum for the third plot
columns_to_sum3 = ['Category_Clothing', 'Category_Footwear', 'Category_Outerwear']

# Select and sum the specified columns
category_variations = df[columns_to_sum3].sum()

# Create the third bar chart in the lower-left subplot
axes[1, 0].bar(category_variations.index, category_variations.values, color='lightcoral')
axes[1, 0].set_title("Distribution of Different Categories")
axes[1, 0].set_xlabel("Categories")
axes[1, 0].set_ylabel("Count")
axes[1, 0].tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability

# List of one-hot encoded color columns and one-hot encoded season columns
color_columns = ['Color_Beige', 'Color_Black', 'Color_Blue', 'Color_Brown', 'Color_Charcoal', 'Color_Cyan', 'Color_Gold', 'Color_Gray', 'Color_Green', 'Color_Indigo', 'Color_Lavender', 'Color_Magenta', 'Color_Maroon', 'Color_Olive', 'Color_Orange', 'Color_Peach', 'Color_Pink', 'Color_Purple', 'Color_Red', 'Color_Silver', 'Color_Teal', 'Color_Turquoise', 'Color_Violet', 'Color_White', 'Color_Yellow']
season_columns = ['Season_Spring', 'Season_Summer', 'Season_Fall', 'Season_Winter']

# Extract the relevant columns
color_data = df[color_columns]
season_data = df[season_columns]

# Calculate the sum of each color for each season
color_by_season = pd.DataFrame()
for season in season_columns:
    color_by_season[season] = color_data.mul(df[season], axis=0).sum()

# Create a bar chart to visualize the presence of colors in each season
color_by_season.plot(kind='bar', stacked=True, colormap='Set3', ax=axes[1, 1])
axes[1, 1].set_title("Colors by Season")
axes[1, 1].set_xlabel("Season")
axes[1, 1].set_ylabel("Count")
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].legend(title='Color', bbox_to_anchor=(1.05, 1), loc='upper left')

# Ensure proper layout
plt.tight_layout()

# Show the figure
plt.savefig('vis.png')

subprocess.call(['python3', 'model.py', f'{file_path}'])