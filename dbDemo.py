from MySQLdb import *

db = connect ('hydra.cpc.local', user='root')

cur = db.cursor ()

cur.execute ('select 42')

print cur.fetchall()


