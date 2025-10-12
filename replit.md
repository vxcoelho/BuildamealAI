# Build A Meal

## Overview
Build A Meal is an AI-powered recipe generator web application built with Flask and PostgreSQL. The application features a modern orange and black luxury design with tab-based navigation across 5 main sections: Home, Browse Recipes, AI Generator, My Favorites (planned), and About. Its purpose is to provide users with custom recipe generation, a vast recipe collection, and meal planning tools, aiming to be a premier platform for culinary exploration.

## User Preferences
Preferred communication style: Simple, everyday language.

## System Architecture

### UI/UX Decisions
The application features a luxury orange and black design with premium typography (Playfair Display for headings, Poppins for body) and professional food photography backgrounds. It utilizes gradient overlays, high-contrast text, and subtle animations (e.g., ripple effects, fade-ins) for an enhanced user experience. The design prioritizes visual consistency and responsiveness across all pages.

**Mobile Responsiveness:**
- Two breakpoints: 768px (tablet) and 480px (mobile)
- All pages collapse to single-column layouts on mobile devices
- Touch-friendly controls with minimum 16px font sizes
- Navigation tabs wrap to 2 columns on tablet, stack vertically on mobile
- Recipe grids, meal planner calendar, and feature sections stack to single columns
- Forms and buttons expand to full width on mobile devices
- No horizontal overflow on any screen size

### Technical Implementations
- **Frontend:** Server-side rendering (SSR) using Flask and Jinja2 templating for dynamic content.
- **Backend:** Python Flask framework with SQLAlchemy ORM for database interactions.
- **Database:** PostgreSQL for production, with SQLite fallback for local development. Automatic table creation and seeding of 10 sample recipes on app startup.
- **AI Integration:** Uses Replit AI Integrations (on Replit) or Google Gemini API (on Railway) for custom recipe generation based on user ingredients and cuisine preferences. Features a loading indicator during AI generation.
- **Recipe Search:** Integrates with TheMealDB API for unlimited access to a vast collection of recipes, offering search by cuisine, text, or a combination.
- **Meal Planning:** Includes a drag-and-drop weekly meal planner with features for assigning recipes, removing meals, generating shopping lists, and tracking basic nutrition (calories, protein, carbs).
- **Deployment:** Configured for Railway deployment, including environment variable handling and database auto-initialization.

### Feature Specifications
- **Tab Navigation:** 5 main tabs: Home (featured recipes), Browse Recipes (TheMealDB integration), AI Generator, My Favorites (placeholder), About.
- **AI Generator:** Allows users to input ingredients and select from 12 cuisines to generate new recipes.
- **Browse Recipes:** Provides filters for 26 world cuisines and text search capabilities.
- **Meal Planner:** Weekly calendar interface for planning breakfast, lunch, and dinner, with automatic shopping list generation.
- **Animated Hero Section:** Home page features dynamic video backgrounds with graceful fallbacks, animated particles, and subtle zoom/pulse effects.

### System Design Choices
- **Modular Structure:** Routes and database models are separated for clarity and maintainability.
- **Database Schema:**
    - `Recipe`: Stores recipe details (id, title, ingredients, instructions, cooking_time, cuisine, calories, protein, carbs).
    - `MealPlan`: Links recipes to specific dates and meal types (id, recipe_id, date, meal_type, created_at).
- **Error Handling:** Robust error handling for API calls and input validation.
- **Performance:** CSS-only animations are used to optimize performance.

## External Dependencies

### Current Dependencies
- **Flask:** Web framework for the application.
- **SQLAlchemy:** ORM for database interactions with PostgreSQL.
- **TheMealDB API:** Free, unlimited recipe database for the "Browse Recipes" section.
- **Google Gemini API:** Used for AI recipe generation when deployed on Railway.
- **Replit AI Integrations:** Used for AI recipe generation when running on Replit.
- **Google Fonts:** For premium typography (Playfair Display, Poppins).

### Anticipated Future Dependencies (Not yet integrated)
- Database driver (e.g., `psycopg2` for PostgreSQL).
- Authentication libraries (e.g., Flask-Login, bcrypt).
- Potential CSS frameworks (e.g., Bootstrap, Tailwind).
- Possible JavaScript frameworks (e.g., Vue.js, React, Alpine.js).