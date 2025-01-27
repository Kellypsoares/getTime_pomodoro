# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
#from timer.py import pomodoro
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


#export FLASK_APP=project
#export FLASK_DEBUG=1