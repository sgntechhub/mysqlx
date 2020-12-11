import fire
import dsnparse
import pymysql.cursors


def pretty(d, indent=0):
  for key, value in d.items():
    print('\t' * indent + str(key))
    if isinstance(value, dict):
      pretty(value, indent+1)
    else:
      print('\t' * (indent+1) + str(value))

class App(object):
  """Main application."""

  def diff(self, source, dest):
    r = dsnparse.parse(source)
    connection = pymysql.connect(
      host=r.host,
      user=r.username,
      password=r.password,
      db=r.paths[0],
      port=r.port,
      charset='utf8mb4',
      cursorclass=pymysql.cursors.DictCursor)
    try:
      with connection.cursor() as cursor:
        # Select table
        table = "notification"
        sql = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=%s"
        cursor.execute(sql, (table))
        table = cursor.fetchall()
        pretty(table[0])
    finally:
      connection.close()
    print(source)
    print(dest)

if __name__ == '__main__':
  fire.Fire(App)
