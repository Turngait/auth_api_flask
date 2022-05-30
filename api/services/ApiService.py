from datetime import datetime
import hashlib
from app import db
from models.api import Api
from config.config import MASTER_API_KEY
class ApiService:
  def __init__(self, ip, master_key) -> None:
    self.ip = ip
    self.master_key = master_key


  def add_new_api_key(self):
    api_key = self.__generate_api_key()
    api = Api(ip=self.ip, key=api_key)
    if not self.master_key == MASTER_API_KEY:
      return {"status": 403, "data": {"api_key": None, "ip": self.ip}}
    try:
      db.session.add(api)
      db.session.commit()
      return {"status": 200, "data": {"api_key": api_key, "ip": self.ip}}
    except:
      return {"status": 500, "data": {"api_key": None, "ip": self.ip}}


  def get_api_key(self):
    pass


  def change_api_key(self):
    pass


  def delete_aip_key(self):
    pass

  def __generate_api_key(self):
    initStr = str(datetime.now()) + MASTER_API_KEY
    key_hash = hashlib.md5(initStr.encode())
    return 'ongid__' + key_hash.hexdigest()

