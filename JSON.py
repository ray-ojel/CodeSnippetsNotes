# JSON JavaScript Object Notation
# Import
import json

# Conversion Table
# JSON              Python
# object            dict
# array             list
# string            str
# number (int)      int
# number (real)     float
# true              True
# false             False
# null              None

# Read a JSON file
file = open("file.json")
json.load(file) # Method, used to load a file object and convert to python object

# convert JSON data contained in a STRING to the equivalent set of Python object
json.loads(str) # Method, str == JSON string, 'load string' converts according to conversion table above

# Create a string from a JSON object
json.dumps(obj, sort_keys = True, indent = 4) # method, obj == JSON obj, returns string

# 


________________________________________________________________________________
