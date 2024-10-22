import os
from flask import Flask
from Controller.home import home_bp
from Controller.coleta import coleta_bp
from Controller.relatorio import relatorio_bp
from Controller.conteudo import conteudo_bp

template_dir =  'View/templates'
static_dir = 'View/static'

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Registrando os blueprints
app.register_blueprint(home_bp)
app.register_blueprint(coleta_bp)
app.register_blueprint(relatorio_bp)
app.register_blueprint(conteudo_bp)

if __name__ == '__main__':
    app.run(debug=True)