from email.policy import default
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SelectField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    unit = SelectField("unit", choices=["litr", "szt."], default="szt.")
    unit_price = DecimalField("unit_price", validators = [DataRequired()], default=1, places=2)
    quantity = IntegerField("quantity", validators = [DataRequired()], default=1)

class Sell(FlaskForm):
    quantity = IntegerField("quantity", default=1)


    
