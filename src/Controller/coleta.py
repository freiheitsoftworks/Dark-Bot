from flask import Blueprint, render_template, request

# Definindo um blueprint para as rotas da coleta
coleta_bp = Blueprint('coleta', __name__)

@coleta_bp.route('/nova-coleta', methods=['GET', 'POST'])
def iniciar():
    return render_template('nova_coleta.html')

def nova_coleta():
    if request.method == 'POST':
        plataforma = request.form['plataforma']
        canais = request.form['canais']
        # Lógica de coleta de dados
    return render_template('nova_coleta.html')
