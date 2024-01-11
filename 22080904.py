#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'climate_change_agriculture_dataset.csv'
data = pd.read_csv(file_path)


# Display basic information about the dataset
print(data.info())

# Summary statistics
print(data.describe())


# Adding my info
my_name = "Md Monir Hussain"
my_id = " Student ID : 22080904"

# Adding Explanation
main_message = "Effect of climate in agricultre"
explanation_plot1 = "Plot-1 : A significant spike in Flood occurrences, making up 250"
explanation_plot2 = "Plot-2 : Low crop diseases reported 35.3%"
explanation_plot3 = "Plot-3 : majority of recorded temperatures fall within the lower range"
explanation_plot4 = "Plot-4 : CO2 levels increase, crop yield generally rises."


# Create a figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.patch.set_facecolor('lightgrey')  # Set background color

# Visualization 1: Bar plot - Extreme Weather Events count
sns.countplot(x='Extreme Weather Events', data=data,
              ax=axs[0, 0], palette='Set2')
axs[0, 0].set_title('Frequency of Extreme Weather Events')

# Visualization 2: Pie plot - Distribution of Crop Disease Incidence
crop_disease_counts = data['Crop Disease Incidence'].value_counts()
axs[0, 1].pie(crop_disease_counts, labels=crop_disease_counts.index,
              autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
axs[0, 1].legend(bbox_to_anchor=(1, 1), loc='upper left',
                 labels=crop_disease_counts.index)
axs[0, 1].set_title('Crop Disease Incidence Distribution')

# Visualization 3: Histogram - Distribution of Temperature
sns.histplot(data['Temperature'], bins=15,
             kde=True, ax=axs[1, 0], color='orange')
axs[1, 0].set_title('Distribution of Temperature')
axs[1, 0].set_xlabel('Temperature')
axs[1, 0].set_ylabel('Frequency')

# Visualization 4: Scatter plot - CO2 Levels vs. Crop Yield
sns.scatterplot(x='CO2 Levels', y='Crop Yield', data=data,
                ax=axs[1, 1], hue='Extreme Weather Events', palette='viridis')
axs[1, 1].set_title('CO2 Levels vs. Crop Yield')
axs[1, 1].set_xlabel('CO2 Levels')
axs[1, 1].set_ylabel('Crop Yield')


# Add text explanations
plt.figtext(0.5, 0.92, f"{my_name}, {my_id}",
            ha='center', va='center', fontsize=14)
plt.figtext(0.5, 0.95, main_message, ha='center',
            va='center', fontsize=18)
plt.figtext(0.1, 0.07, explanation_plot1, ha='left', va='center', fontsize=14)
plt.figtext(0.1, 0.05, explanation_plot2, ha='left', va='center', fontsize=14)
plt.figtext(0.1, 0.03, explanation_plot3, ha='left', va='center', fontsize=14)
plt.figtext(0.1, 0.01, explanation_plot4, ha='left', va='center', fontsize=14)

# Save the dashboard as an image
plt.savefig('22080904.png', dpi=300)
