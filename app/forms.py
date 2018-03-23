from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired


class BuildStorybook(FlaskForm):
    branch = StringField('Branch', validators=[DataRequired()])
    submit = SubmitField('Build Storybook')