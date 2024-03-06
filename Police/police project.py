import pandas as pd

# Read the police data
police_file = pd.read_csv('Police/file_police.csv')

# Data Cleaning: Remove the column that only contains missing values
column_to_drop = 'country_name'
cleaned_police_file = police_file.drop(columns=column_to_drop)
print("Cleaned Police File:\n", cleaned_police_file)

# Filtering + Value Counts: For Speeding, check if Men or Women were stopped more often
speeding = cleaned_police_file[cleaned_police_file['violation'] == "Speeding"]
gender_counts = speeding['driver_gender'].value_counts(dropna=False)
print("Speeding Violation:\n", speeding)
print("Gender Counts for Speeding Violation:\n", gender_counts)

# Groupby: Does gender affect who gets searched during a stop?
grouped_by_gender = cleaned_police_file.groupby('driver_gender')['search_conducted'].sum()
print("Total Searches Conducted by Gender:\n", grouped_by_gender)

# Mapping + Data-type Casting: Convert stop_duration to numeric values and calculate the mean
cleaned_police_file['stop_duration'] = cleaned_police_file['stop_duration'].map({'0-15 Min': 7.5, '16-30 Min': 24, '30+ Min': 45})
mean_stop_duration = cleaned_police_file['stop_duration'].mean()
print("Mean Stop Duration:\n", mean_stop_duration)

# Groupby, Describe: Compare the age distributions for each violation
grouped_by_violation = cleaned_police_file.groupby('violation')
age_descriptions = grouped_by_violation['driver_age'].describe()
print("Age Distributions by Violation:\n", age_descriptions)
