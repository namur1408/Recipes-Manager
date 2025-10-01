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
            ingredients=form.ingredients.data,
            instructions=form.instructions.data
        )
        db.session.add(new_recipe)
        db.session.commit()
        flash('Recipe added successfully', 'success')
        return redirect(url_for('recipes.index'))
    elif form.is_submitted():
        flash('Recipe with this title already exist', 'danger')
    return render_template('add.html', form=form)

@recipes_bp.route('/recipe/<int:id>')
def recipe(id):
    r = Recipe.query.get_or_404(id)
    return render_template('recipe.html', recipe=r)

@recipes_bp.route('/delete/<int:id>', methods=['POST'])
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted successfully', 'success')
    return redirect(url_for('recipes.index'))

@recipes_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    form = RecipeForm(obj=recipe)
    if form.validate_on_submit():
        form.populate_obj(recipe)
        db.session.commit()
        flash('Recipe updated successfully.', 'success')
        return redirect(url_for('recipes.index'))
    elif form.is_submitted():
        flash('Please add "(Updated)" in the end of the title, or whatever you want', 'warning')
    return render_template('edit.html', form=form, recipe=recipe)