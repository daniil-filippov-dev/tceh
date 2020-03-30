# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy_example.config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    from sqlalchemy_example.models import Post, User
    from sqlalchemy_example.forms import PostForm

    if request.method == 'POST':
        print(request.form)
        form = PostForm(request.form)

        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    posts = Post.query.all()
    for post in posts:
        user_id = post.user_id
        user = User.query.filter_by(id=user_id).first()
        print(post.user_id, user)

        print(post.user)

    return render_template('home.txt', posts=posts)


if __name__ == '__main__':
    from sqlalchemy_example.models import *
    db.create_all()

    app.run()
