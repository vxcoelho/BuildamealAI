# 🚀 Deploy Build-A-Meal to Railway

## ✅ Prerequisites

- GitHub account
- Railway account (sign up at https://railway.com - free tier available)
- Your code pushed to a GitHub repository

## 📋 Deployment Steps

### Step 1: Push Code to GitHub

Make sure all your files are committed and pushed to GitHub:
```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### Step 2: Deploy to Railway

**Option A: Deploy from GitHub (Recommended)**

1. Go to https://railway.com and sign in
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your `build-a-meal` repository
5. Railway will automatically:
   - Detect it's a Python/Flask app
   - Install dependencies from `requirements.txt`
   - Use the `Procfile` to start your app with Gunicorn

**Option B: Using Railway CLI**

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Initialize and deploy
railway init
railway up
```

### Step 3: Add PostgreSQL Database (Optional but Recommended)

1. In your Railway project dashboard, click **"New"** → **"Database"** → **"PostgreSQL"**
2. Railway automatically creates a PostgreSQL database
3. Railway automatically sets the `DATABASE_URL` environment variable
4. Your app will connect automatically (already configured in `main.py`)

### Step 4: Run Database Migrations

After deployment, you need to create tables and seed data:

1. In Railway dashboard, go to your service
2. Click on **"Settings"** → **"Deploy"** 
3. Add a **"Build Command"**:
   ```
   python seed_data.py
   ```

Or run manually from Railway CLI:
```bash
railway run python seed_data.py
```

### Step 5: Generate Public Domain

1. In Railway dashboard, click on your deployed service
2. Go to **"Settings"** → **"Networking"**
3. Click **"Generate Domain"**
4. Your app will be live at: `https://build-a-meal.up.railway.app` 🎉

You can also add a custom domain from the same section!

## 📁 Files Needed for Deployment

Make sure you have these files in your repository:

- ✅ `main.py` - Your Flask application
- ✅ `models.py` - Database models
- ✅ `seed_data.py` - Sample recipe data
- ✅ `templates/index.html` - Frontend template
- ✅ `requirements.txt` - Python dependencies
- ✅ `Procfile` - Tells Railway how to run your app
- ✅ `.gitignore` - Ignore unnecessary files

## 🔍 Important Configuration

### Procfile
```
web: gunicorn main:app --bind 0.0.0.0:$PORT
```

### requirements.txt
```
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
gunicorn==23.0.0
psycopg2-binary==2.9.10
```

### Environment Variables (Automatically Set by Railway)
- `PORT` - Railway assigns this automatically
- `DATABASE_URL` - Set automatically when you add PostgreSQL

## 🐛 Troubleshooting

### App Not Responding
- Ensure your app binds to `0.0.0.0`, not `127.0.0.1`
- Verify `$PORT` environment variable is used in `main.py`
- Check logs in Railway dashboard under **"View Logs"**

### Database Connection Error
- Make sure PostgreSQL database is added to your project
- Run `python seed_data.py` to create tables
- Check `DATABASE_URL` is set correctly in environment variables

### 500 Internal Server Error
- Check Railway logs for Python errors
- Ensure all dependencies are in `requirements.txt`
- Verify database tables are created

## 📊 Current Setup Summary

✅ **Flask app with database support**
- 10 sample recipes pre-loaded
- PostgreSQL-ready (works with Railway database)
- Production-ready with Gunicorn server

✅ **Sample Recipes Included:**
1. Pasta Aglio e Olio (20 min)
2. Classic Margherita Pizza (25 min)
3. Chicken Stir Fry (30 min)
4. Caesar Salad (15 min)
5. Beef Tacos (20 min)
6. Vegetable Soup (45 min)
7. Pancakes (15 min)
8. Grilled Salmon (20 min)
9. Chocolate Chip Cookies (25 min)
10. Mushroom Risotto (35 min)

## 🎯 Next Steps After Deployment

1. **Verify deployment**: Visit your Railway URL
2. **Test database**: Add/view recipes functionality (coming soon)
3. **Custom domain**: Set up your own domain name
4. **Monitor**: Check Railway logs and analytics

---

**Your Live URL Format:**
`https://build-a-meal-[random].up.railway.app`

or

`https://yourusername-build-a-meal.up.railway.app`

🚀 **You're all set! Deploy today and get your app live!**
