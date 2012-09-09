import MySQLdb

db = MySQLdb.connect ("hydra.cpc.local", user="root", db="hydraDB")
cur = db.cursor ()
cur.execute ("set autocommit = 1")

def execute (queryString):
    return cur.execute (queryString)

def queryDict (queryString):
    cur.execute (queryString)
    return fetchallDict ()

def fetchallDict ():
    names = [desc[0] for desc in cur.description]
    return [dict (zip (names, tuple))
            for tuple in cur.fetchall ()]


