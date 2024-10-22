from flask import Blueprint, render_template, request

# Definindo um blueprint para as rotas de criação de conteúdo
content = Blueprint('content', __name__)

#@content_bp.route('/criar_content', methods=['GET', 'POST'])
@content.route('/content',methods=['GET'])
def iniciar():
    return render_template('generate_content.html')

@content.route('/content',methods=['POST'])
def generate_content():
    name = request.form['tipo_content']
    return "Hello World, "+name+"!"
