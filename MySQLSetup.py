import MySQLdb
import ConfigParser
from LoggingSetup import logger
import Utils

# statuses for jobs/tasks
READY = 'R'
FINISHED = 'F'

# statuses for render nodes
IDLE = 'I'
OFFLINE = 'O'

# statuses for either jobs/tasks or render nodes
STARTED = 'S'

# open config file
config = ConfigParser.RawConfigParser ()
config.read ("C:/Hydra/hydraSettings.cfg")

# get server & db names
hostname = config.get (section="database", option="host")
dbname = config.get (section="database", option="db")

# open db connection
db = MySQLdb.connect (hostname, user="root", db=dbname)
cur = db.cursor ()
cur.execute ("set autocommit = 1")

def execute (queryString):
    return cur.execute (queryString)

class AUTOINCREMENT: pass

class tupleObject:

    @classmethod
    def tableName (cls):
        return cls.__name__

    autoColumn = None

    def __init__ (self, **kwargs):
        self.__dict__['__dirty__'] = set ()
        for k, v in kwargs.iteritems ():
            self.__dict__[k] = v

    def __setattr__ (self, k, v):
        self.__dict__[k] = v
        if Utils.nonFlanged (k):
            self.__dirty__.add (k)
            logger.debug (('dirty', k, v))

    @classmethod
    def fetch (cls, whereClause = "", order = None, limit = None):
        orderClause = "" if order is None else " " + order + " "
        limitClause = "" if limit is None else " limit %d " % limit
        select = "select * from %s %s %s %s" % (cls.tableName (),
                                             whereClause,
                                                orderClause,
                                             limitClause)
        logger.debug (select)
        cur.execute (select)
        names = [desc[0] for desc in cur.description]
        return [cls (**dict (zip (names, tuple)))
                for tuple in cur.fetchall ()]

    def attributes (self):
        return filter (Utils.nonFlanged, self.__dict__.keys ())
                       
    def insert (self):
            
        names = self.attributes ()
        values = [getattr (self, name)
                  for name in names]
        nameString = ", ".join (names)
        valueString = ", ".join (len(names) * ["%s"])
        query = "insert into %s (%s) values (%s)" % (self.tableName (),
                                                     nameString,
                                                     valueString)
        logger.debug (query)
        cur.executemany (query, [values])
        if self.autoColumn:
            cur.execute ("select last_insert_id()")
            [id] = cur.fetchone ()
            self.__dict__[self.autoColumn] = id
        
    def update (self):
        names = list (self.__dirty__)
        if not names:
            return
        values = ([getattr (self, name)
                  for name in names]
                     +
                  [getattr (self, self.primaryKey)])
        assignments = ", ".join(["%s = %%s" % name
                                 for name in names])
        query = "update %s set %s where %s = %%s" % (self.tableName (),
                                                      assignments,
                                                      self.primaryKey)
        logger.debug ((query, values))
        cur.executemany (query, [values])

class Hydra_rendernode (tupleObject): 
    primaryKey = 'host'

class Hydra_rendertask (tupleObject):
    autoColumn = 'id'
    primaryKey = 'id'
    
class Hydra_job (tupleObject):
    autoColumn = 'id'
    primaryKey = 'id'

class Hydra_test (tupleObject):
    autoColumn = 'id'
    primaryKey = 'id'

class transaction:

    def __enter__ (self):
        logger.debug ("enter transaction")
        cur.execute ("set autocommit = 0")

    def __exit__ (self, errorType, value, traceback):
        if errorType is None:
            logger.debug ("commit")
            cur.execute ("commit")
        else:
            logger.debug ("rollback")
            cur.execute ("rollback")
        logger.debug ("exit transaction")
        cur.execute ("set autocommit = 1")
        
        
