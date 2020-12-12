import fire
import dsnparse
import pymysql.cursors
from app.table import Table


def pretty(d, indent=0):
  for key, value in d.items():
    print('\t' * indent + str(key))
    if isinstance(value, dict):
      pretty(value, indent+1)
    else:
      print('\t' * (indent+1) + str(value))
      
def compareColumn(src, dst):
  pass

def getConn(dsn):
  r = dsnparse.parse(dsn)
  conn = pymysql.connect(
    host=r.host,
    user=r.username,
    password=r.password,
    db=r.paths[0],
    port=r.port,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
  return conn

def getTable(conn, table):
  with conn.cursor() as cursor:
    sql = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=%s"
    cursor.execute(sql, (table))
    return cursor.fetchall()
class App(object):
  """Main application."""

  def diff(self, source, dest):
    """diff compare two schemas

    Args:
      source (string): a DSN of source MySQL
      dest (string): a DSN of dest MySQL 
    """    
    srcConn = getConn(source)
    dstConn = getConn(dest)
    table1 = getTable(srcConn, "notification")
    table2 = getTable(dstConn, "notification")
    t1 = Table(table1)
    for col1 in t1:
      pretty(col1)
    print(source)
    print(dest) 

if __name__ == '__main__':
  fire.Fire(App)
