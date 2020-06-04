# import
import seaborn as sns
________________________________________________________________________________


# general workflow
1. create a plot using data

HISTOGRAM:
# Create a histogram with Kernel density plot
sns.distplot(data) # method,accepts series

# change the number of bins used
sns.distplot(bins = int)
________________________________________________________________________________


KERNEL DENSITY PLOT:
# create a KNP
sns.kdeplot(data) # method, aceepts Series

# shade in the area under the KNP
sns.kdeplot(shade = True)
________________________________________________________________________________


SMALL MULTIPLES: # plots in the same figure that share the same axes
# Condition on one unique values of the column.
g = sns.FacetGrid(DataFrame, col = str)

# For each subset of values, generate a kernel density plot of columns.
g.map(sns.plottype, col, shade=True)

# change the size of the FacetGrid
sns.FacetGrid(size = int) # method, size of the grid in inches

# add a legend
g.map(sns.plottype, col).add_legend() # method chaining

# create plots on two conditons:
g = sns.FacetGrid(DataFrame, col = str, row = str) # str == name col/row, size of grid matches

# create plots on three conditions:
g = sns.FacetGrid(DataFrame, col = str, row = str, hue = str) # hue accepts col data just like the other two
________________________________________________________________________________


VISUALIZING MISSING DATA:
sns.heatmap(DataFrame.isnull(), cbar = False)
________________________________________________________________________________


2. customize the appearance of the plot
# set the style of the plot
sns.set_style(style) # pick style from below, may be some more
# darkgrid: Coordinate grid displayed, dark background color
# whitegrid: Coordinate grid displayed, white background color
# dark: Coordinate grid hidden, dark background color
# white: Coordinate grid hidden, white background color
# ticks: Coordinate grid hidden, white background color, ticks visible

# remove all the axes spines
sns.despine(left = True, bottom = True) # only removes top and right, so we add boolean
________________________________________________________________________________


3. display and export the plot
# display the plot
plt.show()
