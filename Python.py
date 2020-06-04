# print stuff
print('Hello World')

# Print on next line
print('Hello\nWorld')

# Index lists
list[index]

# Index dictionary
dict[key]

# Assign new dict key value
dict[key] = value

# Delete list, elements, variables
del obj

# Add new items to list
list.append(item) # Method

# Python's built-in functions to analyze data in lists:
min()
max()
sorted()

# Use python's built-in with another function inside
def func(param):
    return whatever

var = min(param, key = func) # Used to rank dictionaries and pass in Lambda functions
________________________________________________________________________________


LIST COMPREHENSIONS: # Provides a concise way of creating for loops and creating lists in a single line of code
# A list comprehension can be used where we:
# 1. Iterated over values in a list.
# 2. Performed a transformation on those values.
# 3. Assigned the result to a new list.
new_list = [] # Target Variable
for i in old_list: # For statement
    trans = i * 2 # Transformation
    new_list.append(trans)

# To transform a loop to a list comprehension, in brackets we:
# 1. Start with the target variable
# 2. Assign the code that transforms each item (Could be anything, statement, function, etc)
# 3. Continue with our for statement (without a colon).
new_list = [i * 2 for i in old_list]

# Include an if statement in a list comprehension
new_list = [i for i in old_list if i > 5] # list it at the end, add i back if i is bigger than 5
________________________________________________________________________________

LAMBDA FUNCTIONS: # Temporary functions
# Define a general function
def function(param):
    return param * 2

# To create a 'lambda function equivalent, we:
# Use the 'lambda' keyword, followed by
# The parameter and a colon, and then
# The transformation we wish to perform on our argument
lambda param: param * 2

# Ternary Operator
[on_true] if [expression] else [on_false]
