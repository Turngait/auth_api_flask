from datetime import datetime
import hashlib
from app import db
from models.api import Api
from logger.logger import Logger
from config.config import MASTER_API_KEY


# Service which work with api keys and check authorization to this API
class ApiService:
  def __init__(self, ip, outer_key) -> None:
    self.ip = ip
    self.outer_key = outer_key

  def check_api_key(self) -> bool:
    try:
      api = Api.query.filter_by(ip=self.ip).first()
      if api and api.key == self.outer_key:
        return True
      else:
        return False
    except:
      return False


  def add_new_api_key(self):
    api_key = self.__generate_api_key()
    api = Api(ip=self.ip, key=api_key)

    try:
      db.session.add(api)
      db.session.commit()

      logger = Logger(f"New api key for {self.ip} was added")
      logger.log()
      return {"status": 200, "data": {"api_key": api_key, "ip": self.ip}}
    except:
      return {"status": 500, "data": {"api_key": None, "ip": self.ip}}


  def get_api_key(self):
    try:
      api = Api.query.filter_by(ip=self.ip).first()

      if not api:
        return {"status": 403, "data": {"api_key": None, "msg": ["Cant find key by this ip"], "ip": self.ip}}
      
      logger = Logger(f"Get api key for {self.ip}")
      logger.log()
      return {"status": 200, "data": {"api_key": api.key, "ip": self.ip}}
    except:
      return {"status": 500, "data": {"api_key": None, "ip": self.ip}}


  def change_api_key(self):
    try:
      api_key = self.__generate_api_key()
      api = Api.query.filter_by(ip=self.ip).first()
      api.key = api_key
      db.session.add(api)
      db.session.commit()

      logger = Logger(f"Api key was changed for {self.ip}")
      logger.log()

      return {'data': {'is_success': True, 'msg': ['Api key is changed'], "ip": self.ip, "api_key": api_key}, 'status': 200}
    except:
      logger = Logger(f"Exception {self.ip}")
      logger.log()
      
      return {"status": 500, "data": {"api_key": None, "ip": self.ip}}


  def delete_aip_key(self):
    try:
      api = Api.query.filter_by(ip=self.ip).first()
      db.session.delete(api)
      db.session.commit()

      logger = Logger(f"Api key was deleted for {self.ip}")
      logger.log()

      return {'data': {'is_success': True, 'msg': ['Row was deleted'], "ip": self.ip, "api_key": None}, 'status': 200}
    except:
      logger = Logger(f"Exception {self.ip}")
      logger.log()
      
      return {"status": 500, "data": {"api_key": None, "ip": self.ip}}


  def __generate_api_key(self):
    initStr = str(datetime.now()) + MASTER_API_KEY
    key_hash = hashlib.md5(initStr.encode())
    return 'ongid__' + key_hash.hexdigest()

