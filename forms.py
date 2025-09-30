from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms import StringField, TextAreaField
from models import Recipe
class RecipeForm(FlaskForm):
    title = StringField('Recipe Title', validators=[DataRequired(), Length(max=100)])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])

    def validate_title(self, field):
        existing_recipe = Recipe.query.filter_by(title=field.data).first()
        if existing_recipe:
            raise ValidationError('Recipe with this title already exists')

