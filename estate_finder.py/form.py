from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    SubmitField,
    SelectField, EmailField,
    PasswordField, BooleanField
)
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError
)
from flask_wtf.file import FileField, FileAllowed
from estate_finder.models import User


class PropertyForm(FlaskForm):
    propertyImage = FileField(
             'Property Image URL', validators=[FileAllowed(['jpg', 'png'])])
    propertyStatus = SelectField(
             'Property Status', choices=[
                  ('For Rent', 'For Rent'),
                  ('For Sale', 'For Sale')], validators=[DataRequired()])
    property_type = SelectField(
             'Property Type', choices=[
                  ('Apartment', 'Apartment'),
                  ('Villa', 'Villa'),
                  ('Home', 'Home'),
                  ('Building', 'Building'),
                  ('Office', 'Office'),
                  ('Townhouse', 'Townhouse'),
                  ('Shop', 'Shop'),
                  ('Garage', 'Garage')], validators=[DataRequired()])
    propertyPrice = StringField('Property Price(KSH)', validators=[DataRequired()])
    propertyLocation = SelectField(
             'Property Type', choices=[
                  ('Ruiru', 'Ruiru'),
                  ('Westlands', 'Westlands'),
                  ('Karen', 'Karen'),
                  ('Kilimani', 'Kilimani'),
                  ('Muthaiga', 'Muthaiga'),
                  ('Parklands', 'Parklands'),
                  ('Kahawa', 'Kahawa'),
                  ('Kasarani', 'Kasarani'),
                  ('Utawala', 'Utawala')], validators=[DataRequired()])
    propertySize = IntegerField('Property Size (Sqft)', validators=[DataRequired()])
    propertyBedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])
    propertyBathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    submit = SubmitField('Add ')


class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired()])
    password = PasswordField(
         'Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('login')


class RegistrationForm(FlaskForm):
    username = StringField(
         'username', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken.\
                                  Please choose\
                                  another username')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already exists!')
