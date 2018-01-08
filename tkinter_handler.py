from Tkinter import *
from tkFileDialog import askdirectory
from table import Table

class TkinterHandler:
  def __init__(self):
    self.tk = Tk()

  def draw_explorer(self):
    directory_path = askdirectory() # show an "Open" dialog box and return the path to the selected file
    return directory_path

  def draw_table(self, headers, rows):
      root = self.tk

      my_table = Table(root, headers, column_minwidths=[None, None, None])
      my_table.pack(expand=True, fill=X, padx=10,pady=10)

      my_table.set_data(rows)
      my_table.cell(0,0, " a fdas fasd fasdf asdf asdfasdf asdf asdfa sdfas asd sadf ")
      root.mainloop()