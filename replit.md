# Build-A-Meal

## Overview

Build-A-Meal is a web application built with Flask that appears to be in its initial development phase. The application currently displays a landing page indicating it's "Coming Soon". Based on the naming convention, this application is likely intended to be a meal planning or recipe building platform.

**Tech Stack:**
- **Backend:** Python Flask web framework
- **Frontend:** HTML with inline CSS (currently minimal)
- **Server:** Flask development server

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Current Implementation:**
- Simple HTML template rendering using Flask's Jinja2 templating engine
- Inline CSS styling for the landing page
- Responsive design with flexbox centering
- Gradient background aesthetic (purple/blue theme)

**Design Pattern:**
- Server-side rendering (SSR) approach where Flask renders HTML templates
- Template variable injection for dynamic content (message variable)

**Rationale:**
- Flask's built-in templating is suitable for small to medium applications
- Server-side rendering provides good SEO and initial load performance
- Simple structure allows for rapid prototyping and iteration

### Backend Architecture

**Current Implementation:**
- Flask application with minimal configuration
- Single route handler (`/`) serving the home page
- Development server running on port 5000 with debug mode enabled
- Host set to `0.0.0.0` for external accessibility

**Design Decisions:**
- **Debug Mode:** Enabled for development, provides auto-reload and detailed error messages
- **Host Configuration:** `0.0.0.0` allows access from any network interface, suitable for cloud development environments like Replit

**Future Considerations:**
- As the application grows, route handlers should be organized into blueprints
- Configuration should be externalized (environment variables, config files)
- Debug mode must be disabled in production
- Production-ready WSGI server (like Gunicorn) should replace Flask's development server

### Data Storage

**Current State:**
- No database implementation present
- No data persistence layer

**Expected Future Requirements:**
- Database for storing recipes, ingredients, meal plans, and user data
- Likely candidates: PostgreSQL (for relational data), SQLite (for development)
- ORM consideration: SQLAlchemy or Drizzle for database interactions

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