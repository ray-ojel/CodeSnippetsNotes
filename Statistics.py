SAMPLING:
# Population: Set of ALL values in the dataset
# Sample: A smaller group selected from the population

# Sampling Error: Difference between the population and sample metrics
Sampling Error = parameter - statistic
# Parameter: A metric specific to a population
# Statistic: A metric speicific to a sample

# Simple random sampling (SRS)
Series.Sample(n) # Generate random numbers and use them to select a sample
#OR
DataFrame.Sample(n) # Method

# Stratified sampling
# Organize data into different groups, then SRS every group

# Cluster Sampling
# List all data sources, randomly pick only a few, then SRS every group

________________________________________________________________________________


VARIABLES:
# Quantitative Variable
# Describes HOW MUCH THERE IS of something i.e quantitiy

# Qualitative or Categorical Variables
# Descibes the Qualities of the variable like color or name

# Scales of Measurment
# The system of rules that define how each variable is measured

# Nominal Scale
# Qualitative Data, Tell Difference, No Size of Diff, No Direction of Diff (No Ordering)

# Ordinal Scale
# Qualitative Data, Ranking, Tell Diff, Tell Direction (Ordering), No Size of Diff

# Interval Scale
# Quantitative Data, Tell Diff, Tell Direction (Ordering),but no true zero

# Ratio Scale
# Quantitative Data, Tell Diff, Tell Direction (Ordering), and True zero exists
# Can measure Diff using DISTANCE or RATIO i.e 2x heavier than or 1x lighter

# Discrete Variable
# No possible value in between any two adjacent values of the variable, ex No. ppl

# Frequency Distribution Table (FDT)
# Counting how many times each unique value of a variable occurs
Series.value_counts() # Generates Freq Dist Table

# FDT for Nominal Scale
Series.value_counts().sort_index() # .sort_index(ascending=False) for desc

# FDT for Ordinal Scale
# Convert to nominal scale and use same^^

# Proportions
# Frequency of quantity (relative) over to the total number
# Usually expressed as decimal
Series.value_counts() / len(Series)
# OR
Series.value_counts(normalize = True)

# Percentages
# Proportion multiplied by 100
# Percentages and Proportion are Relative Frequencies i.e depend on total

# Percentile Rank
# Percentage of values that are equal or less than value X in a FDT
# That X value is called the yth percentile


________________________________________________________________________________
SCIPY:
# Import
from scipy.stats import *

# Find percentile 
#
