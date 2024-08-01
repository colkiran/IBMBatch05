# ^ and $

import re

st = "hello world"

# res = re.match(r'^hello', st)
# match will search for data inp
res = re.search(r'world$', st)

if res:
    print("Match found....")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found.....")
