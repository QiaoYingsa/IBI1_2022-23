import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:\\cygwin64\\home\\乔英飒\\IBI1_2022-23\\IBI1_2022-23\\Practical7")
covid_data = pd.read_csv("full_data.csv")

# Show second column from every 100th row from the first 1000 rows (inclusive)
second_column_data = covid_data.iloc[:1001:100, 1]
print("Second column data from every 100th row from the first 1000 rows (inclusive):")
print(second_column_data)

# Show "total cases" for all rows corresponding to Afghanistan
afghanistan_total_cases = covid_data[covid_data['location'] == 'Afghanistan']['total_cases']
print("Total cases for Afghanistan:")
print(afghanistan_total_cases)

# Compute the mean number of new cases and new deaths on 31 March 2020
march_31_data = covid_data[covid_data['date'] == '2020-03-31']
mean_new_cases_march_31 = march_31_data['new_cases'].mean()
mean_new_deaths_march_31 = march_31_data['new_deaths'].mean()
print("Mean number of new cases on 31 March 2020:", mean_new_cases_march_31)
print("Mean number of new deaths on 31 March 2020:", mean_new_deaths_march_31)

# Create a boxplot of new cases and new deaths on 31 March 2020
march_31_data[['new_cases', 'new_deaths']].boxplot()
plt.title('Boxplot of New Cases and New Deaths on 31 March 2020')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

# Plot new cases and new deaths worldwide over time
worldwide_data = covid_data.groupby('date').sum()
plt.plot(worldwide_data.index, worldwide_data['new_cases'], label='New Cases')
plt.plot(worldwide_data.index, worldwide_data['new_deaths'], label='New Deaths')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.title('Worldwide New Cases and New Deaths Over Time')
plt.show()

# Change directory to the folder containing the data file
os.chdir("C:\\cygwin64\\home\\乔英飒\\IBI1_2022-23\\IBI1_2022-23\\Practical7")

# Load the COVID-19 data from the file into a pandas dataframe
covid_data = pd.read_csv("full_data.csv")

# Filter the data for Germany and UK
germany_data = covid_data[covid_data['location'] == 'Germany']
uk_data = covid_data[covid_data['location'] == 'United Kingdom']

# Get the latest information on deaths in Germany and UK
latest_deaths_germany = germany_data['total_deaths'].iloc[-1]
latest_deaths_uk = uk_data['total_deaths'].iloc[-1]

# Get the latest information on total cases in Germany and UK
latest_cases_germany = germany_data['total_cases'].iloc[-1]
latest_cases_uk = uk_data['total_cases'].iloc[-1]

# Calculate the proportion of cases that have died in Germany and UK
death_proportion_germany = latest_deaths_germany / latest_cases_germany
death_proportion_uk = latest_deaths_uk / latest_cases_uk
print("The proportion of cases that have died in Germany is:")
print(death_proportion_germany)
print("The proportion of cases that have died in UK is:")
print(death_proportion_uk)

# Plot the death proportion for Germany and UK
plt.bar(['Germany', 'UK'], [death_proportion_germany, death_proportion_uk])
plt.xlabel('Country')
plt.ylabel('Proportion of Cases That Have Died')
plt.title('Proportion of COVID-19 Cases That Have Died in Germany and UK')
plt.show()

