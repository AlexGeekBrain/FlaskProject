from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound


article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    'Title',
    'Title2',
    'Title3',
}


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
        )
