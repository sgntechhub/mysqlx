class Table:
  cursor = 0
  data = []
  map = {}
  def __init__(self, table):
    self.data = table
    for col in self.data:
      self.map[col.get('COLUMN_NAME')] = col
  def find(self, colName):
    return self.map[colName]
  def __iter__(self):
        return self
  def __next__(self):
    if self.cursor == len(self.data)-1:
      raise StopIteration
    temp = self.cursor
    self.cursor += 1
    return self.data[temp]