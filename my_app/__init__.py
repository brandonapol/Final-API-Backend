from flask import Flask, render_template
from config import Config
from .api.routes import api


# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)

app.config.from_object(Config)



