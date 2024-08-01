
# ( )  grouping
import re

st = "boat"

res = re.match(r'b(ai|es|oa)t', st)

if res:
    print("Match found....")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found.....")
