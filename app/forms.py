from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, SelectField
from wtforms.validators import DataRequired


class BuildStorybook(FlaskForm):
    branch = StringField('Branch', validators=[DataRequired()])
    submit = SubmitField('Build Storybook')


class Server(FlaskForm):
    label = StringField('Tag', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    branch = StringField('Branch', validators=[DataRequired()])
    env = SelectField('Env', choices=[('feature', 'feature'),
                                      ('testing', 'testing'),
                                      ('preproduction', 'preproduction')])
    submit = SubmitField('Ready')