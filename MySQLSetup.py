import MySQLdb
import ConfigParser
from LoggingSetup import logger
import Utils

# statuses for jobs/tasks
READY = 'R'                 # ready to be run by a render node
FINISHED = 'F'              # job complete
KILLED = 'K'                # job was killed

# statuses for render nodes
IDLE = 'I'                  # ready to accept jobs
OFFLINE = 'O'               # not ready to accept jobs

# statuses for either jobs/tasks or render nodes
STARTED = 'S'               # working on a job

# open config file
config = ConfigParser.RawConfigParser ()
config.read ("C:/Hydra/hydraSettings.cfg")

# get server & db names
hostname = config.get (section="database", option="host")
dbname = config.get (section="database", option="db")

#def execute (queryString):
#    return cur.execute (queryString)

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
    def fetch (cls, whereClause = "", order = None, limit = None,
               explicitTransaction=None):
        orderClause = "" if order is None else " " + order + " "
        limitClause = "" if limit is None else " limit %d " % limit
        select = "select * from %s %s %s %s" % (cls.tableName (),
                                             whereClause,
                                                orderClause,
                                             limitClause)
        logger.debug (select)

        def doFetch (t):
            t.cur.execute (select)
            names = [desc[0] for desc in t.cur.description]
            return [cls (**dict (zip (names, tuple)))
                    for tuple in t.cur.fetchall ()]
        if explicitTransaction:
            return doFetch (explicitTransaction)
        else:
            with transaction() as t:
                return doFetch (t)

    def attributes (self):
        return filter (Utils.nonFlanged, self.__dict__.keys ())
                       
    def insert (self, transaction):
            
        names = self.attributes ()
        values = [getattr (self, name)
                  for name in names]
        nameString = ", ".join (names)
        valueString = ", ".join (len(names) * ["%s"])
        query = "insert into %s (%s) values (%s)" % (self.tableName (),
                                                     nameString,
                                                     valueString)
        logger.debug (query)
        transaction.cur.executemany (query, [values])
        if self.autoColumn:
            transaction.cur.execute ("select last_insert_id()")
            [id] = transaction.cur.fetchone ()
            self.__dict__[self.autoColumn] = id
        
    def update (self, transaction):
        
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
        transaction.cur.executemany (query, [values])

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

    def __init__(self):
        # open db connection
        self.db = MySQLdb.connect (hostname, user="root", db=dbname)
        self.cur = self.db.cursor ()
        self.cur.execute ("set autocommit = 1")
        
    def __enter__ (self):
        logger.debug ("enter transaction %s", self)
        self.cur.execute ("start transaction")
        return self

    def __exit__ (self, errorType, value, traceback):
        if errorType is None:
            logger.debug ("commit %s", self)
            self.cur.execute ("commit")
        else:
            logger.debug ("rollback %s", self)
            self.cur.execute ("rollback")
        logger.debug ("exit transaction %s", self)
        self.db.close()
