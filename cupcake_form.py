"""Forms for new pet app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, ValidationError
from wtforms.validators import InputRequired, Optional, url


class AddcupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    flavor = StringField("Flavor", validators=[InputRequired(message='Whats your favorite flavor?')])

    size = SelectField(
                choices=[('s', 'Small'), ('m', 'Medium'), ('l', 'Large') ],
                validators=[InputRequired()])

    rating = IntegerField("Rating", validators=[InputRequired()])
    image = StringField("Image_URL", validators= [url()])
