# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'asdfsdfssf asf dsgsdg',

    # Database settings:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False,

    WTF_CSRF_ENABLED = False
)

db = SQLAlchemy(app)


class First(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))

    def __str__(self):
        return '<First %r>' % self.data


class Second(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_id = db.Column(
        db.Integer,
        db.ForeignKey('first.id'),
        nullable=False,
        index=True
    )
    first = db.relationship(First, foreign_keys=[first_id, ])

    data = db.Column(db.String(120))

    def __str__(self):
        return '<Second %r>' % self.data


if __name__ == '__main__':
    db.create_all()

    f = First(name='one')
    db.session.add(f)

    s = Second(first=f, data='some_data')

    db.session.add(s)
    db.session.commit()

    all_seconds = Second.query.all()
    for second in all_seconds:
        print(second.id, second.first_id, second.data)
        print(second.id, second.first.name, second.first.id)
        print()
