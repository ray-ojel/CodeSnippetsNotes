# Import regular expressions
import re

# Source
https://docs.python.org/3.4/library/re.html

# RegExr to test Regex
https://regexr.com/

# Creating regex are called pattern, when they succeed they 'match'
pattern = r'Blue' # the r in front cancels out the '\n' escape sequences
________________________________________________________________________________


NUMERIC QUANTIFIER: # Repeat sequences
# If we have a pattern that repeats, we can also use curly brackets { and } to indicate the number of times it repeats:
pattern = r"[1-6][a-z][a-z]" = r"[1-6][a-z]{2}" # Also known as a 'Quantifier' (ABOVE)

# Matches character 'a' three, four or five times
pattern = r'a{3}'

# Matches character 'a' zero, one, two or three times
pattern = r'a{ ,3}'

# Matches character 'a' eight or more times
pattern = r'a{8, }'

# Matches character 'a' zero or more quantifier
pattern = r'a*' # Eq to a{0, }

# Matches character 'a' one or more quantifier
pattern = r'a+' # Eq to a{1, }

# Optional match character 'a' quantifier
pattern = r'a?' # Eq to a{0, 1}
EX: pattern = r'e-?mail' # matches email or e-mail
________________________________________________________________________________


CHARACTER CLASS: # Match unknown characters using regular expression
# Set Character Class
pattern = r'[fud]' # Matches f, u or d

# Number Range Character Class
pattern = r"[0-9]" # Any number from 0 to 9

# lowercase letters range character class
pattern = r"[a-e]" # Any lowercase letter from a to e

# Uppercase letters
pattern = r"[A-Z]" # Any uppercase letter from A to Z

# Any uppercase or lowercase character
pattern = r'[A-Za-z]' # Combining set and range

# Combining Set and Range Character Classes
pattern = r"[1-6][a-z][a-z]" # Matches a 0ad or 2er or any string with 1-6 number and two lowercase characters

# If we have a pattern that repeats, we can also use curly brackets { and } to indicate the number of times it repeats:
pattern = r"[1-6][a-z][a-z]" = r"[1-6][a-z]{2}" # Also known as a 'Quantifier' (ABOVE)

# Digit character class
pattern = r'\d' # Matches any digit, Eq to [0-9]

# Word character class
pattern = r'\w' # Eq to [A-Za-z0-9_], matches any digit, lower, upper and special character

# Whitespace character class
pattern = r'\s' # Matches spaces, tabs or linebreak character

# Dot character class
pattern = r'.' # Matches any character except newline

# OR Boolean operator
pattern = r'regex1|regex2' # Matches either regex1 or regex2 in string
________________________________________________________________________________


NEGATIVE CHARACTER CLASS: # Match every character except a character class
# Negative set character class
pattern = r'[^fud]' # Any character except f, u or d
pattern = r'[^1-3Z\s]' # Any character except 1, 2, 3, Z or whitespace characters

# Negative digit
pattern = r'\D' # Any character except digit characters

# Negative word
pattern = r'\W' # Any character except word characters

# Negative whitespace
pattern = r'\S' # Any character except whitespace characters
________________________________________________________________________________


ANCHORS: # matches something that isn't a character, as opposed to character classes which match specific characters.
# Word Boundary Anchor
pattern = r'\d' # Matches the position between a word character and a non-word character, or a word character and the start/end of a string.
EX: pattern = r'\bregex\b' # Matches 'regex' only

# Beginning Anchor
pattern = r'^abc' # Matches any string Beginning with abc, don't confuse with negative set, that needs [^] brakets

# End Anchor
pattern = r'abc$' # Matches any string ending with abc
________________________________________________________________________________


CAPTURE GROUP: # specify one or more groups within our match that we can access separately
pattern = r"(regex)" # The parentheses indicate that only the character pattern matched should be extracted and returned in a series.
EX: pattern = r"([1-6][a-z]{2})"

# Create a named capture group
pattern = r"(?P<Column_Name>regex)" # Returns with a column name
EX: pattern = r"(?P<Years>[1-2][0-9]{3})"

# Create multiple capture groups
pattern = r'(\w+)\s(.+)' # Matches any word separated by space then any one or more character
# Str.extract would extract word alone \1 and character alone \2

# Extract Protocol, Domain and Path from URL
pattern = r"(https?)://([\w\-\.]+)/?(.*)" # extract into three columns with multiple capture groups

# Create multiple named capture groups
pattern = r"(?P<col_1>regex_1)(?P<col_2>regex_2)?"
# What does the '?' do?
# whatever is before ? is considered optional and can match exact or some
________________________________________________________________________________


LOOKAROUNDS: # Define a character or sequence of characters that either must or must not come before or after our regex match
# Positive Lookahead
pattern = r'zzz(?=abc)' # Matches zzz only when it is followed by abc

# Negative lookahead
pattern = r'zzz(?!abc)' # Matches zzz only when it is NOT followed by abc

# Positive lookbehind
pattern = r'(?<=abc)zzz' # Matches zzz only when it is preceded by abc

# Negative lookbehind
pattern = r'(?<!abc)zzz' # Matches zzz only when it is NOT preceded by abc

# NOTES
# Inside the parentheses, the first character of a lookaround is always ?.
# If lookbehind, the next character will be <, which you can think of as an arrow head pointing behind the match.
# The next character indicates whether the lookaround is positive (=) or negative (!).
________________________________________________________________________________


BACKREFERENCE: # let us reuse parts of regular expressions to catch repeated characters and words
# Using int to refer to capture groups (REQUIRED)
pattern = r'(Hello)(Goodbye)' # Matches HelloGoodbye. (Hello) = \1, (Goodbye) = \2
pattern = r'(Hello)(Goodbye)\2\1' # Matches HelloGoodbyeGoodbyeHello

# Match double letters
pattern = r'(\w)\1' # Matches ee in eel or OO in BOOK

# Match double words with one or more spaces between them
pattern = r'\b(\w+)\b\s+\1\b'
________________________________________________________________________________


FUNCTIONS:
# Search for a pattern match
re.search(pattern, string, flags=optional) # method, returns True for match, None for no match == False

# Replace strins
re.sub(pattern, repl, string, flags=optional) # Method,

# Return all non-overlapping matches of pattern in string, as a list of strings
re.findall(pattern, string, flags= optional)

# Flags [FULL LIST](https://docs.python.org/3/library/re.html#re.A)
flag = re.I
flag = re.IGNORECASE # Attribute
________________________________________________________________________________


STRING OPERATIONS:
# Find a substring
Series.str.contains(pattern) # string method, returns True if contains, False otherwise, NaN if absent

# Find a substring but convert NaN
Series.str.contains(pattern, na = 'variable') # variable could be anything we want such as False or a str

# Find a substring but ignore case
Series.str.contains(pattern, flags = re.I)

# Extract a substring
Series.str.extract(pattern) # method

# Extract a substring and return as a DataFrame
Series.str.extract(pattern, expand = True) # method

# Defaults to first match, to extract ALL substrings
Series.str.extractall(pattern) # method, creates a DataFrame, order in which it was found
# If part of the regex isn't grouped using parantheses, (),, i.e a capture group, it won't be extracted.
________________________________________________________________________________
