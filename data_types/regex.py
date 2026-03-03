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


## regex for full lines  to match  not  just word
import re

logs = """INFO Server started
ERROR Database failed
WARNING Disk low
CRITICAL ERROR memory leak"""

pattern = r"^.*\bERROR\b.*$"
## .*  Any characters (before ERROR)
## .* Any characters (after ERROR)

matches = re.findall(pattern, logs, re.MULTILINE)

for line in matches:
    print(line)

  ## .*  Any characters (before ERROR)