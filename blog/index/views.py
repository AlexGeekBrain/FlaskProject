from flask import Blueprint, render_template


index = Blueprint('index', __name__, url_prefix='/index', static_folder='../static')


@index.route('/')
def get_index():
    return render_template('index.html')
