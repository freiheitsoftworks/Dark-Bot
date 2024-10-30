from flask import Blueprint, render_template, request
from .youtube import YoutubeDataCollection as ytdt

bp =  Blueprint('data_collection', __name__)
@bp.route('/create',methods=['GET'])
def index():
    return render_template('create_data_collection.html')

@bp.route('/create', methods=['POST'])
def create():
    url = request.get_json().get('url') # request.get_json() (json normal) != request.form (form data)
    ytdt.open_brave_browser()
    ytdt.open_channel(url)
    return render_template('home.html')