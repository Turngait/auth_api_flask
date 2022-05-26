from config.config import DB_NAME, DB_PASS


db_config = {
  'mysql': 'mysql://root:{db_pass}@db/{db_name}'.format(db_pass=DB_PASS, db_name=DB_NAME),
}
