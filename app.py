import streamlit as st
import pickle
import requests
import time
from requests.exceptions import RequestException

# ========== CONFIGURATION ==========
# Must be the first Streamlit command
st.set_page_config(
    page_title="Movie Recommender", 
    layout="wide",
    menu_items={
        'About': "Movie Recommender using OMDB API"
    }
)

# API Configuration
OMDB_API_KEY = "691cdfa6"  # Your OMDB API key
DEFAULT_POSTER = "https://via.placeholder.com/500x750?text=Poster+Not+Available"
REQUEST_TIMEOUT = 3  # seconds
DELAY_BETWEEN_REQUESTS = 0.2  # seconds

# ========== DATA LOADING ==========
@st.cache_data
def load_data():
    try:
        movies = pickle.load(open('movie_list.pkl', 'rb'))
        similarity = pickle.load(open('similarity.pkl', 'rb'))
        return movies, similarity
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

movies, similarity = load_data()

# ========== POSTER FETCHING ==========
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_poster(movie_title, year=None):
    """
    Fetch poster from OMDB API using movie title
    """
    try:
        # Build query - include year if available for better matching
        params = {
            't': movie_title,
            'apikey': OMDB_API_KEY,
            'type': 'movie'
        }
        if year:
            params['y'] = year
            
        response = requests.get(
            "http://www.omdbapi.com/",
            params=params,
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()
        data = response.json()
        
        if data.get('Poster') and data['Poster'] != 'N/A':
            return data['Poster']
        return DEFAULT_POSTER
        
    except RequestException as e:
        st.warning(f"Couldn't fetch poster for '{movie_title}': {str(e)}")
        return DEFAULT_POSTER
    except Exception as e:
        st.error(f"Unexpected error fetching poster: {str(e)}")
        return DEFAULT_POSTER

# ========== RECOMMENDATION ENGINE ==========
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)
        
        recommendations = []
        for i in distances[1:11]:  # Get top 10 recommendations
            movie_data = movies.iloc[i[0]]
            title = movie_data.title
            year = str(movie_data.get('year', '')) if 'year' in movies.columns else None
            
            time.sleep(DELAY_BETWEEN_REQUESTS)
            poster = fetch_poster(title, year)
            
            recommendations.append({
                'title': title,
                'poster': poster
            })
        
        return recommendations
        
    except Exception as e:
        st.error(f"Recommendation error: {e}")
        return []

# ========== STREAMLIT UI ==========
st.title("🎬 Movie Recommender System")
st.write("Discover movies similar to your favorites")

# Movie selection
selected_movie = st.selectbox(
    "Select a movie you like:",
    movies['title'].values,
    index=0,
    help="Select a movie to get recommendations"
)

# Recommendation button
if st.button("Get Recommendations"):
    with st.spinner('Finding similar movies...'):
        recommendations = recommend(selected_movie)
        
        if not recommendations:
            st.warning("Couldn't generate recommendations. Please try another movie.")
        else:
            # Display in 2 rows of 5 columns
            cols = st.columns(5)
            for i, movie in enumerate(recommendations):
                with cols[i % 5] if i < 5 else cols[i % 5]:
                    st.image(
                        movie['poster'], 
                        use_column_width=True,
                        caption=movie['title']
                    )

# Footer
st.markdown("---")
st.caption("""
    Movie data from your dataset | Posters from OMDB API
    \nNote: Some posters may not be available
""")
