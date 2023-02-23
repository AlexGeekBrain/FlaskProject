from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello web!', 200


@app.errorhandler(404)
def error_404(error):
    return 'Страничка не найдена :('


# @app.route('/user/')
# def read_user():
#     name = request.args.get('name')
#     surname = request.args.get('surname')
#     return f"User {name or '[no name]'} {surname or '[no surname]'}"
