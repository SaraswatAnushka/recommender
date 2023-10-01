import streamlit as st
import pickle
import pandas as pd

# Load data and similarities
with open('required_data.pkl', 'rb') as file:
    data_dict = pickle.load(file)

titles = pd.DataFrame(data_dict)

with open('similarities.pkl', 'rb') as file:
    similarities = pickle.load(file)

st.title('Portfolio Dataset Recommender Model')

def recommend(title_name):
    title_row = titles[titles['title_name'] == title_name]
    title_id = title_row.index[0]
    
    similar_titles_indices = similarities[title_id].argsort()[::-1][1:]
    
    top_similar_titles = titles.iloc[similar_titles_indices[:5]]
    
    return top_similar_titles

selected_title = st.selectbox('Titles', (titles['title_name'].values))

if st.button('Recommend'):
    recommendations = recommend(selected_title)
    recommended_titles = recommendations['title_name'].tolist()
    st.write("Recommended Titles:")
    for title in recommended_titles:
        st.write(title)
