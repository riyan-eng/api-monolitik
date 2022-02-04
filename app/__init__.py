import psycopg2.extras
from flask import Flask
from config import Config, db_query
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cur_query =  db_query.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

from app.models import user
from app import routes