from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


app = Flask(__name__, template_folder='templates')
app.config.update(
    DEBUG=True,
    SECRET_KEY='should always be secret',

    # Database settings:
    SQLALCHEMY_DATABASE_URI='sqlite:///people.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,

    WTF_CSRF_ENABLED=False
)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    job = db.Column(db.String(50))

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'job': self.job
        }


@app.route('/')
def index():
    # It is pretty easy for some tasks:
    people = Person.query.all()
    by_name = Person.query.filter_by(name='Sveta').first()
    by_age = Person.query.filter(Person.age >= 30)
    by_job = Person.query.filter(Person.job == 'HR')

    # And not so easy for others:
    sub = db.session.query(
        func.min(Person.age).label('min_age')
    ).subquery()
    youngest = Person.query.join(
        sub, sub.c.min_age == Person.age
    ).first()

    return jsonify({
        'people': [p.to_json() for p in people],
        'by_name': by_name.to_json(),
        'by_age': [p.to_json() for p in by_age],
        'by_job': [p.to_json() for p in by_job],

        'youngest': youngest.to_json(),
    })

if __name__ == '__main__':
    db.create_all()

    # Deleting all records:
    Person.query.delete()

    # Creating new ones:
    ivan = Person(name='Ivan', age=3)
    sveta = Person(name='Sveta', age=30, job='HR')
    semen = Person(name='Semen', age=32, job='IT')
    kolya = Person(name='Kolya', age=23, job='HR')

    db.session.add(ivan)
    db.session.add(sveta)
    db.session.add(kolya)
    db.session.add(semen)
    db.session.commit()  # note

    # Running app:
    app.run()
