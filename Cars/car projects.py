import pandas as pd

# Read the car data
car_file = pd.read_csv('Cars/cars_data.csv')

# Data Cleaning: Find and fill null values with the mean of each column
null_per_column = car_file[car_file.isnull().any(axis=1)]
null_sum_column = car_file.isnull().sum()
new_car_file = car_file.dropna()
null_sum_new = new_car_file.isnull().sum()

print("Null Values after Cleaning:\n", null_sum_new)
print("Cleaned Data:\n", new_car_file)

# Value Counts: Check different types of makes and their occurrence
types_makes = new_car_file['Make'].value_counts()
print("Types of Makes and Their Counts:\n", types_makes)

# Filtering: Show records where Origin is Asia or Europe
filtered_countries = new_car_file[(new_car_file['Origin'] == 'Asia') | (new_car_file['Origin'] == 'Europe')]
print("Records with Origin in Asia or Europe:\n", filtered_countries)

# Removing unwanted records: Remove records where Weight is above 4000
filter_weight = new_car_file[new_car_file['Weight'] < 4000]
print("Records with Weight below 4000:\n", filter_weight)

# Applying function on a column: Increase all values of 'MPG_City' by 3
car_file_copy = new_car_file.copy()
car_file_copy['MPG_City'] = car_file_copy['MPG_City'] + 3
print("MPG_City values increased by 3:\n", car_file_copy)

