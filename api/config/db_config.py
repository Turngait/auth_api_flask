import os


db_config = {
  'mysql': 'mysql://root:{db_pass}@db/{db_name}'.format(db_pass=os.environ.get("DB_PASS"), db_name=os.environ.get("DB_NAME")),
}
