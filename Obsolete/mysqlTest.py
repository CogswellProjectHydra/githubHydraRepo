from MySQLSetup import queryDict, execute

print execute ("set autocommit = 0")
print  queryDict ("select * from Hydra_rendernode")
print execute ("commit")

