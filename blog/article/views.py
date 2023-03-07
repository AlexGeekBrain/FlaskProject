from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import Article


article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/')
def article_list():
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
        )


@article.route('/<int:pk>')
def article_details(pk: int):
    article = Article.query.filter_by(id=pk).one_or_none()
    if article is None:
        raise NotFound(f'Статья #{pk} не найдена!')
    return render_template(
        'articles/details.html',
        article=article,
        )
