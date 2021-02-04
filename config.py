import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'database-123.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'database-west'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'db1'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Welela@2018'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'heelsworld1234'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'y5SXzVojRf0PbVWiVrBmeFgoYyNJ+qldNOQKER2qiY7LKiM4dmJ0BW2XCV0FnV5DNXmWzmtjBgJUFBTaC1gjLQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
