# import
import pandas as pd

DATAFRAMES AND SERIES:
# read a CSV file into pandas
pd.read_csv('file.csv') # method

# defaults to label index column wth numbers, to set it to str
pd.read_csv('file.csv', index_col = 0)
DataFrame.index.name = None # cancels top row assignment to name

# Set NaN values to a string
pd.read_csv('file.csv', na_values = str)

# Set index to column
DataFrame.set_index('col') # method, changes index from numerical to col we want

# to include different encoding types
pd.read_csv('file.csv', encoding = 'some_encdoing') # UTF-8, Latin-1, Windows-1251

# Series and DataFrame constructors (creators)
pd.Series(dict or array)
pd.DataFrame(dict or array, columns = ['column_name'])

# JSON to DataFrame
pd.read_json(json_file) # Json_file can be JSON file or JSON string
________________________________________________________________________________


EXPLORATORY STEPS:
# how to find the dimensions of DataFrame
DataFrame.shape # attribute

# how to print the first few rows of a DataFrame
DataFrame.head(int) # defaults to 5, we can assign int

# display the last few rows of a DataFrame
DataFrame.tail(int) # defaults to 5, we can assign int

# return information about data types in a DataFrame
DataFrame.dtype # attribute

# display general info about the DataFrame
DataFrame.info() # method

# print the statistics of a DataFrame
DataFrame.describe() # method

# defaults to include numeric only, to include non-numeric:
DataFrame.describe(include = ['O']) # Letter O

# DataFrame statistics methods
# require the axis parameter, defaults to axis = 0
DataFrame.max(axis = 0)
DataFrame.min(axis = 'index')
DataFrame.mean(axis = 1)
DataFrame.median(axis = 'column')
DataFrame.mode()
DataFrame.sum()

# find unique values in a series
Series.unique() # method, returns a list of strings
# we can loop over it

# print the statistics of a Series
Series.describe() # method

# display the values within a series or column
Series.values # attribute

# display the count of each unique value in a column
Series.value_counts() # Series only method

# defaults to no NaN, to include NaN:
Series.value_counts(dropna = False)

# Display the range of unique values
Series.value_counts(bins = n, normalize = True)

# find the number of null values in a DataFrame
Series.isnull().sum() # Series method chaining

# Percentage of null values in a DataFrame
(Series.isnull().sum() / DataFrame.shape[0]) * 100

# series statistics methods
Series.max()
Series.min()
Series.mean()
Series.median()
Series.mode()
Series.sum()
________________________________________________________________________________


DATAFRAME INDEXING:
# select a value in a pandas DataFrame
DataFrame.loc[row_label, cloumn_label]

# select multiple values of a DataFrame
DataFrame.loc[:,'col1'] # OR
DataFrame['col1']

DataFrame.loc[:,['col1','col2']] # OR
DataFrame[['col1', 'col2']]

DataFrame.loc[:, 'col1':'col2']
# similar syntax is used to select rows and values from series

# how to index values in a DataFrame using integers
DataFrame.iloc[row_index, column_index]

# select only null values to create boolean index
Series.isnull() # Series method

# selet only non-null values to create boolean index
Series.notnull() # Series method

# Boolean indexing
DataFrame.loc[DataFrame['column'] ==
'test_value', 'assignment_col'] = 'new_value'

# boolean indexing for values with upper and lower bounds
NewDataFrame = (DataFrame[DataFrame['col'].between(lower_bound, upper_bound, inclusive = False)])

# Index using multiple column names
values = ['val_1', 'val_2', 'val_2']
DataFrame[DataFrame['column'].isin(values)]

# check that a value is NaN
pd.isnull(val)

# Test if any value in a DataFrame is True or False
DataFrame.any(axis = 1, skipna =  False) # method, returns False unless True, NaN or non-zero
________________________________________________________________________________


TRANSFORMING DATA:
# create a new column in a DataFrame
DataFrame['new_column_name'] = new_column

# sort values in a DataFrame
DataFrame.sort_values('column_name') # method
# defaults to ascending order, to make descending
DataFrame.sort_values('column_name', ascending = False)

# Access the column axis of a DataFrame
DataFrame.columns # attribute, returns list of column names

# Assign new labels to columns of a DataFrame
DataFrame.columns = ['new_name']

# Replace character in every column name
DataFrame.columns = DataFrame.columns.str.replace('old_char', 'new_char')

# Change multiple values in a DataFrame column
Series.map({'old_value':'new_value'}) # method
# if old value isn't present, makes new value NaN

# Apply a function, element-wise, without an argument
Series.map(func) # don't include () in function name

# Apply a function, element-wise, with an argument
Series.apply(func, arg) # don't include () in function name
# we can only use the Series.apply() method to apply a function with additional arguments element-wise

# Apply function, element-wise, to multiple columns at once
DataFrame.applymap(func)

# Reshape df and assign column names as rows
pd.melt(DataFrame, id_vars = [col1, col2], value_vars = [col3, col4]) # pandas function, not method
# col1 and 2 are the cols we want to keep the same
# col3 and 4 are the cols we want to change to rows
________________________________________________________________________________


CONVERT TEXT TO NUMERIC:
# Direct Method
pd.to_numeric(Series, errors = 'corece') # Coerce makes error values NaN

# String method
# MAKE SURE TO REASSIGN THE NAME BACK TO THE COLUMN
1. Explore the data in the column:
Series.unique()
Series.dtype()

2. Identify patterns and special cases:
oberve and think

3. Remove non-digit characters: STRING OPERATIONS
Series.str.method_name() # method

# All the string functions that can be applied to Series.str.method()
(https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)

EX:
Series.str.replace()
Series.str.len()
Series.str.contains() # finds the substring
Series.str.extract() # find and extract a subtring
# Remove characters from front and end of string
str.strip() # method
# Defaults to removing white spaces, to remove chars
str.strip([char]) # char will be removed until not met

4. convert the column to a numeric dtype:
Series.astype(dtype) # method, dtype = float, int, or str

5. rename col if required:
DataFrame.rename({'old_name':'new_name'}, axis = 'columns', inplace = True) # method
________________________________________________________________________________


HANDLE DUPLICATE VALUES IN A DATAFRAME:
# Check for duplicate rows
DataFrame.duplicated() # Checks if all row is duplicated only if all columns have the same values

# Check duplicate rows for specific columns
DataFrame.duplicated(['col_1', 'col_2']) # method

# Drop duplicate rows
DataFrame.drop_duplicates() # method, drops ALL row, check for columns like above

# Defaults to keeping only first duplicate, to keep last duplicate
DataFrame.drop_duplicates(keep = 'last')


HANDLE MISSING VALUES IN A DATAFRAME:
# General Workflow
# 1. Check for errors in data cleaning/transformation.
# 2. Use data from additional sources to fill missing values.
# 3. Drop row/column.
# 4. Fill missing values with reasonable estimates computed from the available data.

# Ask
# 1. Is the missing data needed to accomplish our end goal?
# 2. How will removing or replacing the missing values affect our analysis?
# 3. What percentage of the data is missing?
# 4. Will dropping missing values cause us to lose valuable information in other columns?
# 5. Can we identify any patterns in the missing data?

# Possible ways to handle missing data:
1. Remove any rows that have missing values: ML
# Drop NaN values from rows
DataFrame.dropna(axis = 0 OR 'index') # method, default

2. Remove any columns that have missing or duplicate values: ML
# Drop NaN values from columns
DataFrame.dropna(axis = 1 OR 'columns') # method

# Drop NaN columns with a minimum thresh parameter
DataFrame.dropna(axis = 1, thresh = int) # only drop columns if they contain below a int of non-null values
# Find int by using DataFrame.notnull().sum().sort_values()

# Drop full columns
DataFrame.drop('col', axis = 1) # method


3. Fill the missing values with some other value: Imputation
# Assign new values to index values
DataFrame.loc[DataFrame['column'] ==
'test_value', 'assignment_col'] = 'new_value'

# Assign new values to NaN values
Series/DataFrame.fillna(new_value) # method

# Replace certain values in a Series based on a Boolean mask
Series.mask(bool_mask, val_to_fill) # Method, replaces True value with val_to_fill
# Val_to_fill: A value or a series that has identical index labels

# replace null values in a series with their equivalents from another series
Series.mask(Series.isnull(), Eq_Series) # Can check if Series != Eq_series and replace with np.nan

4. Leave the missing value as is
________________________________________________________________________________


CONVERT DATAFRAME TO OBJECT:
# Convet to datetime object
pd.to_datetime(DataFrame) # Method

# Extract datetime data from datetime object
DataFrame.dt.month
DataFrame.dt.year

# convert Series to list
Series.tolist() # method

# Convert to Correlation DataFrame
DataFrame.corr() # Method
________________________________________________________________________________


GROUPBY METHODS:
# Create a GroupBy object
GroupBy = DataFrame.groupby('col') # class, create an instance

# Select data for a certain group
GroupBy.get_group('col') # method

# Explore info about the GroupBy object
GroupBy.groups # attribute

# Calculate the mean of groups.
GroupBy.mean() # method

# Calculate the sum of group values.
GroupBy.sum() # method

# Calculates the size (number of rows) of the groups.
GroupBy.size() # method

# Calculates the count of values in groups.
GroupBy.count() # method

# Calculates the minimum of group values.
GroupBy.min() # method

# Calculates the maximum of group values.
GroupBy.max() # method

# GroupBy object indexing
# Single column
GroupBy["col1"]
# List of columns
GroupBy[["col1", "col2"]]

# Apply multiple aggregation functions at once
GroupBy.agg([func_1, func_2, func_3]) # method, accepts single func or as strings or dict or list of functions without paranthese
# np.mean or 'mean'

# method chaning groupby objects
DataFrame.GroupBy('index')['value'].function() # index == index of groupby, value == values of the function applied
________________________________________________________________________________


PIVOT TABLES:
# create a pivot table from a DataFrame
DataFrame.pivot_table(values='col_to_agg', index='col_to_group_by') # method, defaults to using np.mean, results in DataFrame not object

# apply the function to all the rows/columns for a 'Total result'
DataFrame.pivot_table(values = 'col_to_agg', index = 'col_to_group_by', aggfunc = np.mean, margins = True) # method, accepts boolean

# apply multiples functions
DataFrame.pivot_table(values = 'col_to_agg', index = 'col_to_group_by', aggfunc = [np.mean, np.sum, np.mode]) # list of functions
________________________________________________________________________________


COMBINING DATAFRAMES:
# Concatenate two DataFrames
pd.concat([df_1, df_2, df_3]) # pandas function not method, repeats row indexes

# Defaults to adding rows, to add columns
pd.concat([df_1, df_2, df_3], axis = 1) # adds on columns to the same index
# for uneven rows, just adds both for the total number of rows combined
# By default, concat func keeps all the data and adds NaN with missing data

# Reset the index values
pd.concat([df_1, df_2, df_3], ignore_index = True) # makes index from 0 to n-1

# Merge two DataFrames
pd.merge(left = df_1, right = df_2, on = 'col') # pandas function not method, defaults to axis = 1

# specify different type of join
pd.merge(left = df_1, right = df_2, on = 'col', how = str) # str can be any of the following:
# 'Inner': only includes elements that appear in both dataframes with a common key
# 'Outer': includes all data from both dataframes
# 'Left': includes all of the rows from the "left" dataframe along with any rows from the "right" dataframe with a common key
# 'Right': includes all of the rows from the "right" dataframe along with any rows from the "left" dataframe with a common key
# the result retains all columns from both of the original dataframes
# we'd use a 'left' join when we don't want to drop any data from the left dataframe.

# Add columns suffixes...defaults to ('_x', '_y')
pd.merge(left = df_1, right = df_2, on = 'col', suffixes = ('1', '2'))

# Specify the join based on the indexes of the DataFrames
pd.merge(left = df_1, right = df_2, left_index = True, right_index = True)


# pd.concat()
# Default Join Type?
# Outer
# Can Combine More Than Two Dataframes at a Time?
# No
# Can Combine Dataframes Vertically or Horizontally?
# Both

# pd.merge()
# Default Join Type?
# Inner
# Can Combine More Than Two Dataframes at a Time?
# Yes
# Can Combine Dataframes Vertically or Horizontally?
# Horizontally
________________________________________________________________________________


# save a DataFrame as a csv file after cleaning
DataFrame.to_csv('filename.csv') # method
# to save a DataFrame without index column numbers
DataFrame.to_csv('filename.csv', index = False)
