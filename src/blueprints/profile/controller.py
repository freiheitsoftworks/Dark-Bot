import time
from flask import Blueprint, render_template, request, flash

from utils.enums import Platform
from . create_profile import CreateProfile

bp = Blueprint('profile', __name__)

@bp.route('/create')
def page_redirect():
    platforms = [platform.value for platform in Platform]
    return render_template('create_profile.html', platforms=platforms)

@bp.route('/create', methods=['POST'])
def create():
    url = request.form.get('url')
    platform = request.form.get('platform')
    response = CreateProfile.execute(url, platform)
    if response.status != 200: 
        print("response:",response)
        flash(response.message, 'info')
        time.sleep(5)
        return page_redirect()
    print("response:",response)
    flash(response, 'info')
    return render_template('home.html')