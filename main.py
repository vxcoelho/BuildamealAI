from flask import Flask, render_template, request, redirect, url_for, session
import os
from models import db, Recipe, MealPlan, Review
from openai import OpenAI
import google.generativeai as genai

# Setup AI client (Replit AI or Google Gemini)
# Replit AI for local dev, Google Gemini (FREE) for Railway
ai_client = None
ai_type = None

try:
    # Try Replit AI Integrations first (local dev)
    ai_integrations_key = os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY")
    ai_integrations_url = os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL")
    
    if ai_integrations_key and ai_integrations_url:
        ai_client = OpenAI(
            api_key=ai_integrations_key,
            base_url=ai_integrations_url
        )
        ai_type = "openai"
    else:
        # Use Google Gemini (completely FREE for Railway!)
        gemini_key = os.environ.get("GEMINI_API_KEY")
        if gemini_key:
            genai.configure(api_key=gemini_key)
            ai_client = genai.GenerativeModel('gemini-2.5-flash')
            ai_type = "gemini"
except Exception as e:
    print(f"Warning: AI client initialization failed: {e}")
    ai_client = None

app = Flask(__name__)

# Secret key for sessions
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

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
        "cooking_time": 20,
        "cuisine": "Italian"
    },
    {
        "title": "Classic Margherita Pizza",
        "ingredients": "Pizza dough, 200g mozzarella cheese, 4 tomatoes, fresh basil leaves, olive oil, salt",
        "instructions": "Preheat oven to 475°F. Roll out pizza dough on a floured surface. Spread crushed tomatoes, add torn mozzarella. Bake for 12-15 minutes until crust is golden. Top with fresh basil leaves and drizzle olive oil before serving.",
        "cooking_time": 25,
        "cuisine": "Italian"
    },
    {
        "title": "Chicken Stir Fry",
        "ingredients": "500g chicken breast (cubed), 2 bell peppers, 1 onion, 3 tbsp soy sauce, 2 tbsp sesame oil, ginger, garlic, vegetables",
        "instructions": "Heat sesame oil in a wok over high heat. Add chicken and cook until golden. Remove and set aside. Stir-fry vegetables with ginger and garlic. Add chicken back, pour soy sauce, and toss everything together for 2 minutes. Serve hot with rice.",
        "cooking_time": 30,
        "cuisine": "Asian"
    },
    {
        "title": "Caesar Salad",
        "ingredients": "Romaine lettuce, parmesan cheese, croutons, caesar dressing (mayo, lemon, garlic, anchovies), black pepper",
        "instructions": "Wash and chop romaine lettuce. Make dressing by mixing mayo, lemon juice, minced garlic, mashed anchovies, and black pepper. Toss lettuce with dressing, top with croutons and shaved parmesan. Serve immediately.",
        "cooking_time": 15,
        "cuisine": "American"
    },
    {
        "title": "Beef Tacos",
        "ingredients": "500g ground beef, taco seasoning, taco shells, lettuce, tomatoes, cheese, sour cream, salsa",
        "instructions": "Brown ground beef in a pan, drain excess fat. Add taco seasoning and water, simmer for 5 minutes. Warm taco shells in oven. Fill shells with beef, top with shredded lettuce, diced tomatoes, cheese, sour cream, and salsa.",
        "cooking_time": 20,
        "cuisine": "Mexican"
    },
    {
        "title": "Vegetable Soup",
        "ingredients": "4 cups vegetable broth, carrots, celery, onions, potatoes, green beans, tomatoes, herbs (thyme, bay leaf)",
        "instructions": "In a large pot, sauté diced onions, carrots, and celery until soft. Add vegetable broth, diced potatoes, green beans, and chopped tomatoes. Bring to a boil, then reduce heat and simmer for 30 minutes. Season with thyme, bay leaf, salt, and pepper.",
        "cooking_time": 45,
        "cuisine": "American"
    },
    {
        "title": "Pancakes",
        "ingredients": "2 cups flour, 2 tbsp sugar, 2 tsp baking powder, 1 tsp salt, 2 eggs, 1.5 cups milk, 4 tbsp melted butter, maple syrup",
        "instructions": "Mix dry ingredients in a bowl. In another bowl, whisk eggs, milk, and melted butter. Combine wet and dry ingredients until just mixed (some lumps okay). Heat a griddle, pour batter to form pancakes. Flip when bubbles form. Serve with maple syrup and butter.",
        "cooking_time": 15,
        "cuisine": "American"
    },
    {
        "title": "Grilled Salmon",
        "ingredients": "4 salmon fillets, lemon, olive oil, garlic, dill, salt, pepper",
        "instructions": "Preheat grill to medium-high. Brush salmon with olive oil, season with salt, pepper, minced garlic, and fresh dill. Place salmon skin-side down on grill. Cook for 6-8 minutes, flip carefully and cook another 4-5 minutes. Squeeze fresh lemon juice over salmon before serving.",
        "cooking_time": 20,
        "cuisine": "American"
    },
    {
        "title": "Chocolate Chip Cookies",
        "ingredients": "2 cups flour, 1 tsp baking soda, 1/2 tsp salt, 1 cup butter, 3/4 cup sugar, 3/4 cup brown sugar, 2 eggs, 2 tsp vanilla, 2 cups chocolate chips",
        "instructions": "Preheat oven to 375°F. Mix flour, baking soda, and salt. In another bowl, cream butter and sugars, add eggs and vanilla. Gradually mix in dry ingredients, fold in chocolate chips. Drop spoonfuls onto baking sheet. Bake 9-11 minutes until golden. Cool before serving.",
        "cooking_time": 25,
        "cuisine": "American"
    },
    {
        "title": "Mushroom Risotto",
        "ingredients": "1.5 cups arborio rice, 500g mushrooms (sliced), 1 onion (diced), 4 cups vegetable broth (warm), 1/2 cup white wine, parmesan cheese, butter",
        "instructions": "Sauté onions in butter until soft. Add rice and toast for 2 minutes. Add white wine and stir until absorbed. Gradually add warm broth one ladle at a time, stirring constantly. In a separate pan, sauté mushrooms. Fold mushrooms into risotto, add parmesan and butter. Serve immediately.",
        "cooking_time": 35,
        "cuisine": "Italian"
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
                cooking_time=recipe_data['cooking_time'],
                cuisine=recipe_data.get('cuisine', 'Other')
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
    error = None
    
    if request.method == 'POST':
        ingredients = request.form.get('ingredients', '')
        cuisine = request.form.get('cuisine', 'Any')
        time_input = request.form.get('time', '30')
        try:
            time = int(time_input) if time_input else 30
        except ValueError:
            time = 30
        
        if not ingredients:
            error = "Please enter some ingredients!"
        elif not ai_client:
            error = "AI recipe generation is not available. Please contact support."
        else:
            try:
                # Create AI prompt for recipe generation
                cuisine_text = f"{cuisine} " if cuisine and cuisine != 'Any' else ""
                prompt = f"""You are a creative chef. Create a delicious {cuisine_text}recipe using ONLY these ingredients: {ingredients}

IMPORTANT: You must ONLY use the ingredients listed above. Do NOT add any extra ingredients or suggest substitutions. Work with exactly what is provided.

The recipe should take about {time} minutes to cook.

Format your response EXACTLY like this:
Recipe Name: [creative name]
Cuisine: {cuisine if cuisine else 'International'}
Cooking Time: {time} minutes
Ingredients:
- [list ONLY the ingredients provided, with quantities]

Instructions:
[step by step cooking instructions using ONLY the provided ingredients]"""

                # Call AI API (OpenAI or Gemini)
                if ai_type == "openai":
                    # the newest OpenAI model is "gpt-5" which was released August 7, 2025. do not change this unless explicitly requested by the user
                    response = ai_client.chat.completions.create(
                        model="gpt-5",
                        messages=[
                            {"role": "system", "content": "You are a creative chef who creates delicious recipes from leftover ingredients."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    ai_text = response.choices[0].message.content
                else:  # gemini
                    response = ai_client.generate_content(prompt)
                    ai_text = response.text
                
                # Extract recipe details from AI response with improved parsing
                recipe_name = "AI-Generated Recipe"
                recipe_cuisine = cuisine if cuisine else "International"
                recipe_ingredients = []
                recipe_instructions = []
                
                # Split by sections
                if "Recipe Name:" in ai_text:
                    name_part = ai_text.split("Recipe Name:")[1].split("\n")[0]
                    recipe_name = name_part.strip()
                
                if "Ingredients:" in ai_text and "Instructions:" in ai_text:
                    ingredients_section = ai_text.split("Ingredients:")[1].split("Instructions:")[0]
                    instructions_section = ai_text.split("Instructions:")[1]
                    
                    # Parse ingredients
                    for line in ingredients_section.strip().split('\n'):
                        line = line.strip()
                        if line and not line.startswith("Cooking Time") and not line.startswith("Cuisine"):
                            recipe_ingredients.append(line)
                    
                    # Parse instructions
                    for line in instructions_section.strip().split('\n'):
                        line = line.strip()
                        if line:
                            recipe_instructions.append(line)
                
                generated_recipe = {
                    'name': recipe_name,
                    'cuisine': recipe_cuisine,
                    'cooking_time': time,
                    'ingredients': '\n'.join(recipe_ingredients) if recipe_ingredients else "See AI response above",
                    'instructions': '\n'.join(recipe_instructions) if recipe_instructions else ai_text
                }
                
                # Store recipe in session and redirect to result page
                session['generated_recipe'] = generated_recipe
                return redirect(url_for('recipe_result'))
                
            except Exception as e:
                # Show detailed error to help debug Railway issues
                error = f"AI Error: {str(e)[:200]}"
                print(f"Full AI Error: {e}")
    
    return render_template('generate.html', error=error, active_tab='generate')

@app.route('/recipe/result')
def recipe_result():
    recipe = session.get('generated_recipe')
    if not recipe:
        return redirect(url_for('generate'))
    return render_template('recipe_result.html', recipe=recipe, active_tab='generate')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html', active_tab='favorites')

@app.route('/about')
def about():
    return render_template('about.html', active_tab='about')

@app.route('/planner')
def planner():
    from datetime import datetime, timedelta
    from collections import defaultdict
    import requests
    
    # Get database recipes
    db_recipes = Recipe.query.all()
    
    # Fetch popular recipes from TheMealDB for more variety, categorized by meal type
    breakfast_recipes = []
    lunch_recipes = []
    dinner_recipes = []
    
    try:
        # Define cuisines for different meal types
        breakfast_cuisines = [('American', 6), ('British', 6)]  # 12 breakfast items
        lunch_cuisines = [('Italian', 7), ('Japanese', 7)]  # 14 lunch items
        dinner_cuisines = [('Chinese', 8), ('Mexican', 8), ('Indian', 8)]  # 24 dinner items
        
        # Fetch breakfast recipes
        for cuisine, count in breakfast_cuisines:
            response = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?a={cuisine}')
            if response.status_code == 200:
                data = response.json()
                if data.get('meals'):
                    for meal in data['meals'][:count]:
                        breakfast_recipes.append({
                            'id': f"api_{meal['idMeal']}",
                            'title': meal['strMeal'],
                            'cuisine': cuisine,
                            'cooking_time': 20,
                            'meal_type': 'breakfast',
                            'image': meal.get('strMealThumb')
                        })
        
        # Fetch lunch recipes
        for cuisine, count in lunch_cuisines:
            response = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?a={cuisine}')
            if response.status_code == 200:
                data = response.json()
                if data.get('meals'):
                    for meal in data['meals'][:count]:
                        lunch_recipes.append({
                            'id': f"api_{meal['idMeal']}",
                            'title': meal['strMeal'],
                            'cuisine': cuisine,
                            'cooking_time': 30,
                            'meal_type': 'lunch',
                            'image': meal.get('strMealThumb')
                        })
        
        # Fetch dinner recipes
        for cuisine, count in dinner_cuisines:
            response = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?a={cuisine}')
            if response.status_code == 200:
                data = response.json()
                if data.get('meals'):
                    for meal in data['meals'][:count]:
                        dinner_recipes.append({
                            'id': f"api_{meal['idMeal']}",
                            'title': meal['strMeal'],
                            'cuisine': cuisine,
                            'cooking_time': 45,
                            'meal_type': 'dinner',
                            'image': meal.get('strMealThumb')
                        })
    except Exception as e:
        print(f"Error fetching TheMealDB recipes: {e}")
    
    # Add database recipes to dinner (or categorize them if they have meal_type)
    for recipe in db_recipes:
        dinner_recipes.append(recipe)
    
    # Get current week (Monday to Sunday)
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    week_dates = [start_of_week + timedelta(days=i) for i in range(7)]
    
    # Get all meal plans for this week
    meal_plans = MealPlan.query.filter(
        MealPlan.date >= start_of_week,
        MealPlan.date < start_of_week + timedelta(days=7)
    ).all()
    
    # Organize meal plans by date and meal type
    planned_meals = defaultdict(lambda: {'breakfast': None, 'lunch': None, 'dinner': None})
    for meal_plan in meal_plans:
        planned_meals[str(meal_plan.date)][meal_plan.meal_type] = {
            'id': meal_plan.id,
            'recipe': meal_plan.recipe
        }
    
    return render_template('planner.html', 
                         breakfast_recipes=breakfast_recipes,
                         lunch_recipes=lunch_recipes,
                         dinner_recipes=dinner_recipes,
                         week_dates=week_dates,
                         planned_meals=dict(planned_meals),
                         active_tab='planner')

@app.route('/planner/add', methods=['POST'])
def add_meal_plan():
    from datetime import datetime
    import requests
    data = request.json
    recipe_id = data.get('recipe_id')
    date_str = data.get('date')
    meal_type = data.get('meal_type')
    
    # Check if this is an API recipe (starts with "api_")
    if str(recipe_id).startswith('api_'):
        # Fetch full recipe details from TheMealDB and save to database
        api_id = str(recipe_id).replace('api_', '')
        try:
            response = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={api_id}')
            if response.status_code == 200:
                data_api = response.json()
                if data_api.get('meals'):
                    meal = data_api['meals'][0]
                    
                    # Build ingredients list
                    ingredients = []
                    for i in range(1, 21):
                        ingredient = meal.get(f'strIngredient{i}')
                        measure = meal.get(f'strMeasure{i}')
                        if ingredient and ingredient.strip():
                            ingredients.append(f"- {measure} {ingredient}".strip())
                    
                    # Check if recipe already exists in database
                    existing = Recipe.query.filter_by(title=meal['strMeal']).first()
                    if existing:
                        recipe_id = existing.id
                    else:
                        # Save new recipe to database
                        new_recipe = Recipe(
                            title=meal['strMeal'],
                            ingredients='\n'.join(ingredients),
                            instructions=meal.get('strInstructions', 'No instructions available'),
                            cooking_time=30,
                            cuisine=meal.get('strArea', 'International'),
                            calories=500,  # Default values
                            protein=25,
                            carbs=50
                        )
                        db.session.add(new_recipe)
                        db.session.commit()
                        recipe_id = new_recipe.id
        except Exception as e:
            print(f"Error fetching API recipe: {e}")
            return {'success': False, 'error': str(e)}, 400
    
    # Delete existing meal plan for this slot if any
    MealPlan.query.filter_by(
        date=datetime.strptime(date_str, '%Y-%m-%d').date(),
        meal_type=meal_type
    ).delete()
    
    # Add new meal plan
    meal_plan = MealPlan(
        recipe_id=recipe_id,
        date=datetime.strptime(date_str, '%Y-%m-%d').date(),
        meal_type=meal_type
    )
    db.session.add(meal_plan)
    db.session.commit()
    
    return {'success': True, 'meal_plan_id': meal_plan.id}

@app.route('/planner/remove/<int:meal_plan_id>', methods=['DELETE'])
def remove_meal_plan(meal_plan_id):
    meal_plan = MealPlan.query.get_or_404(meal_plan_id)
    db.session.delete(meal_plan)
    db.session.commit()
    return {'success': True}

@app.route('/planner/shopping-list')
def shopping_list():
    from datetime import datetime, timedelta
    from collections import defaultdict
    
    # Get current week meal plans
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    
    meal_plans = MealPlan.query.filter(
        MealPlan.date >= start_of_week,
        MealPlan.date < start_of_week + timedelta(days=7)
    ).all()
    
    # Aggregate ingredients
    ingredient_list = []
    total_nutrition = {'calories': 0, 'protein': 0, 'carbs': 0}
    
    for meal_plan in meal_plans:
        if meal_plan.recipe.ingredients:
            ingredient_list.append(f"**{meal_plan.recipe.title}** ({meal_plan.meal_type.title()}):\n{meal_plan.recipe.ingredients}")
        
        # Add nutrition
        total_nutrition['calories'] += meal_plan.recipe.calories or 0
        total_nutrition['protein'] += meal_plan.recipe.protein or 0
        total_nutrition['carbs'] += meal_plan.recipe.carbs or 0
    
    return render_template('shopping_list.html', 
                         ingredient_list=ingredient_list,
                         total_nutrition=total_nutrition,
                         meal_count=len(meal_plans),
                         active_tab='planner')

@app.route('/recipe/<int:recipe_id>/review', methods=['POST'])
def add_review(recipe_id):
    data = request.json
    rating = data.get('rating')
    comment = data.get('comment', '')
    
    if not rating or rating < 1 or rating > 5:
        return {'success': False, 'error': 'Invalid rating'}, 400
    
    review = Review(
        recipe_id=recipe_id,
        rating=int(rating),
        comment=comment
    )
    db.session.add(review)
    db.session.commit()
    
    # Calculate new average
    avg_rating = db.session.query(db.func.avg(Review.rating)).filter(Review.recipe_id == recipe_id).scalar()
    review_count = Review.query.filter_by(recipe_id=recipe_id).count()
    
    return {
        'success': True,
        'average_rating': round(float(avg_rating), 1) if avg_rating else 0,
        'review_count': review_count
    }

# Helper function to get average rating
def get_recipe_rating(recipe_id):
    avg_rating = db.session.query(db.func.avg(Review.rating)).filter(Review.recipe_id == recipe_id).scalar()
    review_count = Review.query.filter_by(recipe_id=recipe_id).count()
    return {
        'average': round(float(avg_rating), 1) if avg_rating else 0,
        'count': review_count
    }

# Add rating to template context
@app.context_processor
def utility_processor():
    return dict(get_recipe_rating=get_recipe_rating)

if __name__ == '__main__':
    # Railway provides PORT via environment variable
    port = int(os.environ.get('PORT', 5000))
    # Disable debug in production (Railway sets RAILWAY_ENVIRONMENT)
    debug = os.environ.get('RAILWAY_ENVIRONMENT') is None
    app.run(host='0.0.0.0', port=port, debug=debug)
