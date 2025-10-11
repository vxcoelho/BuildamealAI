# Build-A-Meal

## Overview

Build-A-Meal is an AI-powered recipe generator web application built with Flask and PostgreSQL. The application features a tab-based navigation system with 5 main sections: Home (featured recipes), Browse Recipes (full recipe collection), AI Generator (custom recipe generation), My Favorites (planned feature), and About.

**Tech Stack:**
- **Backend:** Python Flask web framework
- **Database:** PostgreSQL with SQLAlchemy ORM
- **Frontend:** HTML with inline CSS, Jinja2 templating
- **Server:** Flask development server (Gunicorn for production via Railway)
- **Deployment:** Railway-ready with Procfile

## Recent Changes

### October 11, 2025 - AI Recipe Generation Integration
- **Real AI Integration:** Implemented OpenAI-powered recipe generation using Replit AI Integrations
- **Custom Recipe Creation:** AI generates complete recipes from user's leftover ingredients
- **Smart Prompting:** AI considers ingredients, cuisine preferences, and cooking time constraints
- **Robust Parsing:** Extracts recipe name, ingredients, and step-by-step instructions from AI responses
- **Input Validation:** Added error handling for invalid cooking time inputs (defaults to 30 minutes)
- **Error Display:** User-friendly error messages in the AI Generator interface
- **No API Key Required:** Uses Replit AI Integrations (charges billed to Replit credits)

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
- Inline CSS styling with purple/blue gradient theme
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
- `browse.html`: All recipes with full details
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
- `/browse` - Browse all recipes
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
- Recipe model with 4 fields (id, title, ingredients, instructions, cooking_time)
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