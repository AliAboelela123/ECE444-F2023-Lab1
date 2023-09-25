from flask import Flask, render_template
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
    name = None
    email = None
    form = Form()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        email = form.email.data
        form.email.data = ''
    return render_template('index.html', form=form, name=name, email=email)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())