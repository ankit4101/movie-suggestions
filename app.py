import streamlit as st
import pickle
import pandas as pd
import requests

# Load data and API key
mov_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(mov_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
api_key = st.secrets['API_KEY']

# Function to fetch poster
def fetch_poster(movie_id):
    url = fr'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    resp = requests.get(url)
    data = resp.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

# Function to fetch release year
def release_year(movie_id):
    url = fr'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    resp = requests.get(url)
    data = resp.json()
    return (data['release_date'])[:4]

# Recommendation logic
def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        movie_title = movies.iloc[i[0]].title
        movie_year = release_year(movie_id)
        recommended_movies.append(f"{movie_title} ({movie_year})")
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# Page configuration
st.set_page_config(
    page_title="🎬 Movie Suggestions",
    page_icon="🎥",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
<style>
body {
    background-color: #0f0f0f;
    color: #fff;
}
h1, h3 {
    color: #00ffe1;
    text-align: center;
}
.stSelectbox > div {
    background-color: #1c1c1c !important;
    color: #00ffe1 !important;
}
button[kind="primary"] {
    background-color: #00ffe1 !important;
    color: #0f0f0f !important;
    font-weight: bold;
}
.card {
    background-color: #1e1e1e;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0 4px 8px rgba(0,255,255,0.2);
    transition: 0.3s;
    text-align: center;
}
.card:hover {
    box-shadow: 0 8px 16px rgba(0,255,255,0.4);
}
.card-title {
    font-size: 16px;
    margin: 10px 0;
    color: #00ffe1;
}
</style>
""", unsafe_allow_html=True)

# App header
st.title("🎬 Movie Suggestions")
st.markdown("#### Get 5 recommendations based on your favorite movie (powered by TMDb 5000 Movie Dataset)")

# Movie selection
selected_movie = st.selectbox('Pick a movie:', movies['title'].values)

# Recommend button
if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    st.markdown("### 🔥 Recommended Movies")
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"""
            <div class="card">
                <img src="{posters[idx]}" style="width:100%; border-radius:10px;" />
                <div class="card-title">{names[idx]}</div>
            </div>
            """, unsafe_allow_html=True)
