import numpy as np

# read csv files into a numpy ndarray
np.genfromtxt('file.csv', delimiter = ',', skip_header = 1)
# delimiter: A named argument
#specifying the string used to separate each value.
# Skip_header takes in the number of row to remove not index

# find the dimenstions of an ndarray
ndarray.shape # attribute

# find the data type inside an ndarray
ndarray.dtype # attribute

# how to index using boolean arrays
array = []
bool_array = []
result = array[bool_array]

# how to modfify values in an array
ndarray[location_of_values] = new_value

# how to use boolean indexing to change values in ndarray
array[array[:, column_for_comparison]
== value_for_comparison, column_for_assigment] = new_value

# Display an array of values within a range
np.arange([start, ]stop, [step, ]) # method, takes in int or list
