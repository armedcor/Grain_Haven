import os

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_parameter

# Configure Flask App and set app Variables

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'brewing_database'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

# Landing Page Route


@app.route('/')
def home_page():
    return render_template('home.html')

# Get all recipes


@app.route('/get_recipes')
def get_recipes():
    per_page = 8
    page = request.args.get(get_page_parameter(), type=int, default=1)
    recipes = mongo.db.recipes.find()
    pagination = Pagination(page=page, total=recipes.count(), per_page=per_page,
                           search=False, record_name='recipes', css_framework='bootstrap4', alignment='center')
    recipe_page = recipes.skip((page - 1) * per_page).limit(per_page)
    return render_template('recipes.html', recipe=recipe_page, pagination=pagination, recipes=mongo.db.recipes.find(),
                           styles=mongo.db.recipe_style.find())


# Render single recipe

@app.route('/recipe_single/<recipe_id>')
def recipe_single(recipe_id):
    return render_template('recipepage.html',
                         recipes=mongo.db.recipes.find
                         ({'_id': ObjectId(recipe_id)}))

# Create Recipe Route


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           styles=mongo.db.recipe_style.find())
    

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    
    recipe_name = request.form['recipe_name']
    recipe_style = request.form['recipe_style']
    batch_size = request.form['batch_size']
    fermentables = request.form['fermentables']
    hops = request.form['hops']
    mash_steps = request.form['mash_steps']
    yeast = request.form['yeast']
    comments = request.form['comments']
    image = request.form['image']
    
    recipe_form = {
        'recipe_name': recipe_name,
        'recipe_style': recipe_style,
        'batch_size': batch_size,
        'fermentables': fermentables,
        'hops': hops,
        'mash_steps': mash_steps,
        'yeast': yeast,
        'comments': comments,
        'image': image,
        'can_delete': True
    }
    
    recipes.insert_one(recipe_form)
    return redirect(url_for('get_recipes'))
    
# Edit Recipe
    
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipe=recipe)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])    
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    
    recipe_name = request.form['recipe_name']
    recipe_style = request.form['recipe_style']
    batch_size = request.form['batch_size']
    fermentables = request.form['fermentables']
    hops = request.form['hops']
    mash_steps = request.form['mash_steps']
    yeast = request.form['yeast']
    comments = request.form['comments']
    image = request.form['image']
    
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': recipe_name,
        'recipe_style': recipe_style,
        'batch_size': batch_size,
        'fermentables': fermentables,
        'hops': hops,
        'mash_steps': mash_steps,
        'yeast': yeast,
        'comments': comments,
        'image': image,
        'can_delete': True
    })
    return redirect(url_for('get_recipes'))
    
    
# Delete Recipe

@app.route('/remove_recipe/<recipe_id>')
def remove_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


# About page


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
