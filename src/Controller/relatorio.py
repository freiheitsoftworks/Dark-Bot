from flask import Blueprint, render_template

# Definindo um blueprint para as rotas de relatórios
relatorio_bp = Blueprint('relatorio', __name__)

@relatorio_bp.route('/ver-relatorios')
def iniciar():
    return render_template('ver_relatorios.html')

def ver_relatorios():
    # Exemplo de relatórios, você pode substituir isso pelo banco de dados
    relatorios = [
        {'plataforma': 'YouTube', 'canais': 'Canal 1', 'data_criacao': '2024-10-01'},
        # Adicione mais relatórios
    ]
    return render_template('ver_relatorios.html', relatorios=relatorios)

#@relatorio_bp.route('/gerar_relatorio', methods=['GET', 'POST'])
def gerar_relatorio():
    # Lógica para gerar o relatório
    return render_template('gerar_relatorio.html')
