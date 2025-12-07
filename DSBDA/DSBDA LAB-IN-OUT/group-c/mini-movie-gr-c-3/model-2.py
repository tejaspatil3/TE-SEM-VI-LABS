import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset from local file
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\Lenovo\Desktop\VSC1\dsbda-lab\movie-rec-model\movie_dataset.csv")  # adjust to actual location
  # Make sure this file is in the same folder

df = load_data()

# Handle missing values
df['overview'] = df['overview'].fillna('')

# Vectorize overview text using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['overview'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create reverse mapping of movie titles to DataFrame indices
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# Recommendation function
def recommend(title):
    idx = indices.get(title)
    if idx is None:
        return ["Movie not found."]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

# Streamlit UI
st.title("Movie Recommendation System ")

selected_movie = st.selectbox("Choose a movie you like:", df['title'].dropna().unique())

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
