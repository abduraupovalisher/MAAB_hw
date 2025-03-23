import requests
import random

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.themoviedb.org/3"

def get_genre_id(genre_name):
    """Fetches genre ID based on the user's input"""
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    genres = response.json().get("genres", [])

    for genre in genres:
        if genre["name"].lower() == genre_name.lower():
            return genre["id"]
    return None

def get_movies_by_genre(genre_id):
    """Fetches movies based on genre ID"""
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    movies = response.json().get("results", [])
    return movies

def recommend_movie():
    """Asks for genre input and recommends a random movie"""
    genre_name = input("Enter a movie genre (e.g., Action, Comedy, Horror): ")
    genre_id = get_genre_id(genre_name)

    if not genre_id:
        print("Sorry, genre not found. Try again!")
        return

    movies = get_movies_by_genre(genre_id)

    if not movies:
        print(f"Sorry, no movies found for {genre_name}.")
        return

    movie = random.choice(movies)
    print("\n🎬 **Movie Recommendation:**")
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"More details: https://www.themoviedb.org/movie/{movie['id']}")

recommend_movie()

