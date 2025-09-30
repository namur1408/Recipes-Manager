import flask
from flask import Blueprint, render_template, flash, redirect, request, url_for
from db_config import db
from forms import RecipeForm
from models import Recipe

recipes_bp = Blueprint('recipes', __name__)

@recipes_bp.route('/')
def index():
    all_recipes = Recipe.query.order_by(Recipe.title).all()
    return render_template('index.html', recipes=all_recipes)

@recipes_bp.route('/add', methods=['GET', 'POST'])
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        new_recipe = Recipe(
            title=form.title.data,
            ingredients=form.description.data,
            instructions=form.instructions.data
        )
        db.session.add(new_recipe)
        db.session.commit()
        flash('Recipe added successfully')
        return redirect(url_for('recipes.index'))
    elif form.is_submitted():
        flash('Please check the fields - something is wrong', 'danger')
    return render_template('add.html', form=form)

@recipes_bp.route('/delete/<int:id>', methods=['POST'])
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted successfully')
    return redirect(url_for('recipes.index'))