import os

print("🔍 Checking environment variable...")
api_key = os.environ.get('TMDB_API_KEY')

if api_key:
    print(f"✅ TMDB_API_KEY found!")
    print(f"   Length: {len(api_key)} characters")
    print(f"   First 5 chars: {api_key[:5]}...")
    print(f"   Last 5 chars: ...{api_key[-5:]}")
else:
    print("❌ TMDB_API_KEY not found in environment!")
    print("   Make sure it's set in Replit Secrets")
