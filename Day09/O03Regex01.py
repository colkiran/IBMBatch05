
import re

st = "bit"
# match function - pettern to be searched in the string st
# r'pattern' = raw string
res = re.match(r'b.t', st)

if res:
    print("Match found....")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found.....")
