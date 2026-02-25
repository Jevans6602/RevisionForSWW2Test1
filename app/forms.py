from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,SubmitField, DateField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class GameForm(FlaskForm):
    title = StringField("Enter the title of the game:", validators=[DataRequired(), Length(0, 20)])
    genre = SelectField("Genre:",
                        choices=[('action', 'Action'), ('rpg', 'RPG'), ('horror', 'Horror'), ('multiplayer', 'Multiplayer')],
                        validators = [DataRequired()])
    rating = IntegerField("Rating (1-5):", validators=[DataRequired(), NumberRange(1,5)])
    submit = SubmitField("Add")

