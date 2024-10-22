from flask import Blueprint, render_template

# Definindo um blueprint para as rotas de relatórios
report = Blueprint('report', __name__)

@report.route('/ver-reports')
def iniciar():
    return render_template('ver_reports.html')

def ver_reports():
    # Exemplo de relatórios, você pode substituir isso pelo banco de dados
    reports = [
        {'plataforma': 'YouTube', 'canais': 'Canal 1', 'data_criacao': '2024-10-01'},
        # Adicione mais relatórios
    ]
    return render_template('ver_reports.html', reports=reports)

#@report_bp.route('/gerar_report', methods=['GET', 'POST'])
def gerar_report():
    # Lógica para gerar o relatório
    return render_template('gerar_report.html')
