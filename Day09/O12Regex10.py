
import re

lno = "LCNO-KAR-73-2021-8000"

res = re.search(r'LCNO-(KAR|KER|APN|TND|MAH)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})', lno)

if res:
    print("Match found....")
    print(res.group(0))         # string that matched the regex
else:
    print("Match not found.....")
