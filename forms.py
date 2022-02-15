from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField

class ToDoForm(FlaskForm):
    #title = StringField()
    zadanie = StringField()
    #description = TextAreaField()
    opis = TextAreaField()
    #done = BooleanField()
    status = StringField()
 