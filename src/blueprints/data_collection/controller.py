from flask import Blueprint, render_template
from . youtube_data_collection import YoutubeDataCollection as ytdt
import time

bp =  Blueprint('data_collection', __name__)
@bp.route('/create',methods=['GET'])
def index():
    print("entrou")
    return render_template('create_data_collection.html')

@bp.route('/create',methods=['POST'])
def create():
    print("iniciou coleta")
    ytdt.openBraveBrowser()
    return