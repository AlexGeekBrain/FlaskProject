from blog.app import create_app

from blog.models.database import db


app = create_app()


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )
    

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('done!')


@app.cli.command('create-users')
def create_users():
    from blog.models import User
    admin = User(username='admin', is_staff=True)
    alex = User(username='Alex')

    db.session.add(admin)
    db.session.add(alex)
    db.session.commit()

    print('users created!')


@app.cli.command('create-articles')
def create_articles():
    from blog.models import Article
    sometitle = Article(title='Sometitle', text='sometext')
    test = Article(title='test', text='text')

    db.session.add(sometitle)
    db.session.add(test)
    db.session.commit()

    print('articles created!')
