import fire
import dsnparse
import pymysql.cursors

class App(object):
  """Main application."""

  def diff(self, source, dest):
    r = dsnparse.parse(source)
    print(r.scheme)  # prom.interface.postgres.Interface
    print(r.username)  # testuser
    print(r.password)  # testpw
    print(r.host)  # localhost
    print(r.port)  # 1234
    print(r.hostloc)  # localhost:1234
    print(r.paths)  # ['testdb']
    print(source)
    print(dest)

if __name__ == '__main__':
  fire.Fire(App)
