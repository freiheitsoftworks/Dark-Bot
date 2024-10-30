from flask import Blueprint, render_template, request
from .youtube import YoutubeProfile as ytp

bp = Blueprint('profile', __name__)

@bp.route('/create')
def index():
    return render_template('create_profile.html')

@bp.route('/create', methods=['POST'])
def index():
    url = request.get_json().get('url')
    ytp.open_brave_browser()
    ytp.open_channel(url)
    print('perfil criado')
    return render_template('home.html')

