from flask import Blueprint, render_template, request


bp = Blueprint('content', __name__)
@bp.route('/create') # pode colocoar methods = ['GET...]
def index():
    return render_template('create_content.html')