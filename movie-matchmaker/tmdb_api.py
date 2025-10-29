import os
import requests

# Get API key from environment
TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

def fetch_popular_movies():
    """
    Fetch popular movies from TMDB
    """
    url = f"{TMDB_BASE_URL}/movie/popular?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def search_movies(query):
    """
    Search for movies by title
    """
    url = f"{TMDB_BASE_URL}/search/movie?api_key={TMDB_API_KEY}&query={query}"
    response = requests.get(url)
    data = response.json()
    return data

def get_movie_details(movie_id):
    """
    Get detailed information about a specific movie
    """
    url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data
