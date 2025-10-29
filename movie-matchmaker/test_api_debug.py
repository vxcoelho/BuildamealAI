from tmdb_api import fetch_popular_movies, search_movies, get_movie_details

print("🎬 Testing TMDB API Integration (Debug Mode)...")
print("=" * 50)

# Test 1: Fetch popular movies
print("\n1️⃣ Testing fetch_popular_movies()...")
try:
    popular = fetch_popular_movies()
    print(f"Response: {popular}")
    if popular and 'results' in popular:
        print(f"✅ Success! Found {len(popular['results'])} popular movies")
        print(f"   First movie: {popular['results'][0]['title']}")
    elif 'status_message' in popular:
        print(f"❌ API Error: {popular['status_message']}")
    else:
        print(f"❌ Unexpected response format")
except Exception as e:
    print(f"❌ Exception: {e}")

print("\n" + "=" * 50)
