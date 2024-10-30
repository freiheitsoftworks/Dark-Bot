from flask import Flask
import logging
from mongoengine import connect
from config import Config  # Importar as configurações

from blueprints.data_collection.controller import bp as data_collection
from blueprints.home.controller import bp as home
from blueprints.profile.controller import bp as profile
from blueprints.report.controller import bp as report
from blueprints.content.controller import bp as content

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("pymongo").setLevel(logging.WARNING)

template_dir =  'views/templates'
static_dir = 'views/static'

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.config.from_object(Config) # ja aplica o secret key, e o uri do mongo
connect(host=app.config["MONGODB_SETTINGS"]["host"])


app.register_blueprint(home)
app.register_blueprint(profile,url_prefix="/profile")
app.register_blueprint(data_collection,url_prefix="/data-collection")
app.register_blueprint(content,url_prefix="/content")
app.register_blueprint(report,url_prefix="/report")

if __name__ == '__main__':
    logging.debug("App is starting...")
    app.run(debug=True)
