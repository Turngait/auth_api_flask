import hashlib
from datetime import datetime
import os


def hashPass(password, paper):
  newPass = os.environ.get("PASS_HASH") + str(password) + str(paper)
  m = hashlib.md5()
  m.update(newPass.encode('utf-8'))
  return m.hexdigest()


def createPaper():
  m = hashlib.md5()
  m.update(str(datetime.utcnow()).encode('utf-8'))
  return m.hexdigest()


def createToken(email):
  mock = str(email) + os.environ.get("TOKEN_HASH") + str(datetime.utcnow())
  m = hashlib.md5()
  m.update(mock.encode('utf-8'))
  return m.hexdigest()