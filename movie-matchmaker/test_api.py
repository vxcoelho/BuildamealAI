from tmdb_api import fetch_popular_movies, search_movies, get_movie_details

print("🎬 Testing TMDB API Integration...")
print("=" * 50)

# Test 1: Fetch popular movies
print("\n1️⃣ Testing fetch_popular_movies()...")
popular = fetch_popular_movies()
if popular and 'results' in popular:
    print(f"✅ Success! Found {len(popular['results'])} popular movies")
    print(f"   First movie: {popular['results'][0]['title']}")
else:
    print("❌ Failed to fetch popular movies")

# Test 2: Search for a movie
print("\n2️⃣ Testing search_movies('Inception')...")
search_results = search_movies('Inception')
if search_results and 'results' in search_results:
    print(f"✅ Success! Found {len(search_results['results'])} results")
    if len(search_results['results']) > 0:
        print(f"   First result: {search_results['results'][0]['title']}")
else:
    print("❌ Failed to search movies")

# Test 3: Get movie details
print("\n3️⃣ Testing get_movie_details(550)...")  # Fight Club
details = get_movie_details(550)
if details and 'title' in details:
    print(f"✅ Success! Movie: {details['title']}")
    print(f"   Year: {details['release_date'][:4]}")
    print(f"   Rating: {details['vote_average']}/10")
else:
    print("❌ Failed to get movie details")

print("\n" + "=" * 50)
print("🎉 All tests complete!")
