# general syntax
matplotlib.pyplot.method()

# import
import matplotlib.pyplot as plt

# Use jupyter notebook with matplotlib (makes the plot inline instead of opening up another window)
%matplotlib inline
________________________________________________________________________________


# general workflow:
# Figure is the container for all plots, i.e. the display window
# Axes is the plot itself
# axis there's x and y axis
# subplots lead from left to right, top to bottom
1. create a plot using data

# Create a figure
fig = plt.figure() # figure class method

# THEN create subplots == instances of the Axes class
subplot = fig.add_subplot(nrows, ncols, plot_number) # int
# empty plot goes from 0.0 to 1.0

# Shortcut method
fig, subplot = plt.subplots(nrows, ncols) # defaults to 1 by 1

# figure plots read from left to right (3 x 3 plot)
1, 2, 3,
4, 5, 6,
7, 8, 9

# OR (3 x 4 figure)
1, 2, 3, 4
5, 6, 7, 8
9, 10, 11, 12

# OR (4x1 figure)
1
2
3
4
________________________________________________________________________________


LINE PLOT:
# generate a plot within an axes
subplot.plot(x_values, y_values) # method

# add label of a line
subplot.plot(label = str) # str is the name of the line

# set color of plot
subplot.plot(color = str) # str is color, 'green', 'red', 'yellow'

# set color using tableu palette and color ratios
cb_dark_blue = (0/255, 107/255, 164/255) # why 255? in comps, RGB from 0 to 255
# plt can only accept RGB values within 0 to 1 so we ratio the values
# http://tableaufriction.blogspot.com/2012/11/finally-you-can-use-tableau-data-colors.html

# set the line width
subplt.plot(linewidth = float) # method, float is the thicccness we want #THICCCwith3C's

# Use a loop with range() function to generate plots:
# range() built-in function produces a list of sequences of numbers from 0 to, but not including, arg parameter
for i in range(int):
    subplot = fig.add_subplot(nrows, ncols, i+1)
    subset = DataFrame[(i*12) : ((i+1) * 12)]
    subplot.plot(subset['col1'], subset['col2'])
________________________________________________________________________________


DATAFRAME PLOTS:
# create a plot directly using pandas DataFrame
subplot = DataFrame.plot(x, y, kind, figszie = (int, int), title = str) # method, x and y are data cols, kind is str of type of plot
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

# general plot using a Series
subplot = Series.plot(x, y, kind) # hist for histogram of series
________________________________________________________________________________


LINE PLOT WITH MULTIPLE LINES:
# create a plot with multiple lines
subplot.plot(data1)
subplot.plot(data2)
# will generate one plot with both lines
# automatically generates a figure unless one was created
________________________________________________________________________________


BAR PLOTS:
# create a vertical bar subplot
subplot.bar(x, height, width) # method, width = 0.8, accepts a list-like object, x is position the left

# create a horizontal bar subplot
subplt.barh(y, width, height) # method, height = 0.8, accepts a list, y is the position at the bottom
________________________________________________________________________________


SCATTER PLOT:
# create a scatter plot
subplot.scatter(x, y) # method, x and y are int or list like objects
# Put the independent on x-axis and the dependent on the y-axis
________________________________________________________________________________


HISTOGRAMS:
# create a histogram
subplot.hist(x) # method, x is an array or iterable object
# 1. calculate the minimum and maximum value from the sequence of values we passed in
# 2. create 10 bins of equal length that span the range from the minimum to the maximum value
# 3. group unique values into the bins
# 4. sum up the associated unique values
# 5. generate a bar for the frequency sum for each bin

# 1. to set max and min values for hist x ticks
subplot.hist(range(min, max)) # method, min and max are int

# 2. set the number of bins
subplot.hist(bins = int) # method
________________________________________________________________________________


BOXPLOTS:
# create a box-and-whiskers plot
subplot.boxplot(x) # method, takes in iterable (array, list, etc.) object

# create multiple box plots in the same figure
data = [data_1, data_2, data_3, data_4]
subplot.boxplot(data.values) # .values attribute returns the data as a numpy object
________________________________________________________________________________


2. customize the appearance of the plot
# tweak the dimensions of the plotting area
fig = plt.figure(figsize = (width, height)) # takes in tuple of floats, default inches

# add subplots title
subplot.set_title(str) # method

# add x and y axis labels
subplot.set_xlabel(str)
subplot.set_ylabel(str) # method, str is the label

# add a legend and specify its location
subplot.legend(loc = str) # str is the location
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

# set x and y ticks values
subplot.set_xticks([ticks]) # method, ticks is a list of values
subplot.set_yticks([ticks])

# set x and y ticks labels
subplot.set_xticklabels([label]) # method, label is a list of labels
subplot.set_yticklabels([label])

# rotate xticks
subplot.set_xticklabels(rotation = angle) # method, angle is an int
subplot.set_yticklabels(rotation = angle)

# set x and y graph max and min bounds
subplot.set_xlim(min, max) # method, min = lower bound, max = upper bound
subplot.set_ylim(min, max)
# this can be used to zoom into the plot we want by specifying limit

# delete ticks on axes
subplot.tick_params(bottom = "off", top = "off", left = "off", right = "off")

# delete the tick labels on axes
subplot.tick_params(labelbottom = 'off')

# delete spine of axes
subplot.spines["right"].set_visible(False) # acess it like a dictionary key-value pair

# shortcut method
for key,spine in ax.spines.items():
    spine.set_visible(False)

# add a horizontal line
subplot.axhline(y_value) # draws a line at that y value

# set the color of the horizontal line
subplot.axhline(c = str) # str is the color we want

# set the transparency of the horiztonal line
subplot.axhline(alpha = int) # int between 0 and 1

# add annotation and labels to the line
subplot.text(x, y, s) # x, y = position, s = the string value or label
________________________________________________________________________________


3. display and export the plot
# export before showing always
plt.savefig('filename.png') # .png, .jpg, etc.

# display the plot
plt.show() # method




`
