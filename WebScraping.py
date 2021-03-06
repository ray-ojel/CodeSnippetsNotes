GENERAL WORKFLOW:
# Get the page content and set up a new parser.
import requests
from bs4 import BeautifulSoup
response = requests.get("http://www.URL.com")
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())
________________________________________________________________________________


HYPERTEXT MARKUP LANGUAGE (HTML):
# Markup langauage, not programming langauage like python
# URL: https://developer.mozilla.org/en-US/docs/Web/HTML/Element
# Simple HTML Code
URL = '''
<html>

<head lang="en">
    <meta charset="utf-8" />
    <title>2014 Superbowl Team Stats</title>
</head>

<body>
    <table class="stats_table nav_table" id="team_stats">
        <tbody>
            <tr id="teams">
                <th></th>
                <th>SEA</th>
                <th>NWE</th>
            </tr>
            <tr id="first-downs">
                <td>First downs</td>
                <td>20</td>
                <td>25</td>
            </tr>
            <tr id="total-yards">
                <td>Total yards</td>
                <td>396</td>
                <td>377</td>
            </tr>
            <tr id="turnovers">
                <td>Turnovers</td>
                <td>1</td>
                <td>2</td>
            </tr>
            <tr id="penalties">
                <td>Penalties-yards</td>
                <td>7-70</td>
                <td>5-36</td>
            </tr>
            <tr id="total-plays">
                <td>Total Plays</td>
                <td>53</td>
                <td>72</td>
            </tr>
            <tr id="time-of-possession">
                <td>Time of Possession</td>
                <td>26:14</td>
                <td>33:46</td>
            </tr>
        </tbody>
    </table>
</body>

</html>
'''
# Head section: Rendering page, user doesn't see it 'head'
# Body section: bulk of content the use interacts with on the page 'body'
# id: Denoted by #id
# Class: Denoted by .class
# The same element can have both an ID and a class.
# We can also assign multiple classes to a single element; we just separate the classes with a space.

# Anything in between is the content of that tag
# Open tags
<tag>

# Close tags
</tag>

# Bold Tag
<b> </b>

# Title tag
<title> What to display on top of the tab</title>

# Paragraph tag
<p>Paragraph</p>

# Divider tag
<div>Content</div> # Creates a box that houses multiple tags ex: footers, sidebars, etc.
________________________________________________________________________________


REQUESTS:
# Import
import requests

# Make a Get Request for the link
page = requests.get(URL) # Method

# Display the html content of the page
content = page.content # Attribute

# Check page encoding
encoding = page.encoding

________________________________________________________________________________


BEAUTIFUL SOUP:
# extract tags from an HTML document
# Import
from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
soup = BeautifulSoup(content, 'html.parser') # BeautifulSoup object, represents the document as a nested data structure

# Display 'pretty' HTML Code
print(soup.prettify())

# Get the title tag from the document
title = soup.title

# Get the body tag from the document
body = soup.body

# Get the p tag from the body
p = body.p

# Get the string from the title tag
title_str = soup.tag.string
# OR
title_str = soup.tag.text

# Return string content of the tag
tag = tag.text # Returns printable string
________________________________________________________________________________


FIND_ALL:
# find all occurrences of a tag in the current element
soup.find_all('tag', id = opt, class_ = opt) # Method, Return a list which we can index to access the specific tag we want

# Find all occurences of body
body = soup.find_all("body") # ['body']

# Find all paragraphs
p = soup.find_all('p') # index a list to access specific paragraph

# Select first paragraph
p[0]

# HTML allows elements to have IDs, Find items using id
p = soup.find_all('p', id = 'first paragraph')[0] # Also returns as list stil have to select index

# Find items using class
P = soup.find_all('p', class_ = 'outer_class')[0]
________________________________________________________________________________


CASCADING STYLE SHEETS (CSS):
# Uses selectors to add styles to elements and classes

# Select the color red for all paragraphs
<head>
    p{
        color:red
    }
</head>

# Select color red for any paragraphs that have class
p.outer_class{
    color:red
}
# OR
.outer_class{
    color:red
}

# Select color red for any paragraph that have id='first', we use the # symbol
p#first{
    color:red
}
# OR
#first{
    color:red
}

SELECT:
# Select the elements
soup.select('#id .class tag') # Returns list we can index

# Select class
soup.select('.class')

# Select id
soup.select('#id')

# Target any paragraph inside div tag selector:
soup.select('div p')

# Target any item inside a div tag that has a class:
soup.selectdiv('.class')

# Select any item inside a div tag inside a body tag but only if it also has the id
soup.selectbody('div #id')

# Select any items with the ID that are inside any items with the class
soup.select('.class #id')

# Select any item with ID inside body inside tag
soup.select('body tag#id') # right next to it no spaces
