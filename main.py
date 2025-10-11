from flask import Flask, render_template, request
import os
from models import db, Recipe

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///recipes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Sample recipes for seeding
sample_recipes = [
    {
        "title": "Pasta Aglio e Olio",
        "ingredients": "400g spaghetti, 6 cloves garlic (sliced), 1/2 cup olive oil, red chili flakes, fresh parsley, salt",
        "instructions": "Cook pasta in salted boiling water until al dente. In a large pan, heat olive oil and sauté sliced garlic until golden. Add chili flakes. Toss cooked pasta in the garlic oil, add pasta water to create a light sauce. Garnish with fresh parsley and serve immediately.",
        "cooking_time": 20
    },
    {
        "title": "Classic Margherita Pizza",
        "ingredients": "Pizza dough, 200g mozzarella cheese, 4 tomatoes, fresh basil leaves, olive oil, salt",
        "instructions": "Preheat oven to 475°F. Roll out pizza dough on a floured surface. Spread crushed tomatoes, add torn mozzarella. Bake for 12-15 minutes until crust is golden. Top with fresh basil leaves and drizzle olive oil before serving.",
        "cooking_time": 25
    },
    {
        "title": "Chicken Stir Fry",
        "ingredients": "500g chicken breast (cubed), 2 bell peppers, 1 onion, 3 tbsp soy sauce, 2 tbsp sesame oil, ginger, garlic, vegetables",
        "instructions": "Heat sesame oil in a wok over high heat. Add chicken and cook until golden. Remove and set aside. Stir-fry vegetables with ginger and garlic. Add chicken back, pour soy sauce, and toss everything together for 2 minutes. Serve hot with rice.",
        "cooking_time": 30
    },
    {
        "title": "Caesar Salad",
        "ingredients": "Romaine lettuce, parmesan cheese, croutons, caesar dressing (mayo, lemon, garlic, anchovies), black pepper",
        "instructions": "Wash and chop romaine lettuce. Make dressing by mixing mayo, lemon juice, minced garlic, mashed anchovies, and black pepper. Toss lettuce with dressing, top with croutons and shaved parmesan. Serve immediately.",
        "cooking_time": 15
    },
    {
        "title": "Beef Tacos",
        "ingredients": "500g ground beef, taco seasoning, taco shells, lettuce, tomatoes, cheese, sour cream, salsa",
        "instructions": "Brown ground beef in a pan, drain excess fat. Add taco seasoning and water, simmer for 5 minutes. Warm taco shells in oven. Fill shells with beef, top with shredded lettuce, diced tomatoes, cheese, sour cream, and salsa.",
        "cooking_time": 20
    },
    {
        "title": "Vegetable Soup",
        "ingredients": "4 cups vegetable broth, carrots, celery, onions, potatoes, green beans, tomatoes, herbs (thyme, bay leaf)",
        "instructions": "In a large pot, sauté diced onions, carrots, and celery until soft. Add vegetable broth, diced potatoes, green beans, and chopped tomatoes. Bring to a boil, then reduce heat and simmer for 30 minutes. Season with thyme, bay leaf, salt, and pepper.",
        "cooking_time": 45
    },
    {
        "title": "Pancakes",
        "ingredients": "2 cups flour, 2 tbsp sugar, 2 tsp baking powder, 1 tsp salt, 2 eggs, 1.5 cups milk, 4 tbsp melted butter, maple syrup",
        "instructions": "Mix dry ingredients in a bowl. In another bowl, whisk eggs, milk, and melted butter. Combine wet and dry ingredients until just mixed (some lumps okay). Heat a griddle, pour batter to form pancakes. Flip when bubbles form. Serve with maple syrup and butter.",
        "cooking_time": 15
    },
    {
        "title": "Grilled Salmon",
        "ingredients": "4 salmon fillets, lemon, olive oil, garlic, dill, salt, pepper",
        "instructions": "Preheat grill to medium-high. Brush salmon with olive oil, season with salt, pepper, minced garlic, and fresh dill. Place salmon skin-side down on grill. Cook for 6-8 minutes, flip carefully and cook another 4-5 minutes. Squeeze fresh lemon juice over salmon before serving.",
        "cooking_time": 20
    },
    {
        "title": "Chocolate Chip Cookies",
        "ingredients": "2 cups flour, 1 tsp baking soda, 1/2 tsp salt, 1 cup butter, 3/4 cup sugar, 3/4 cup brown sugar, 2 eggs, 2 tsp vanilla, 2 cups chocolate chips",
        "instructions": "Preheat oven to 375°F. Mix flour, baking soda, and salt. In another bowl, cream butter and sugars, add eggs and vanilla. Gradually mix in dry ingredients, fold in chocolate chips. Drop spoonfuls onto baking sheet. Bake 9-11 minutes until golden. Cool before serving.",
        "cooking_time": 25
    },
    {
        "title": "Mushroom Risotto",
        "ingredients": "1.5 cups arborio rice, 500g mushrooms (sliced), 1 onion (diced), 4 cups vegetable broth (warm), 1/2 cup white wine, parmesan cheese, butter",
        "instructions": "Sauté onions in butter until soft. Add rice and toast for 2 minutes. Add white wine and stir until absorbed. Gradually add warm broth one ladle at a time, stirring constantly. In a separate pan, sauté mushrooms. Fold mushrooms into risotto, add parmesan and butter. Serve immediately.",
        "cooking_time": 35
    }
]

# Auto-initialize database on startup
with app.app_context():
    db.create_all()
    # Seed database if empty
    if Recipe.query.first() is None:
        for recipe_data in sample_recipes:
            recipe = Recipe(
                title=recipe_data['title'],
                ingredients=recipe_data['ingredients'],
                instructions=recipe_data['instructions'],
                cooking_time=recipe_data['cooking_time']
            )
            db.session.add(recipe)
        db.session.commit()
        print(f"✅ Database initialized with {len(sample_recipes)} recipes!")

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
