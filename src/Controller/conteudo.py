from flask import Blueprint, render_template, request

# Definindo um blueprint para as rotas de criação de conteúdo
conteudo_bp = Blueprint('conteudo', __name__)

#@conteudo_bp.route('/criar_conteudo', methods=['GET', 'POST'])
@conteudo_bp.route('/criar-conteudo')
def iniciar():
    return render_template('criar_conteudo.html')

def criar_conteudo():
    if request.method == 'POST':
        tipo_conteudo = request.form['tipo_conteudo']
        # Lógica para criar o conteúdo
    return render_template('criar_conteudo.html')
