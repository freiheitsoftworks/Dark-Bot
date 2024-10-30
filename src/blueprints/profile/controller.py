from flask import Blueprint, render_template, request

from blueprints.profile.create_profile import CreateProfile

bp = Blueprint('profile', __name__)

@bp.route('/create')
def page_redirect():
    return render_template('create_profile.html')

@bp.route('/create', methods=['POST'])
def create():
    url = request.get_json().get('url')
    profile = CreateProfile.execute(url)
    print("profile:",profile)
    return render_template('home.html')

