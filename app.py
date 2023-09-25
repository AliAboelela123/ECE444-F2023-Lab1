from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime

class Form(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your email?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
    

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/',  methods=['GET', 'POST'])
def index():
    form = Form()
    if form.validate_on_submit():
        oldName, oldEmail = session.get('name'), session.get('email')
        if ((form.email.data).find('utoronto') != -1):
            session['uoftEmail'] = True
        else:
            session['uoftEmail'] = False
        if oldName is not None and oldName != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        if oldEmail is not None and oldEmail != form.email.data:
            flash('Looks like you have changed your email!')
        session['email'] = form.email.data
        return redirect(url_for('index'))
    return render_template('index.html', uoftEmail=session.get('uoftEmail'), form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())