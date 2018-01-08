import os;

def list_all_files(directory_path):
  print "----"
  paths = []
  for (dir, _, files) in os.walk(directory_path):
    for f in files:
      path = os.path.join(dir, f)
      if os.path.exists(path) and os.path.isfile(path):
        print path
        paths.append(path)

  return paths