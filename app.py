
import streamlit as st
import pickle
import requests



movies_list = pickle.load(open('movies.pkl','rb'))
movie_list = movies_list['title'].values


similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3e20f79ccaa13e9c7f895064c7eb6989'.format(movie_id))
    data = response.json()
    x = "https://image.tmdb.org/t/p/original/" + data['poster_path']
    return x

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True,key=lambda x:x[1])[1:6]
        
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        #fetch poster from api  
        recommended_movies_posters.append(fetch_poster(movie_id))

    m = recommended_movies
    p = recommended_movies_posters
    return m,p

st.title('Movie Recommender System')

option = st.selectbox(
    'Which Movie you like the most?',
    movie_list )

st.write('You selected:', option)


if st.button('Recommend'):
    recommendations,posters = recommend(option)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(recommendations[0])
    with col2:
        st.image(posters[1])
        st.text(recommendations[1])
    with col3:
        st.image(posters[2])
        st.text(recommendations[2])
    with col4:
        st.image(posters[3])
        st.text(recommendations[3])
    with col5:
        st.image(posters[4])
        st.text(recommendations[4])


    