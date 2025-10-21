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
    # YOUR CODE HERE - Fill in the 4 lines like above!
    # Hint: url = f"{TMDB_BASE_URL}/search/movie?api_key={TMDB_API_KEY}&query={query}"
    pass

def get_movie_details(movie_id):
    """
    Get detailed information about a specific movie
    """
    # YOUR CODE HERE - Fill in the 4 lines like above!
    # Hint: url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}"
    pass
