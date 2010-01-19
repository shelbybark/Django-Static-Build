from settings_common import *
import os
PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PROJECT_DIR, 'db/site.db')


#MEDIA_URL = 'http://127.0.0.1:8000/media/'
MEDIA_URL = '/media/'
