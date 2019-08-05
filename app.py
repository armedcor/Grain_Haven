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
    return render_template('recipepage.html', recipes=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))

    
    
# About page
@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
