
import streamlit as st
import pandas as pd
import pickle
import requests
import webbrowser
import random 
import requests


# 1 slider menu
from streamlit_option_menu import option_menu
selected = option_menu(menu_title =None,
                           options=['Movies Recommendation','Popular TV Shows'],
                           icons = ['','award'],
                           orientation='horizontal',
                           styles={ 
                            "container": {"padding": "0!important", "background-color": "#000000"},
                            "icon": {"color": "white", "font-size": "15px"}, 
                            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#4a4a4a"},
                            "nav-link-selected": {"background-color": '#9277E8'},
                                }
                    )

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

@st.cache(allow_output_mutation=True,suppress_st_warning=True,show_spinner=False)
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc41989ea22a08de0810429c2fe674d8&language=en-US'.format(movie_id))

    data = response.json()  #convert that file into a json
    
    if data['poster_path'] == None:
        data = 'https://cdn.wallpapersafari.com/26/62/EITbaV.jpg'
    else:
        data = "https://image.tmdb.org/t/p/w500/" + data['poster_path'] 
    return data   #and copy the poster path from json file but this is not the comlete path
    #st.write(movie_id)
    #st.write("https://image.tmdb.org/t/p/w500/" , data['poster_path'])                                                                   # so added complete path 
                                                                       
@st.cache(allow_output_mutation=True,suppress_st_warning=True,show_spinner=False)
# Function for fetch the released date of the movie
def fetch_release_date(movie_id):
    release_date = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc41989ea22a08de0810429c2fe674d8&language=en-US'.format(movie_id))
    data = release_date.json()
    if data['release_date'] == None:
        ds = '   '
    else:
        ds = data['release_date'] 
    return ds 

@st.cache(allow_output_mutation=True,suppress_st_warning=True,show_spinner=False)
# Function for fetch the tagline of the movie
def fetch_tagline(movie_id):
    tagline = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc41989ea22a08de0810429c2fe674d8&language=en-US'.format(movie_id))
    data = tagline.json()
    if data['tagline'] == None:
        ds = '   '
    else:
        ds = data['tagline'] 
    return ds
    
    
@st.cache(allow_output_mutation=True,suppress_st_warning=True,show_spinner=False)
# Function to fetch the overview 
def fetch_overview(movie_id):
    overview = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc41989ea22a08de0810429c2fe674d8&language=en-US'.format(movie_id))
    data = overview.json()
    if data['overview'] == None:
        ds = '   '
    else:
        ds = data['overview'] 
    return ds

@st.cache(allow_output_mutation=True,suppress_st_warning=True,show_spinner=False)
# Function to fetch the rating 
def fetch_rating(movie_id):
    rating = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc41989ea22a08de0810429c2fe674d8&language=en-US'.format(movie_id))
    data = rating.json()
    
    if data['vote_average'] == None:
        ds = '   '
    else:
        ds = data['vote_average'] 
    #st.write(movie_id)
    return ds
    #st.write(movie_id)
    #return data['vote_average']
@st.cache(allow_output_mutation=True,suppress_st_warning=True,show_spinner=False)
# Function fro convert those tuple data type into string
def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + '- ' + item
    return str
 
@st.cache(allow_output_mutation=True,suppress_st_warning=True,show_spinner=False)
# Function for fetch types of movie
def fetch_types(movie_id):
    types = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc41989ea22a08de0810429c2fe674d8&language=en-US'.format(movie_id))
    ds = types.json()
    genres = ds['genres']# there fetching nested dict of genres
    # st.write(movie_id)
    # st.write(ds)
    # write a if condition if there types of movies is 0 then print nothing
    if len(genres) == 0:
        data = '  '
        return data
        
    elif len(genres) == 1:
        dr = genres[0]['name']    
        # function for convertt the tupe into strings
        def convertTuple(tup):
        # initialize an empty string
            str = ''
            for item in tup:
                str = str + '- ' + item
            return str 
        data = convertTuple(dr)
        data = data     
        return data  
    elif len(genres) > 1:
        dr = genres[0]['name'],genres[1]['name']  # then fetch both directory element but it is in tuple
        # function for convertt the tupe into strings
        def convertTuple(tup):
        # initialize an empty string
            str = ''
            for item in tup:
                str = str + '- ' + item
            return str 
        
        data = convertTuple(dr)   # so, convert tuple into string using above function
        data = data     
        return data
    
@st.cache(allow_output_mutation=True,suppress_st_warning=True,show_spinner=False)
# Function for fetch trailer link of the movie
def fetch_trailer(movie_id):
    trailer = requests.get('https://api.themoviedb.org/3/movie/{}/videos?api_key=dc41989ea22a08de0810429c2fe674d8&language=en-US'.format(movie_id))
    ds = trailer.json()
    results = ds['results']
    # st.write(movie_id)
    # st.write(results)
    if results[0]['type'] == None:
        link = ''
    elif results[0]['type'] == 'Trailer':
        link = results[0]['key']
    elif results[1]['type'] == None:
        link = ''
    elif results[1]['type'] == 'Trailer':
        link = results[1]['key']    
    elif results[2]['type'] == None:
        link = ''
    elif results[2]['type'] == 'Trailer':
        link = results[2]['key'] 
    elif results[3]['type'] == None:
        link = ''
    elif results[3]['type'] == 'Trailer':
        link = results[3]['key'] 
    elif results[4]['type'] == None:
        link = ''
    elif results[4]['type'] == 'Trailer':
        link = results[4]['key']   
    elif results[5]['type'] == None:
        link = ''
    elif results[5]['type'] == 'Trailer':
        link = results[5]['key']   
    elif results[6]['type'] == None:
        link = ''   
    elif results[6]['type'] == 'Trailer':
        link = results[6]['key']
    else:
        link = results[0]['key']
    
    return 'https://www.youtube.com/watch?v=' + link
   
   
@st.cache(allow_output_mutation=True,suppress_st_warning=True,show_spinner=False)
# Fetch the background poster path
def fetch_bg_poster(movie_id):
    back_poster = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dc41989ea22a08de0810429c2fe674d8&language=en-US'.format(movie_id))
    data = back_poster.json()  #convert that file into a json
    #return "https://image.tmdb.org/t/p/w500/" + data['backdrop_path']   #and copy the poster path from json file but this is not the comlete path
    # so added complete path 
    dt = data['backdrop_path']
    # below if function will check the path link of background if link is missing then it will be set a fixed image 
    # else it will be print the link with front link
    if dt == None:
        #st.write('No background poster available for this movie')
        link = 'https://cdn.wallpapersafari.com/26/62/EITbaV.jpg'
    else:
        link  = "https://image.tmdb.org/t/p/w500/" + data['backdrop_path']
        #st.write("https://image.tmdb.org/t/p/w500/" , data['backdrop_path']) 
                 
    return link

    
    
# Function for recommended the movies
@st.cache(allow_output_mutation=True,suppress_st_warning=True)
def recommend(movie):
    movie_index =movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6] # from here taking top 5 movies name
    
    
    recommended_movies_name = []
    recommended_movies_poster = []
    recommended_movies_release_date = []
    recommended_movies_tagline = []
    recommended_movies_overview = []
    recommended_movies_rating = []
    recommended_movies_types = []
    recommended_movies_trailer_link = []
    recommended_movies_bg_poster_path = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id # to fetch movie id
        # Fetch movies name from API
        recommended_movies_name.append(movies.iloc[i[0]].title) # all movies list append with titles
        # Fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
        # Fetch release date from API
        recommended_movies_release_date.append(fetch_release_date(movie_id))
        # Fetch tagline from API
        recommended_movies_tagline.append(fetch_tagline(movie_id))
        # Fetch overview from API
        recommended_movies_overview.append(fetch_overview(movie_id))
        # Fetch overview from API
        recommended_movies_rating.append(fetch_rating(movie_id))
        # Fetch types of movie from API
        recommended_movies_types.append(fetch_types(movie_id))
        # Fetch trailer link from API
        recommended_movies_trailer_link.append(fetch_trailer(movie_id))
        # Fetch bg_poster link from API
        recommended_movies_bg_poster_path.append(fetch_bg_poster(movie_id))
    return recommended_movies_name,recommended_movies_poster,recommended_movies_release_date,recommended_movies_tagline,recommended_movies_overview,recommended_movies_rating,recommended_movies_types,recommended_movies_trailer_link,recommended_movies_bg_poster_path

# load movies list file
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
# from dictionary dataframe create
movies  = pd.DataFrame(movies_dict)
# load similarity file
similarity = pickle.load(open('similarity.pkl','rb'))

    
# if selected == 'Recommended':
if selected == "Movies Recommendation":
    st.title(f'Movie Recommendation System🎬')
    
    st.caption('A movie recommendation system, or a movie recommender system, is an ML-based approach to filtering or predicting the users’ film preferences based on their past choices and behavior. It’s an advanced filtration mechanism that predicts the possible movie choices of the concerned user and their preferences towards a domain-specific item, aka movie.')
    
    selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown box▾',
    movies['title'].values)
#-----------------------------------------------------------------------------------------------------

    recommend_button = st.button('Recommend') 
    if recommend_button: 
        names,posters,release_date,tagline,overview,rating,types,trailer_link,bg_poster = recommend(selected_movie_name) 

# --------------------------------------------- 1st Movie Showing -------------------------------------- #
    # Grid making for only first movie 
    
        col1, col2 = st.columns((1,1))
        with col1:
            url = trailer_link[0]
       
        # Add chart #1
            st.image(posters[0],width=280)
    
    # Add chart #2  
        with col2:
            st.header(names[0])
        
            st._transparent_write('R :  ', release_date[0], "  " , rating[0], "  ",  types[0])
        
        # Showing tagline of movies
            st.caption(tagline[0])
        
        #st.write(url)
        # Creating function for on_click method youtube link open
            def link_open():
                url = trailer_link[0]
                webbrowser.open_new_tab(url)
        # Calling link open function    
            st.button('Watch Trailer', on_click=link_open)
       
        # Showing overview details of movie
            st.subheader('Overview')
            overview_first = overview[0]
            slice_data = overview_first[0: 180] + '...'
            st._transparent_write(slice_data)
            
# ------------------------------------------------- 2nd Movie Showing -------------------------------------- #      
        # Grid making for only first movie 
        col1, col2 = st.columns((1,1))
        with col1:
            url = trailer_link[1]
       
        
    # Add chart #1
            st.image(posters[1],width=280)
        with col2:
    # Add chart #2    
            st.header(names[1])
            st._transparent_write('R :  ', release_date[1], "  " , rating[1], "  ",  types[1])
        
        # Showing tagline of movies
            st.caption(tagline[1])
        
        #st.write(url)
        # Creating function for on_click method youtube link open
            def link_open():
                url = trailer_link[1]
                webbrowser.open_new_tab(url)
        # Calling link open function    
            st.button('Watch Trailer ', on_click=link_open)
       
        # Showing overview details of movie
            st.subheader('Overview')
            overview_first = overview[1]
            slice_data = overview_first[0: 180] + '...'
            st._transparent_write(slice_data)
        
# ------------------------------------------------- 3rd Movie Showing -------------------------------------- #      
    # Grid making for only third movie 
        col1, col2 = st.columns((1,1))
        with col1:
            url = trailer_link[2]
       
        
    # Add chart #1
            st.image(posters[2],width=280)
        with col2:
    # Add chart #2    
            st.header(names[2])
            st._transparent_write('R :  ', release_date[2], "  " , rating[2], "  ",  types[2])
        
        # Showing tagline of movies
            st.caption(tagline[2])
        
        #st.write(url)
        # Creating function for on_click method youtube link open
            def link_open():
                url = trailer_link[2]
                webbrowser.open_new_tab(url)
        # Calling link open function    
            st.button('Watch Trailer  ', on_click=link_open)
       
        # Showing overview details of movie
            st.subheader('Overview')
            overview_first = overview[2]
            slice_data = overview_first[0: 180] + '...'
            st._transparent_write(slice_data)

# ------------------------------------------------- 4th Movie Showing -------------------------------------- #      
    # Grid making for only fourth movie 
        col1, col2 = st.columns((1,1))
        with col1:
            url = trailer_link[3]
       
        # Add chart #1
            st.image(posters[3],width=280)
        with col2:
    # Add chart #2    
            st.header(names[3])
            st._transparent_write('R :  ', release_date[3], "  " , rating[3], "  ",  types[3])
        
        # Showing tagline of movies
            st.caption(tagline[3])
        
        #st.write(url)
        # Creating function for on_click method youtube link open
            def link_open():
                url = trailer_link[3]
                webbrowser.open_new_tab(url)
        # Calling link open function    
            st.button(' Watch  Trailer  ', on_click=link_open)
       
        # Showing overview details of movie
            st.subheader('Overview')
            overview_first = overview[3]
            slice_data = overview_first[0: 180] + '...'
            st._transparent_write(slice_data)
        
# ------------------------------------------------- 5th Movie Showing -------------------------------------- #      
    # Grid making for only fifth movie 
        col1, col2 = st.columns((1,1))
        with col1:
            url = trailer_link[4]
       
        
    # Add chart #1
            st.image(posters[4],width=280)
        with col2:
    # Add chart #2    
            st.header(names[4])
            st._transparent_write('R :  ', release_date[4], "  " , rating[4], "  ",  types[4])
        
        # Showing tagline of movies
            st.caption(tagline[4])
        
        #st.write(url)
        # Creating function for on_click method youtube link open
            def link_open():
                url = trailer_link[4]
                webbrowser.open_new_tab(url)
        # Calling link open function    
            st.button(' Watch Trailer  ', on_click=link_open)
       
        # Showing overview details of movie
            st.subheader('Overview')
            overview_first = overview[4]
            slice_data = overview_first[0: 180] + '...'
            st._transparent_write(slice_data)
        # st.success('Five movies recommended')
        st.write('---')
       

#----------------------------------------------All Grid Making done!----------------------------# 

if selected == 'Popular TV Shows':
#     st.markdown("<h3 style='text-align: left; color: #BB86FC;'> Popular Movies list</h3>", unsafe_allow_html=True)
#     buton_5 = st.button('Show')
#     if buton_5:
#         st.session_state.load_statee = False
#         def link_create(link):
#             request_file = requests.get(link)
#             file_convert = request_file.json()
#             rand_data = random.sample(file_convert,5)
#             title_01 = rand_data[0]
#             title_02 = rand_data[1]
#             title_03 = rand_data[2]
#             title_04 = rand_data[3]
#             title_05 = rand_data[4]
#             title_name_01 =title_01['title']
#             st.write('1.',title_name_01)
#             # st.write(title_name_01)
#             title_name_02=title_02['title']
#             # st.write(title_name_02)
#             st.write('2.', title_name_02)
#             title_name_03 =title_03['title']
#             # st.write(title_name_03)
#             st.write('3. ', title_name_03)
#             title_name_04 =title_04['title']
#             # st.write(title_name_04)
#             st.write('4.', title_name_04)
#             title_name_05 =title_05['title']
#             # st.write(title_name_05)
#             st.write('5. ',title_name_05)
#         rand = link_create('https://raw.githubusercontent.com/hjorturlarsen/IMDB-top-100/master/data/movies.json')

#         st.write('**NOTE : **','This app is made for fun perpous dont take it seriously')
        # st.markdown('--------------------------------------------------------------')
    st.markdown("<h2 style='text-align: center; color: #ffff;'> Popular TV Shows</h2>", unsafe_allow_html=True)
    st.write( "           ")
    st.caption('''Are you interest in TV shows? Here you can check it. The Most Popular TV Shows of All time based on IMDB ranked randomly suggests three TV  Shows. Hit the refresh button to get new results every time.''')
    col1,col2,col3, col4, col5 = st.columns(5)
    with col1:
        pass
    with col2:
        pass
    with col3:
        refresh_button = st.button('Refresh ↻')
    with col4:
        pass
    with col5:
        pass
    if refresh_button:
       
        def tv_show_link(link):
            request_file = requests.get(link)
            file_convert = request_file.json()
        
            # st.write(tv_show_posters)
            # Random number generate
            rand_data = random.sample(file_convert,5)
            random_no_1 = rand_data[0]
            random_no_2 = rand_data[1]
            random_no_3 = rand_data[2]
            random_no_4 = rand_data[3]
            random_no_5 = rand_data[4]
        
            # Tv show title fetch 01
            title_01 = random_no_1['name']
        
            # Tv show posters fetch  01
            poster_index_01 = random_no_1
            tv_show_posters = poster_index_01['image']
            poster_img_01 = tv_show_posters['medium']
        
            # Tv show title fetch 02
            title_02 = random_no_2['name']
        
            # Tv show posters fetch  02
            poster_index_02 = random_no_2
            tv_show_posters = poster_index_02['image']
            poster_img_02 = tv_show_posters['medium']
        
            # Tv show title fetch 03
            title_03 = random_no_3['name']

            # Tv show posters fetch  03
            poster_index_03 = random_no_3
            tv_show_posters = poster_index_03['image']
            poster_img_03 = tv_show_posters['medium']

            # Tv show title fetch 04
            title_04 = random_no_4['name']
        
            # Tv show posters fetch  04
            poster_index_04 = random_no_4
            tv_show_posters = poster_index_04['image']
            poster_img_04 = tv_show_posters['medium']
        
            # Tv show title fetch 05
            title_05 = random_no_5['name']
        
            # Tv show posters fetch  05
            poster_index_05 = random_no_5
            tv_show_posters = poster_index_05['image']
            poster_img_05 = tv_show_posters['medium']
      
        
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(poster_img_01)
                st.markdown("<h4 style='text-align: center; color: #9277E8;'> {}</h4>".format(title_01), unsafe_allow_html=True)
            
            with col2:
                st.image(poster_img_02)
                st.markdown("<h4 style='text-align: center; color: #9277E8;'> {}</h4>".format(title_02), unsafe_allow_html=True)
            with col3:
                st.image(poster_img_03)
                st.markdown("<h4 style='text-align: center; color: #9277E8;'> {}</h4>".format(title_03), unsafe_allow_html=True)

 
        #link of json file
        rand = tv_show_link('https://raw.githubusercontent.com/Rafikul10/Movies/main/tv_shows.json') 
        st.write('-----')   
 
    