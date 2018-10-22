from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, InputRequired

class Registration(FlaskForm):
	fname = StringField('First Name',
							validators=[InputRequired(), Length(min=2, max=20)])
	lname = StringField('Last Name',
							validators=[InputRequired(), Length(min=2, max=20)])
	username = StringField('Username',
							validators=[InputRequired(), Length(min=5, max=16)])
	email = StringField('Email',
							validators=[InputRequired(), Email()])
	password = PasswordField('Password',
							validators=[InputRequired(), EqualTo('confirm_password', message='Passwords do not match,')])
	confirm_password = PasswordField('Confirm Password',
							validators=[InputRequired()])

#def validate_username(self, username):
	#user = User.query.filter_by(username=username.data).first()
	#if user:
		#raise ValidationError('That username already exists! Please use a different one.')

#def validate_email(self, email):
	#user = User.query.filter_by(email=email.data).first()
	#if user:
		#raise ValidationError('That e-mail is already in use! Please use a different one.')


class LogIn(FlaskForm):
	email = StringField('Email',
							validators=[InputRequired(), Email()])
	password = PasswordField('Password',
							validators=[InputRequired()])
	remember = BooleanField('Remember Me')

class AddVenue(FlaskForm):
	room = StringField('Room Name',
							validators=[DataRequired()])
	college = StringField('College',
							validators=[DataRequired()])
	location = StringField('Location',
							validators=[Optional()])
	capacity = IntegerField('Capacity',
							validators=[Optional()])
	rate = IntegerField('Rate',
							validators=[Optional()])
	equipment = StringField('Equipment',
							validators=[Optional()])
	submit = SubmitField('Add Venue')


