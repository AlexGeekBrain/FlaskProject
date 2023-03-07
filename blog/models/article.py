from sqlalchemy import Column, Integer, String, Text

from blog.models.database import db


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(Text)

    def __repr__(self):
        return f'<Article #{self.id} {self.title}>'
    