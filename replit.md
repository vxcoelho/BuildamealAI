# Build A Meal

## Overview

Build A Meal is an AI-powered recipe generator web application built with Flask and PostgreSQL. The application features a modern orange and black luxury design with tab-based navigation across 5 main sections: Home (featured recipes), Browse Recipes (full recipe collection), AI Generator (custom recipe generation), My Favorites (planned feature), and About.

**Tech Stack:**
- **Backend:** Python Flask web framework
- **Database:** PostgreSQL with SQLAlchemy ORM
- **Frontend:** HTML with inline CSS, Jinja2 templating
- **Server:** Flask development server (Gunicorn for production via Railway)
- **Deployment:** Railway-ready with Procfile

## Recent Changes

### October 12, 2025 - Luxury Design Overhaul & Animated Hero
- **Branding Update:** Changed from "Build A Meal" to "Build a Meal" (lowercase 'a')
- **Animated Hero Background:** Cinematic cooking scene with zoom/pulse animation and gradient color shifts
- **Floating Particles:** 4 animated particles with opacity fading for dynamic visual interest
- **Ripple Button Effects:** CTA button with expanding ripple animation on hover
- **Cinematic Animations:** Smooth fade-in sequences, staggered feature card reveals
- **High-End Aesthetic:** Professional food photography, gradient overlays, luxury typography
- **Performance Optimized:** CSS-only animations, no heavy JavaScript
- **Clean Logo:** Text-only branding with gradient effect (no images)

### October 12, 2025 - Unlimited Recipe Search via TheMealDB API
- **TheMealDB Integration:** Connected to free, unlimited recipe database (no API key required)
- **Thousands of Recipes:** Access to real recipes from around the world via internet API
- **26 World Cuisines:** Dropdown filter with American, British, Chinese, French, Indian, Italian, Japanese, Mexican, Thai, Vietnamese, and 16+ more
- **3 Search Modes:**
  - **Cuisine Only:** Browse all recipes from selected cuisine (e.g., "Italian")
  - **Text Search Only:** Find recipes by name or ingredient (e.g., "chicken soup")
  - **Combined Filter:** Select cuisine AND search by text (e.g., "Mexican" + "chicken")
- **Smart API Usage:** Limits to 12 results per cuisine filter, fetches full recipe details with ingredients/instructions
- **Empty State Design:** No recipes shown by default until user searches (clean luxury aesthetic)
- **Robust Error Handling:** Defensive null checks for all recipe fields, network error handling
- **Professional Recipe Cards:** Displays recipe images, title, cuisine/category, ingredients list, instruction preview
- **100% Free:** No API keys, no rate limits, no costs - completely free unlimited access

### October 12, 2025 - Premium Icon Upgrade
- **Professional Photography:** Replaced emoji icons with high-end stock images
- **Feature Icons:** AI technology (circuit board), Lightning (energy bolt), Globe (world cuisine)
- **Circular Design:** 100px circular frames with orange border and hover effects
- **Visual Polish:** Images scale and glow on hover for premium interaction

### October 12, 2025 - Meal Planning & Calendar Feature
- **Weekly Calendar:** Drag-and-drop meal planner with Monday-Sunday weekly view
- **Meal Organization:** Three meal types per day (breakfast, lunch, dinner) with visual calendar grid
- **Drag-and-Drop Interface:** HTML5 drag API implementation for intuitive meal planning
- **Recipe Assignment:** Drag recipes from sidebar into calendar slots to plan meals
- **Meal Removal:** One-click removal of planned meals with confirmation dialog
- **Shopping List Generation:** Automatically aggregates ingredients from all planned meals
- **Nutrition Tracking:** Added calories, protein, and carbs fields to recipes
- **Weekly Nutrition Summary:** Total and per-meal nutrition estimates on shopping list
- **Database Model:** New MealPlan table with recipe_id, date, meal_type relationships
- **API Endpoints:** RESTful endpoints for adding/removing meals (POST /planner/add, DELETE /planner/remove/<id>)
- **Empty States:** Helpful messages when no meals are planned
- **Print Functionality:** Print-friendly shopping list for grocery trips

### October 12, 2025 - Luxury Design Upgrade
- **Premium Typography:** Implemented Google Fonts with Playfair Display (serif) for all headings and Poppins (sans-serif) for body text
- **Branding Update:** Removed hyphen from "Build-A-Meal" → "Build A Meal" across entire website
- **Food Imagery:** Added professional stock photography background (chef cutting vegetables) with subtle opacity overlay
- **Color Scheme Refinement:** Enhanced gradients from orange to gold (#FF6B35 to #FFD700) for premium aesthetic
- **Luxury Design Elements:** 
  - Increased font sizes and letter-spacing for elegant typography
  - All heading levels (h1-h6) now use Playfair Display serif font
  - Consistent dark theme with high-contrast light text (#cccccc) for readability
  - Premium gradient effects and enhanced shadows throughout
  - Orange (#FF6B35) accent colors for sophisticated visual hierarchy
- **Visual Consistency:** Fixed readability across all pages (About, Favorites) with proper light text on dark backgrounds
- **Static Assets:** Created /static folder for background images and assets

### October 11, 2025 - AI Recipe Generation Integration (FREE!)
- **Real AI Integration:** Implemented AI-powered recipe generation
- **Dual Environment Support:** 
  - Replit: Uses Replit AI Integrations (automatic, no setup needed)
  - Railway: Uses Google Gemini API (100% FREE, no credit card required!)
- **Custom Recipe Creation:** AI generates complete recipes from user's leftover ingredients
- **Smart Prompting:** AI considers ingredients, cuisine preferences, and cooking time constraints
- **Robust Parsing:** Extracts recipe name, ingredients, and step-by-step instructions from AI responses
- **Input Validation:** Added error handling for invalid cooking time inputs (defaults to 30 minutes)
- **Error Display:** User-friendly error messages in the AI Generator interface
- **Railway Setup:** Requires GEMINI_API_KEY environment variable (free from Google AI Studio)

### October 11, 2025 - Railway Deployment & Auto-Initialization
- **Fixed Railway deployment:** Added automatic database initialization on app startup
- **Auto-create tables:** Database tables now created automatically via `db.create_all()` in app context
- **Auto-seed recipes:** 10 sample recipes automatically added if database is empty (prevents duplicates)
- **Production ready:** App now works seamlessly on Railway with PostgreSQL
- **Live deployment:** Successfully deployed to Railway at web-production-9b7cc.up.railway.app

### October 10, 2025 - Tab Navigation System
- Created base template (`base.html`) with tab navigation UI
- Implemented 5 tabs: Home, Browse Recipes, AI Generator, My Favorites, About
- Added routes for all tabs in `main.py`
- Fixed circular import issue by moving `db` initialization to `models.py`
- Added empty-state handling for recipe displays
- Improved code quality per architect review (removed unused imports, added type casting)

### Database Integration
- Recipe model with fields: title, ingredients, instructions, cooking_time
- Seeded database with 10 sample recipes
- Home page displays 6 random featured recipes
- Browse page displays all recipes with full details

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Current Implementation:**
- Tab-based navigation with 5 main sections
- Base template inheritance pattern for consistent UI/UX
- Luxury orange and black color scheme with premium typography
- Google Fonts: Playfair Display (headings) and Poppins (body)
- Professional food photography background with opacity overlay
- Responsive grid layout for recipe cards
- Active tab highlighting for navigation feedback

**Design Pattern:**
- Server-side rendering (SSR) with Jinja2 templating
- Template inheritance using `base.html` as parent template
- Dynamic content rendering from database queries
- Active tab tracking via `active_tab` parameter

**Template Structure:**
- `base.html`: Master template with navigation and shared styles
- `home.html`: Featured recipes (6 random from database)
- `browse.html`: Unlimited recipe search via TheMealDB API with cuisine filter and text search
- `generate.html`: AI recipe generation form
- `favorites.html`: Placeholder for future favorites feature
- `about.html`: Application information and features

### Backend Architecture

**Current Implementation:**
- Flask application with SQLAlchemy ORM
- Multiple route handlers for tab navigation
- Database integration for recipe retrieval
- Railway deployment configuration (PORT env var, debug mode control)
- Circular import resolution via `db.init_app(app)` pattern

**Routes:**
- `/` - Home page with featured recipes
- `/browse` - Unlimited recipe search via TheMealDB API (cuisine filter + text search)
- `/generate` - AI recipe generator (POST support for form submission)
- `/favorites` - My Favorites page
- `/about` - About page

**Design Decisions:**
- **Debug Mode:** Disabled in production (checks RAILWAY_ENVIRONMENT)
- **Host Configuration:** `0.0.0.0` for cloud deployment compatibility
- **Database:** SQLAlchemy with PostgreSQL support
- **Circular Import Fix:** Moved `db = SQLAlchemy()` to models.py, use `db.init_app(app)` in main.py
- **Auto-Initialization:** Database tables and seed data automatically created on app startup
  - `db.create_all()` runs in app context at startup
  - 10 sample recipes auto-seeded if Recipe table is empty
  - Works seamlessly with both SQLite (local) and PostgreSQL (Railway)

### Data Storage

**Current State:**
- PostgreSQL database via SQLAlchemy ORM
- Recipe model with 8 fields (id, title, ingredients, instructions, cooking_time, cuisine, calories, protein, carbs)
- MealPlan model for weekly meal planning
- 10 seeded sample recipes covering various cuisines
- SQLite fallback for local development

**Database Schema:**
```
Recipe:
  - id (Integer, Primary Key)
  - title (String, 100 chars)
  - ingredients (Text)
  - instructions (Text)
  - cooking_time (Integer, minutes)
  - cuisine (String, 50 chars) - Italian, Mexican, American, Asian, Other
  - calories (Integer, default 0)
  - protein (Integer, default 0)
  - carbs (Integer, default 0)

MealPlan:
  - id (Integer, Primary Key)
  - recipe_id (Integer, Foreign Key to Recipe)
  - date (Date)
  - meal_type (String, 20 chars) - breakfast, lunch, dinner
  - created_at (DateTime)
```

### Authentication & Authorization

**Current State:**
- No authentication or authorization implemented

**Future Requirements:**
- User registration and login system likely needed for personalized meal plans
- Session management for maintaining user state
- Possible integration with OAuth providers (Google, Facebook) for social login

## External Dependencies

### Current Dependencies

**Flask:**
- Purpose: Web framework providing routing, templating, and request handling
- Version: Not specified in repository (should be added to requirements.txt)

### Missing Infrastructure

**Requirements File:**
- No `requirements.txt` or `pyproject.toml` present
- Should include: Flask, and future dependencies (database drivers, authentication libraries, etc.)

**Environment Configuration:**
- No `.env` file or environment variable management
- Future needs: database URLs, API keys, secret keys for sessions

### Anticipated Future Dependencies

**Database:**
- Database driver (psycopg2 for PostgreSQL, or appropriate driver for chosen database)
- ORM/Query builder (SQLAlchemy, Drizzle, or similar)

**Authentication:**
- Flask-Login or similar session management
- Password hashing library (bcrypt, Werkzeug's security module)
- Possible OAuth libraries for social authentication

**API Integrations:**
- Potential nutrition API for ingredient data
- Recipe APIs for meal suggestions
- Email service for notifications (SendGrid, Mailgun, etc.)

**Frontend Enhancement:**
- CSS framework (Bootstrap, Tailwind, or similar) for responsive design
- JavaScript framework possibility (Vue.js, React, or Alpine.js) for interactive features