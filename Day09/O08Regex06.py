# {}
import re

st = "baaaaaat"

# res = re.match(r'ba{3}t', st)
# res = re.match(r'ba{3,}t', st)

res = re.match(r'ba{3,6}t', st)

if res:
    print("Match found....")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found.....")
