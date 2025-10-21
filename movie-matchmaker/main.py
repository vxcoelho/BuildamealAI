from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Movie Matchmaker - Coming Soon!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

url = f"{TMDB_BASE_URL}/movie/popular?api_key={TMDB_API_KEY}"
response = requests.get(url)
data = response.json()
return data

url = f"{TMDB_BASE_URL}/search/movie?api_key={TMDB_API_KEY}&query={query}"

url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}"
response = requests.get(url)
data = response.json()
return data
-- movie-matchmaker/templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Matchmaker</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
  <div class="container">
    <h1>Movie Matchmaker</h1>
    <p>Find your perfect movie match!</p>
    <form action="/search" method="post">
      <input type="text" name="query" placeholder="Search for a movie..." required>    
      <button type="submit">Search</button>
    </form>
  </div>
</body>
</html>
-- movie-matchmaker/templates/search_results.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Results</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
  <div class="container">
    <h1>Search Results</h1>
    <a href="/">Back to Home</a>
