from flask import Blueprint, render_template

bp = Blueprint('profile', __name__)

@bp.route('/create')
def index():
    return render_template('create_profile.html')

