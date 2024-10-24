from flask import Blueprint, render_template

# Definindo um blueprint para as rotas de relatórios
bp = Blueprint('report', __name__)# template_folder pode ser trocado para cada modulo blueprint

@bp.route('/index')
def index():
    return render_template('index_reports.html')