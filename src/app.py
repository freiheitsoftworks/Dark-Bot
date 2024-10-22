from flask import Flask
from Controller.home import home
from Controller.data_collections import data_collection
from Controller.reports import reports
from Controller.contents import contents

template_dir =  'View/templates'
static_dir = 'View/static'

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Registrando os blueprints
app.register_blueprint(home)
app.register_blueprint(data_collection)
app.register_blueprint(reports)
app.register_blueprint(contents)

if __name__ == '__main__':
    app.run(debug=True)