from flask import Flask
import logging
from mongoengine import connect
from config import Config  # Importar as configurações


from blueprints.data_collection.routes import bp as data_collection
from blueprints.home.routes import bp as home
from blueprints.profile.routes import bp as profile
from blueprints.report.routes import bp as report
from blueprints.content.routes import bp as content


logging.basicConfig(level=logging.DEBUG)



template_dir =  'views/templates'
static_dir = 'views/static'

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.config.from_object(Config)

app.register_blueprint(home)
app.register_blueprint(profile,url_prefix="/profile")
app.register_blueprint(data_collection,url_prefix="/data-collection")
app.register_blueprint(content,url_prefix="/content")
app.register_blueprint(report,url_prefix="/report")



if __name__ == '__main__':
    logging.debug("App is starting...")
    app.run(debug=True)
