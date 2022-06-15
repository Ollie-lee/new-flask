import os
from forms import AddForm, DelForm, AddCompanyForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

# SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Tutor(db.Model):

    __tablename__ = 'tutors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    company = db.relationship('Company', backref='tutor', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.company:
            return f"Tutor name is {self.name} and company is {self.company.name}"
        else:
            return f"Tutor name is {self.name} and has no company assigned yet."


class Company(db.Model):

    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # We use tutors.id because __tablename__='tutors'
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))

    def __init__(self, name, tutor_id):
        self.name = name
        self.tutor_id = tutor_id

    def __repr__(self):
        return f"Company Name: {self.name}"
############################################

        # VIEWS WITH FORMS

##########################################


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_tut():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Tutor to database
        new_tut = Tutor(name)
        db.session.add(new_tut)
        db.session.commit()

        return redirect(url_for('list_tut'))

    return render_template('add.html', form=form)


@app.route('/add_company', methods=['GET', 'POST'])
def add_company():

    form = AddCompanyForm()

    if form.validate_on_submit():
        name = form.name.data
        tut_id = form.tut_id.data
        # Add new company to database
        new_company = Company(name, tut_id)
        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for('list_tut'))

    return render_template('add_company.html', form=form)


@app.route('/list')
def list_tut():
    # Grab a list of tutors from database.
    tutors = Tutor.query.all()
    return render_template('list.html', tutors=tutors)


@app.route('/delete', methods=['GET', 'POST'])
def del_tut():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        tut = Tutor.query.get(id)
        db.session.delete(tut)
        db.session.commit()

        return redirect(url_for('list_tut'))
    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
