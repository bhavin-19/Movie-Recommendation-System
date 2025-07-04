import pickle
import pandas as pd
import streamlit as st
import requests

# ✅ Your TMDB API Key
API_KEY = "api key"

# ✅ Function to fetch poster and trailer link using TMDB API
import time

def fetch_poster_and_trailer(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "append_to_response": "videos"
    }

    try:
        response = requests.get(url, params=params, timeout=10)  # ⏱ Add timeout
        response.raise_for_status()  # 🔍 Raise HTTPError if status is not 200
        data = response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return None, None

    # Extract poster
    poster_url = None
    if data.get("poster_path"):
        poster_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    # Extract trailer
    trailer_url = None
    for video in data.get('videos', {}).get('results', []):
        if video['type'] == 'Trailer' and video['site'] == 'YouTube':
            trailer_url = f"https://www.youtube.com/watch?v={video['key']}"
            break

    return poster_url, trailer_url

# ✅ Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_trailers = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        poster_url, trailer_url = fetch_poster_and_trailer(movie_id)
        recommended_movie_posters.append(poster_url)
        recommended_movie_trailers.append(trailer_url)
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_trailers


# ✅ Load data
movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ✅ Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.header('🎬 Movie Recommender System')

movie_list = movies['title'].tolist()
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    names, posters, trailers = recommend(selected_movie)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
            if trailers[i]:
                st.markdown(f"[▶ Watch Trailer]({trailers[i]})", unsafe_allow_html=True)
            else:
                st.write("Trailer not available")
