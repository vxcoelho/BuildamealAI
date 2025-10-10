from flask import Flask, render_template, request
import os
from models import db, Recipe

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///recipes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    # Get 6 random featured recipes
    recipes = Recipe.query.order_by(db.func.random()).limit(6).all()
    return render_template('home.html', recipes=recipes, active_tab='home')

@app.route('/browse')
def browse():
    recipes = Recipe.query.all()
    return render_template('browse.html', recipes=recipes, active_tab='browse')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    generated_recipe = None
    if request.method == 'POST':
        ingredients = request.form.get('ingredients', '')
        cuisine = request.form.get('cuisine', 'Any')
        time = int(request.form.get('time', 30))
        
        # Simple AI simulation - pick a random recipe for now
        # In future, this will use actual AI
        sample_recipe = Recipe.query.order_by(db.func.random()).first()
        if sample_recipe:
            generated_recipe = {
                'name': f"AI-Generated {cuisine} Recipe",
                'cuisine': cuisine if cuisine else 'International',
                'cooking_time': time,
                'ingredients': ingredients + " (AI will suggest more ingredients)",
                'instructions': "AI-generated instructions coming soon! For now, here's a sample: " + sample_recipe.instructions
            }
    
    return render_template('generate.html', generated_recipe=generated_recipe, active_tab='generate')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html', active_tab='favorites')

@app.route('/about')
def about():
    return render_template('about.html', active_tab='about')

if __name__ == '__main__':
    # Railway provides PORT via environment variable
    port = int(os.environ.get('PORT', 5000))
    # Disable debug in production (Railway sets RAILWAY_ENVIRONMENT)
    debug = os.environ.get('RAILWAY_ENVIRONMENT') is None
    app.run(host='0.0.0.0', port=port, debug=debug)
