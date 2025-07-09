# Movie Recommender System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)

Hey there! Welcome to my Movie Recommender System, a fun project I built to help you discover movies you’ll love. Pick a movie you enjoy, and this app will suggest similar ones, complete with posters to spark your interest. It’s powered by machine learning and wrapped in a slick Streamlit interface. I’m Poornasai, and I had a blast putting this together—hope you enjoy it!

Check out my GitHub: [kpoornasai121](https://github.com/paulanurag05)

## What’s This All About?

This project uses a clever technique called content-based filtering to recommend movies based on what you already like. It digs into movie details like genres, plot summaries, cast, and crew, then finds similar films using a bit of math magic (cosine similarity, if you’re curious). The recommendations pop up in a clean web app, with posters pulled straight from the OMDB API.

## Cool Features

- **Easy-to-Use Interface**: Just pick a movie from a dropdown and hit a button to get recommendations.
- **Movie Posters**: See vibrant posters for each suggestion (or a placeholder if one’s missing).
- **Smart Recommendations**: Finds movies with similar vibes based on genres, cast, and more.
- **Smooth Performance**: Caches data to keep things fast and respects API limits.
- **Oops-Proof**: Handles errors gracefully, so you’re never left hanging.

## What Data Powers It?

The system uses two datasets from TMDB:
- **tmdb_5000_movies.csv**: Packed with movie info like titles, genres, and summaries.
- **tmdb_5000_credits.csv**: Lists the cast and crew for each film.

These get mashed together and processed to make the recommendation engine hum.

## Getting Started

Want to try it out on your own machine? Here’s how to get it running:

1. **Grab the Code**:
   ```bash
      git clone https://github.com/kpoornasai121/Movie-Recommender-System.git
      cd movie-recommender-system
   ```
2. **Get the Datasets**:
  - Download tmdb_5000_movies.csv and tmdb_5000_credits.csv from Kaggle.
  - Pop them into a Dataset folder in the project.

3. **Snag an OMDB API Key**:
  - Head to OMDB API and grab a free key.
  - Open app.py and swap out the OMDB_API_KEY with yours.


## How to Use It

**Fire Up the App**:
      ```bash
      streamlit run app.py
      ```
It’ll open in your browser at http://localhost:8501.

**Pick Your Movie**:
- Choose a movie you love from the dropdown.
- Click “Get Recommendations” to see 10 similar movies.

**Enjoy the Suggestions**:
- You’ll get a neat grid of movie posters and titles.
- Scroll through and find your next watch!

## Stuff You’ll Need

- Python 3.8 or higher
- pandas
- numpy
- scikit-learn
- nltk
- streamlit
- requests

**Intall them all with**:
   ```bash
   pip install pandas numpy scikit-learn nltk streamlit requests
   ```
