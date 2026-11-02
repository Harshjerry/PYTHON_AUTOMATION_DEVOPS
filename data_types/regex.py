from pickle import GET
import re

txt = "We will mostly focus on learning regular expressions."

print(re.findall("learn", txt))
##  square brackets [] are used to find all the characters in the given string w or s 
print(re.findall("[Ws]", txt))
text = "Regular expression and regular grammar."
print(re.findall("[Rr]egular", text))


## scenarios  matching
log = """
INFO Server started
ERROR Database failed
ERRORCODE 123
CRITICAL ERROR occurred
Client 192.168.1.10 connected
FakeIP 999.999.1
Another 10.0.0.5

"""


##| `\b`    | Word boundary | and  r  start a pattern 
# Find all lines that contain the word "ERROR"
error= re.findall(r"\bERROR\b", log)
print(error)
print(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log))
status="""200 OK
404 Not Found
500InternalError"""
print(re.findall(r"\b[1-5][0-9]{2}\b", log))

# /d is used to find all the digits in the given string

## regex for full lines  to match  not  just word
import re

logs = """INFO Server started
ERROR Database failed
WARNING Disk low
CRITICAL ERROR memory leak"""

pattern = r"^.*\bERROR\b.*$"
## ^ Start of the line
## .*  Any characters (before ERROR)
## .* Any characters (after ERROR)
## $ End of the lines

matches = re.findall(pattern, logs, re.MULTILINE)

for line in matches:
    print(line)

  ## .*  Any characters (before ERROR)

##3. Extract HTTP Status Codes

log= """
GET /home 200
GET /admin 403
GET /api 500
"""
error= re.findall(r"\b[1-5]\d{2}\b", log)

# find all email addresses in a string
Contact= "admin@example.com"
email= re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", Contact)

# 8. Find Timestamps
# Log:
timestamp = "2026-06-03 10:15:22 ERROR"

date = re.findall(r"\d{4}-\d{2}-\d{2}", timestamp)
# Output:

# ['2026-06-03']


#parsing web url
text = "Visit https://api.company.com for API docs"
# The ? means:
# Previous character is optional
# So:
# http
# https
# [^\s]+
 
# The + means:
# Match anything EXCEPT whitespace
# Examples it matches:
# a
# b
# 1
# .
# /
# @
# #
# So regex keeps eating characters until it sees a space
url = re.findall(r"https?://[^\s]+", text)
print(url)