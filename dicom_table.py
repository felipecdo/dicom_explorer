# mocked
class DicomTable:
  def __init__(self, headers):
    self.headers = headers
    self.rows = []
  def get_headers(self):
    return self.headers
  def get_rows(self):
    return self.rows
  
  def add_row(self, row):
    if len(row) != len(self.headers):
      raise "bad row length!"
    self.rows.append(row)

  @staticmethod
  def from_files(all_files):
    table = DicomTable(["column A", "column B", "column C"])
    for filename in all_files:
      row = [filename, 'a',1]
      table.add_row(row)
    return table