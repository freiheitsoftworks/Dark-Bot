from flask import Blueprint, render_template

# Definindo um blueprint para as rotas da home
home = Blueprint('home',__name__)

@home.route('/')
def home():
    return render_template('home.html')