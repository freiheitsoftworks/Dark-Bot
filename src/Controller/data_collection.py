import cv2
import selenium
import pyautogui
from flask import Blueprint, render_template, request

# Definindo um blueprint para as rotas da data_collection
data_collection = Blueprint('data_collection', __name__)

@data_collection.route('/new-data_collection', methods=['GET', 'POST'])
def iniciar():
    return render_template('new_data_collection.html')

def nova_data_collection():
    if request.method == 'POST':
        plataforma = request.form['plataforma']
        canais = request.form['canais']
        # Lógica de data_collection de dados
    return render_template('new_data_collection.html')