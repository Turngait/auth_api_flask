from datetime import datetime

class Logger:
  def __init__(self, msg, level="info", filename="logs") -> None:
    self.filename = filename
    self.date = datetime.now()
    self.msg = msg
    self.level = level

  def log(self):
    try:
      fo = open(self.filename, "a+")
      fo.write(f"{self.level}: {self.msg} --{self.date}--\n")
      fo.close()
      return True
    except:
      return False

