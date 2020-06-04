# import
import matplotlib.pyplot as plt

# Use jupyter notebook with matplotlib
%matplotlib inline
________________________________________________________________________________


# general workflow
1. create a plot using data

LINE PLOT:
plt.plot(x_values, y_values) # method
# empty plot goes from -0.6 to 0.6
________________________________________________________________________________


PLOTS WITH MULTIPLE LINES:
# overlaying multiple lines in the same figure
plt.plot(data1)
plt.plot(data2)
# will generate one plot with both lines
# automatically generates a figure unless one was created
________________________________________________________________________________


BAR PLOTS:
# create a vertical bar plot with the data
plt.bar(left, height, width) # method, accept a list-like object, the position of the bar on the left
________________________________________________________________________________


DATAFRAME PLOTS:
# create a plot directly using pandas
DataFrame.plot(x, y, kind, figszie = (int, int), title = str, legend = bool) # method, x and y are data cols, kind is:
# ‘line’ : line plot (default)
# ‘bar’ : vertical bar plot
# ‘barh’ : horizontal bar plot
# ‘hist’ : histogram
# ‘box’ : boxplot
# ‘kde’ : Kernel Density Estimation plot
# ‘density’ : same as ‘kde’
# ‘area’ : area plot
# ‘pie’ : pie plot
# ‘scatter’ : scatter plot
# ‘hexbin’ : hexbin plot

# create a scatter matrix plot
from pandas.plotting import scatter_matrix
scatter_matrix(DataFrame, figsize = (int, int))

# create a bar plot
DataFrame.plot.bar(x, y) # method, x and y are the names of the axes

# histogram using Series
Series.hist(bins = int, range = (min, max)) # set number of bins and range, both int
________________________________________________________________________________


2. customize the appearance of the plot
# choose the color of the plot
plt.plot(c = str) # str is the color we want, ex 'red'

# add label of a line
plt.plot(label = str) # str is the name of the line

# rotate the x and y-axis labels by 90 degrees
plt.xticks(rotation = angle) # method, angle int or float
plt.yticks(rotation = angle)

# add x and y labels
plt.xlabel(str) # accepts a string value, which gets set as the x-axis label.
plt.ylabel(str) # accepts a string value, which is set as the y-axis label.

# add plot title
plt.title(str) # accepts a string value, which is set as the plot title.

# add a legend and specify its location
plt.legend(loc = str) # str is the location
# ‘upper right’
# ‘upper left’
# ‘lower left’
# ‘lower right’
# ‘right’
# ‘center left’
# ‘center right’
# ‘lower center’
# ‘upper center’
# ‘center’
________________________________________________________________________________


3. display the plot
plt.show() # method
