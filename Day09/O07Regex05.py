# +
import re

st = "bat"

res = re.match(r'ba+t', st)

if res:
    print("Match found....")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found.....")
