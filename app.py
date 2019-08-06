import os

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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
    return render_template('recipes.html', recipes=mongo.db.recipes.find())


# Render single recipe

@app.route('/recipe_single/<recipe_id>')
def recipe_single(recipe_id):
    return render_template('recipepage.html',
                         recipes=mongo.db.recipes.find
                         ({'_id': ObjectId(recipe_id)}))

# Create Recipe Route


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html')
    

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
        'image': image
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
        'image': image
    })
    return redirect(url_for('get_recipes'))


# About page
@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
