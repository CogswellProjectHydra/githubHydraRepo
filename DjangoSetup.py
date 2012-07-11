import os

"""Set up the environment so that django can run standalone"""

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoSettings'

# Temporary code for debugging
from django.db import connection
cursor = connection.cursor( )
cursor.execute("SET @@autocommit=0")
cursor.execute("SELECT @@autocommit")
autocommit = cursor.fetchone( )
print( autocommit[0] )
