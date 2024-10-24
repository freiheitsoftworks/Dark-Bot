# import cv2
# import selenium
# import pyautogui
from flask import Blueprint, render_template

bp =  Blueprint('data_collection', __name__)
@bp.route('/create',methods=['GET'])
def index():
    print("entrou")
    return render_template('create_data_collection.html')