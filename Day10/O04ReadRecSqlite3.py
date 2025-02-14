
import sqlite3
from prettytable import PrettyTable, from_db_cursor

conn = sqlite3.connect("playersdb.sqlite3")

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

prtyTbl = from_db_cursor(cursor)

prtyTbl.align['plyname'] = "l"
prtyTbl.align['achievements'] = 'l'
prtyTbl.align['sport'] = "r"

print(prtyTbl)

conn.close()
