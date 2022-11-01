import streamlit as st
import sqlite3
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import extra_streamlit_components as stx
# heading of the page 
st.markdown("<h1 style='text-align: center; color: #C059C0;'> Project Workflow</h1>", unsafe_allow_html=True)
st.write('\n')
# columns for shields 
_ ,col2,_= st.columns([0.1,2,0.1])

with col2:
    st.write('''[![Data kaggle](https://img.shields.io/badge/Data-Kaggle-blueviolet)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) 
             [![MYSQL](https://img.shields.io/badge/DataBase-MySQL-blue)](https://dev.mysql.com/doc/) 
             [![Python 3.10.0](https://img.shields.io/badge/Python-3.10.0-brightgreen)](https://www.python.org/downloads/release/python-3100/) 
             [![Github](https://camo.githubusercontent.com/3a41f9e3f8001983f287f5447462446e6dc1bac996fedafa9ac5dae629c2474f/68747470733a2f2f62616467656e2e6e65742f62616467652f69636f6e2f4769744875623f69636f6e3d67697468756226636f6c6f723d626c61636b266c6162656c)](https://github.com/Rafikul10?tab=repositories) 
             [![Streamlit 1.14.0](https://img.shields.io/badge/Streamlit%20-1.14.0-Ff0000)](https://docs.streamlit.io/) 
             [![Cloud Platform](https://img.shields.io/badge/CloudPlatform-Heroku-9cf)](https://www.heroku.com/managed-data-services)''')

st.write('-----')

# animated image loading function 
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# columns for animated image and description of page
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='text-align: center; color: #fffff;'> Description</h3>", unsafe_allow_html=True)
    st.caption(f'''Movie Recommendation System is a simple Machine Learning Project.
               By collecting the data from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
               i started the project and then i 
               did some preprocessing on the dataset and build the final model. 
               It takes one movie name as an input and suggests 5 more movie names. 
               For fetching all information (Release Date, Types, Ratings, Trailer, 
               Tag line, Overview) i used API keys. For more information scroll down 
               and check out the Website Build page. Output of the code is not available 
               write all code in your notebook and run to see the output!
                
               ''')

# url of animated image
lotti_ur = load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_w51pcehl.json')
# second grid for animated image   
with col2:
    st_lottie(lotti_ur,
          speed = 1,
          key=None,
          height=280,
          width=350,
          quality='high',
          reverse=False
          )
q = st.sidebar.text('Ask Questions')
with q:
    
    col1 , _ = st.columns([1,0.000001])
    with col1:
        st.markdown("<h4 style = 'text-align: left; color:  #ffff;'>\n 📝 How can i help you?  </h4>",unsafe_allow_html=True)
        questions = st.text_area('',placeholder='''Write your Queries*''')
        
            
            
        user_email = st.text_input('',placeholder='Email Id*')                 
        submit_prob = st.button('Submit')
        if submit_prob:
            if questions == '':
                st.markdown('''<h8 style = 'text-align:left; color: red; opacity: 70%'> _Fill the quesries box before submit_</h8>''',unsafe_allow_html=True)
            elif user_email == '':
                st.markdown('''<h8 style = 'text-align:left; color: red; opacity: 70%'> _Invalid Email id_</h8>''',unsafe_allow_html=True)
            else:    
                st.markdown('''<h8 style = 'text-align:left; color: green; opacity: 70%'> _Sucessfully submitted!_</h8>''',unsafe_allow_html=True)
                _conect_queries = sqlite3.connect('queries.db')
                c = _conect_queries.cursor()
                def create_table(): 
                    c.execute('CREATE TABLE IF NOT EXISTS queries( Email TEXT, Questions TEXT)')
               
                
                def add_querise(user_email, questions ):  
                    c.execute('INSERT INTO queries (Email, Questions) VALUES (?,?)',(user_email, questions))
                    _conect_queries.commit()
                # table create function called
                create_table()
                # added all data 
                add_querise(user_email,questions,)
                
         
st.write('-----')
st.markdown("<h2 style='text-align: center; color: #C059C0;'>  Steps </h2>", unsafe_allow_html=True)

val = stx.stepper_bar(steps=["DataCollection🗂️", "Preprocessing👨‍💻", "Model Build🤖",'Website Build🌐','Deployment🎯'])

if val == 0:
    st.write('----')
    st.markdown("<h2 style='text-align: center; color: #C059C0;;'> Data Collection Processs</h2>", unsafe_allow_html=True)
    # columns create for align the text in middle
    col1, col2, col3 = st.columns([0.35,1,0.1])
    with col1:
        pass
    with col2:
        st.write('''[![Data Kaggle](https://img.shields.io/badge/Data-Kaggle-blueviolet)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)
                 [![Size](https://img.shields.io/badge/Size-45.74mb-br)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)
                 [![File Format](https://img.shields.io/badge/FileFormat-.csv-blue)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)
                 [![streamlit](https://camo.githubusercontent.com/3a41f9e3f8001983f287f5447462446e6dc1bac996fedafa9ac5dae629c2474f/68747470733a2f2f62616467656e2e6e65742f62616467652f69636f6e2f4769744875623f69636f6e3d67697468756226636f6c6f723d626c61636b266c6162656c)](https://github.com/Rafikul10?tab=repositories)''')
    
    st.write('\n')
    st.markdown(f'''<h4 style = 'text-align: left;'> Dependencies :</h4>''',
                    unsafe_allow_html=True)
    st.markdown(f'''* Jupyter Notebook''') 
    st.markdown(f'''* Python 3.10.0''')
    st.markdown(f'''* Pandas''')
    st.markdown(f'''* Numpy''')
    st.caption(f'''Install dependencies using [conda](https://docs.conda.io/en/latest/)''')
    # st.write('--')
    st.write('Setup :')
    st.code('''import numpy as np \nimport pandas as pd''')
    st.write('Data Import :')
    st.caption('''
               Two different datase is there movies and credits
               import both the dataset and merge it in one data.''')
    st.code('''
            movies = pd.read_csv('tmdb_5000_movies.csv')   # movies dataset\n
credits = pd.read_csv('tmdb_5000_credits.csv') # credits dataset\n
display(movies.head(3))  # check the movie dataset
            ''')
    st.code('''display(movies.head(3))  # check the movie dataset''')
    st.write('Merge Both Dataset :')
    st.caption('''Both dataste have one same column 'title'
               merge both data basis on common 'title' column''')
    st.code('''
            movies = movies.merge(credits, on='title') # merge movies and credits data on 'title'\n
movies.head(1)
            ''')
    st.code('movies.info()')
    st.write('\n')
    
    st.write('**Note** : Data collection is done now for further process check 2nd step - **Preprocessing** from top.')
    st.write('\n')
    st.write('\n')
    st.caption('''For full code with output check my [GitHub](https://github.com/Rafikul10/Movies) repositories.''')   

# now preprocessing page
if val == 1:
    st.write('---')
    st.markdown("<h2 style='text-align: center; color: #C059C0;;'> Data Preprocessing</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.32,1,0.1])
    with col1:
        pass
    with col2:
        st.write('''[![Data Kaggle](https://img.shields.io/badge/Data-Kaggle-blueviolet)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)
                 [![streamlit](https://camo.githubusercontent.com/3a41f9e3f8001983f287f5447462446e6dc1bac996fedafa9ac5dae629c2474f/68747470733a2f2f62616467656e2e6e65742f62616467652f69636f6e2f4769744875623f69636f6e3d67697468756226636f6c6f723d626c61636b266c6162656c)](https://github.com/Rafikul10?tab=repositories)
                 [![Python 3.10.0](https://img.shields.io/badge/Python-3.10.0-brightgreen)](https://www.python.org/downloads/release/python-3100/)
                 [![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0.2-red)](https://scikit-learn.org/stable/)''')
                 
    with col3:
        pass
    st.write('\n')
    st.markdown(f'''<h4 style = 'text-align: left;'> Dependencies :</h4>''',
                    unsafe_allow_html=True)
    st.markdown(f'''* Jupyter Notebook''') 
    st.markdown(f'''* Python 3.10.0''')
    st.markdown(f'''* scikit-learn 1.0.2''')
    st.markdown(f'''* Pandas''')
    st.markdown(f'''* Numpy''')
    st.caption(f'''Install dependencies using [conda](https://docs.conda.io/en/latest/)''')
    st.markdown(f'''<h4 style = 'text-align: left;'> Preprocessing :</h4>''',
                    unsafe_allow_html=True)
    
    # st.write('**Preprocessing :**')    
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%'> _In movies dataset have 22 columns but 
i will be used only few importants column to build the model columns will be used for make 
the model ('genres', 'id', 'keywords', 'title', ''overview', 'cost', 'crew')_</h7>''',unsafe_allow_html=True)
    st.code ('''movies['original_title'].value_counts()''')
    st.write('Final Data :')
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%'>_Make a final dataset with the columns which will be used to make
model ('genres', 'id', 'keywords', 'title', ''overview', 'cost', 'crew')._</h7>''',unsafe_allow_html=True) 
    st.code('''movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']] #final dataset\n
movies.head(1)  # check 1 data from final dataset''')
    st.code('''movies.info()''')
    st.code('''movies.isnull().sum()  # check missing values in dataset''')
    st.code("movies.dropna(inplace=True)  # 3 missing values found in overview rows so, i drop those 3 rows")
    st.code("movies.duplicated().sum()   # check duplicat data")
    st.code("movies.iloc[0].genres  # print first data of genres column")
    st.code('''#Now 'genres' column look like 👉 '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, 
#{"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]'
#take all 'name' from genres column and list it like this 👉 {'Action','Adventure','Fantasy','Scifi'}''')
    st.code('''import ast   # ast libray cahnage the str list to an lsit
# function create for convert the obj into list
# only specially for 'genres' and 'keywords' column
# for cast and crew columns i make different different 
# function which is shwon below\n
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L''')
    
    st.code('''ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')''')
    st.code('''movies['genres'] = movies['genres'].apply(convert)  # now replace the previous 'genres' column 
                                                    # with new genres column ''')
    st.code('''movies.head(1)    # check genres column now it's changed to new one''')
    st.code('''movies['keywords'] = movies['keywords'].apply(convert) # also apply same function in 'Keywords' column''')
    st.code('''movies['cast'][0] # check the data of 1 cast column''')
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%'> _In cast column have so much information about the movies from all the information i take only one important information 
from cast column top 3 dictionary will be take beacuse there have actor's name_</h7>''',unsafe_allow_html=True)
    st.code('''# function for convert the cast columns in a list
\ndef convert_cast(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L''')
    st.code('''movies['cast'] = movies['cast'].apply(convert_cast)  # apply of conver_cast column function''')
    st.code('''movies.head(1)  # now check cast columns''')
    st.code('''movies['crew'][0]  # check crew column''')
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%'>_In the crew column also have huge data about the movie but 
i will take only 'director' name of that movie 
 director name store in 'job' so, where job == 'Director' 
 pick that name and replace it in existing crew column_ </h7>''',unsafe_allow_html=True)
    st.code('''# function for conver_crew columns \n
def convert_crew(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director': 
            L.append(i['name']) 
            break
    return L''')
    st.code('''movies['crew'] = movies['crew'].apply(convert_crew)  # apply convert_csre function and replace the existing column''')
    st.code('''movies.head(1)  # now check all data , it's done!''')
    st.code('''movies['overview'][0]   # now check 1 overview columns data''')
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%'> _This is a string conver it into list so, i can append with others column_
</h7>''',unsafe_allow_html=True)
    st.code('''movies['overview'] = movies['overview'].apply(lambda x:x.split()) \n# Applyed a lambda function for 
# split the string and make it a list 
''')
    st.code('''# movies['overview'][0] \n
movies.head(1)   # check the overview''')
    
    st.code('''# labda function apply only for - 'genres', 'keywords', 'cast', 'crew' columns -->\n 

# 1.Changes on generes column 
movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x]) \n
# 2.Changes on 'keywords' column 
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x]) \n
# 3.Changes on 'cast' colum 
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x]) \n
# 4.Changes on 'crew' column 
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])''') 
    
    st.code('movies.head(5) # After apply all changes dataset look like this')
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%'>_Now i make a new column 'tags' , in this column 
i add all others 5 columns('overview', 'genres',
'keywords', 'cast', 'crew') data in 'tags' column_
</h7>''',unsafe_allow_html=True)
    st.code('''# Merge all data in 'tags' column 
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew'] ''')
    st.code('movies.head(1) ')
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%'>_Now all data is present in a single 'tags' column so i create a new_df data and remove all the others 
columns('overview','genres', 'keywords', 'cast', 'crew') 
beacuse it's not requied i stored all the data in one 
'tags' column and keept only 3 columns('movie_id', 'title', 'tags')_
</h7>''',unsafe_allow_html=True)
    st.code('''new_df = movies[['movie_id','title','tags']]  # create new_df with only 3 columns('movie_id','title','tags') \nnew_df''')
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%'>_All are in list so i convert them into a string_
</h7>''',unsafe_allow_html=True)
    st.code('''new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))   # conver 'tags' column into string''')
    st.code('new_df.head(1)  ')
    st.code('''new_df['tags'][0]   # First data of 'tags' column''')
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%'>_For better performance convert the string to lower case_
</h7>''',unsafe_allow_html=True)
    st.code('''new_df['tags'] = new_df['tags'].apply(lambda x:x.lower()) \n#Apply lowercase on 'tags' column it will 
# convert 'tags' column data into lower case''')
    st.code('''new_df.head() # now all 'tags' column data in lower case''')
    st.code('''new_df['tags'][0]   # 1st data of 'tags' column''')
    st.code('''new_df['tags'][1]  # 2nd data of 'tags' column''')
    st.write('\n')
    st.caption('**Note** : Data preprocessing is done now for further process check 3rd step - **Model Build** from top.')
    st.write('\n')
    st.write('\n')
    st.caption('''👨‍💻For code with output check my [GitHub](https://github.com/Rafikul10/Movies) repositories.''')   
    

# Model build page --
if val == 2:
    st.write('---')
    st.markdown("<h2 style='text-align: center; color: #C059C0;;'> Model Build</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.33,1,0.1])
    with col1:
        pass
    with col2:
        st.write('''[![Text Vectorization](https://img.shields.io/badge/TextVectorization-%20BoW-blueviolet)](https://towardsdatascience.com/text-vectorization-bag-of-words-bow-441d1bfce897)
                 [![nltk](https://img.shields.io/badge/nltk-3.6.7-brightgreen)](https://www.tutorialspoint.com/natural_language_processing/natural_language_processing_python.htm)
                 [![cosine similarity](https://img.shields.io/badge/sklearn-cosine__similarity-blue)](https://www.machinelearningplus.com/nlp/cosine-similarity/)''')
    with col3:
        pass
    st.write('\n')
    st.markdown(f'''<h4 style = 'text-align: left;'> Dependencies :</h4>''',
                    unsafe_allow_html=True)
    st.markdown(f'''* Jupyter Notebook''') 
    st.markdown(f'''* Python 3.10.0''')
    st.markdown(f'''* scikit-lean''')
    st.markdown(f'''* nltk 3.6.7''')
    st.markdown(f'''* Pandas''')
    st.markdown(f'''* Numpy''')
    st.caption(f'''Install dependencies using [conda](https://docs.conda.io/en/latest/)''')
    
    st.markdown(f'''<h4 style = 'text-align: left;'> Model Build :</h4>''',
                    unsafe_allow_html=True)
    
    
    # st.write('**Model Build :**')     
    
    st.markdown(f'''<h4 style = 'text-align: center; color: #9277E8'> 📈Text Vectorization: Bag of Words (BoW) </h4>''',unsafe_allow_html=True)
    st.markdown(f'''<h8 style = 'text-align: center; opacity: 50%;'> This vectorization technique converts 
                the text content to numerical feature vectors. Bag of Words takes a document from a 
                corpus and converts it into a numeric vector by mapping each document word to a feature 
                vector for the machine learning model.
                </h8>''',unsafe_allow_html=True)
    
    
    st.markdown(f'''<h8 style = 'text-align: left; ;'>**Need for text vectorization :**</h8>''',unsafe_allow_html=True)

    st.markdown(f'''<h8 style = 'text-align: left; opacity: 50% ;'> 

>Let’s say we have reviews of a movies. Text reviews provided by the customers are of different lengths. By converting from text to numbers, we can represent a review by a finite length of the vector. In this way, the length of the vector will be equal for each review, irrespective of the text length.
>Bag of words is the most trivial representation of text into vectors. Each column of a vector represents a word. The values in each cell of a row show the number of occurrences of a word in a sentence.</h8>''',unsafe_allow_html=True)

    st.markdown(f'''<h8 style = 'text-align: left;  ;'> **Example :**</h8>''',unsafe_allow_html=True)
    st.image('https://miro.medium.com/max/828/1*PuyVAffx2GLwqzZmmOE52w.png')
    st.markdown(f'''<h8 style = 'text-align: left; opacity: 50% ;'>
                
>The initial step is to find a vocabulary of unique words (ignoring the punctuation and cases). Vocabulary in the above example:
>[This, movie, is, the, good, of, times, not, I, love, watch, you, will, it, too]
>In our vocabulary, we have 15 unique words. Therefore, each movie review is represented by a vector of 15 dimensions (each word representing a dimension). For the reviews:</h8>''',unsafe_allow_html=True)
    st.image('https://miro.medium.com/max/1400/1*S8uW62e3AbYw3gnylm4eDg.png')
    st.markdown(f'''<h8 style = 'text-align: left; opacity: 50% ;'>

>The values corresponding to each word shows the number of occurrences of a word in a review. Similarly, 15-dimension vectors represent the remaining reviews.</h8>''',unsafe_allow_html=True)
    st.markdown(f'''<h8 style = 'text-align: left ;'> **NOTE** - If you want to learn more about Text Vecorization click [here](https://towardsdatascience.com/text-vectorization-bag-of-words-bow-441d1bfce897).</h8>''',unsafe_allow_html=True)
    
    st.markdown(f'''<h4 style = 'text-align: center; color: #9277E8'> Natural Language Preprocessing </h4>''',unsafe_allow_html=True)
    st.markdown(f'''<h8 style = 'text-align: left ; opacity: 50% '>
                
>In Natural Language Processing (NLP), unnecessary words are called stopwords. nltk library already contains the list of stopwords. There are 179 stopwords in English.</h8>''',unsafe_allow_html=True)
    st.code('''# install nltk library 
!pip install nltk''')
    st.code('''# import nltk library for steming 
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

ps = PorterStemmer()  # stem define, used in below code
cv = CountVectorizer(max_features=5000,stop_words='english')
# mentioned stop_words = 'english', 
# # max_features = no of features should create
# it can be any number but here i set it to 
# 5000 if features is increased more 
# computational power required''')
    
    st.markdown(f'''<h5 style = 'text-align: left ;'> STEM :</h5>''',unsafe_allow_html=True)
    st.markdown(f'''<h5 style = 'text-align: left; opacity: 50%;;'>
                
>stem change slidely different words into same words as example
>["love",'loving','lovers']
>stem will convert the above list to like this one - ['love','love','love']

Example :
ps.stem('loved')

Output : love</h5>''',unsafe_allow_html=True)
    st.code('''# stem function
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)''')
    st.code('''new_df['tags'] = new_df['tags'].apply(stem)    # apply stem function to 'tags' column and replacing the data''')
    st.code('''vectors = cv.fit_transform(new_df['tags']).toarray()  
# cv.fit_transform change everyting into verctorize form of 0,1 (1=true, 0=false)''')
    st.code('''vectors[0]   # check fast vector''')
    st.code('''len(cv.get_feature_names())    # len of features 5000 ,i set it previously as max_features 5000''')
    st.code('''cv.get_feature_names()''')
    
    st.markdown(f'''<h4 style = 'text-align: center; color: #9277E8'> 📈Cosine Similarity </h4>''',unsafe_allow_html=True)
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%;'> 
                
>cosine similarity is the cosine of the angle between them, that is, the dot product of the vectors divided by the product of their lengths. It follows that the cosine similarity does not depend on the magnitudes of the vectors, but only on their angle. The cosine similarity always belongs to the interval [-1,1], [-1,1]. For example, two proportional vectors have a cosine similarity of 1, two orthogonal vectors have a similarity of 0, and two opposite vectors have a similarity of -1. The cosine 
>similarity is particularly used in positive space, where the outcome is neatly bounded in [0,1] [0,1] </h7>''',unsafe_allow_html=True)
    st.image('https://www.machinelearningplus.com/wp-content/uploads/2018/10/soft-cosine.png')
    st.markdown(f'''<h7 style = 'text-align: left; opacity: 50%;'> 

> Here i used cosine smilarity function for calculate the angle between every movies.</h7>''',unsafe_allow_html=True)
    
    st.markdown(f'''<h7 style = 'text-align: left; '> NOTE : Click [here](https://en.wikipedia.org/wiki/Cosine_similarity) for details information about cosine similarity</h7>''',unsafe_allow_html=True)
    st.code('''# Import cosine_similarity from sklearn
from sklearn.metrics.pairwise import cosine_similarity''')
    st.code('''similarity = cosine_similarity(vectors) ''')
    st.code('''similarity[1] # after apply cosine_similarity its convert all vecors in between 0-1''')
    
    st.markdown(f'''<h5 style = 'text-align: left ;'> ❗Problem :</h5>''',unsafe_allow_html=True)
    st.markdown(f'''<h7 style = 'text-align: left; opacity:50% '> 
                
>To find the distance between similar movies i sorted the list but when i sorted then index number is chnaging beacuse the 
>index number is fixed but when movies sorted again and again as per similarity it's change the index number, as an example 
> --> [ 1 = 'Movie_1' and 2 = 'Movie_2' if i sorted the data then it may be change into this --> 1 = 'Movie_2' and 2 = 'Movie_1' ] 
>that is the main problem here in order to avoid that problem i assigned fixed one index number in exach movie so, again we can say 
>that 1st index for 1st movie only , 2nd index for 2nd movie,...to fixed the index number in every movie i used enumerate function to 
>fixed the index number of all movies and lambda is used for sorted by 2nd similarity key not sort by enumerate.</h7>''',unsafe_allow_html=True)
    st.code('''# function for sorted and enumerate the data
sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]''')
    st.code('''# recomended function - this will be take a input of movie name and will be recommended 5 movies name 
def recommend(movie):
    movie_index =new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    for i in movies_list:
        # print the name of the movies from new_df title column
        print(new_df.iloc[i[0]].title)''')
    st.code('''recommend('Batman Begins')   # test the model''')
    st.markdown(f'''<h5 style = 'text-align: left ;'> 📂Save Model :</h5>''',unsafe_allow_html=True)
    st.markdown(f'''<h7 style = 'text-align: left; opacity:50% '>
                
>By using pickle library saved the model in .pkl format so, i can load this .pkl file again in vs code to use it in Web Application
</h5>''',unsafe_allow_html=True)
    st.code('''# Import pickle to save it in .pkl format
import pickle''')
    st.code('''# save it in 'wb' mode, 'wb' means write binary
# and can open it byt 'rb' mode , 'rb' mean right binary 
pickle.dump(new_df,open('movies.pkl','wb'))''')
    st.code('''# Created a dictionaty with movies name from dataset so i can share this 
# list to user for pick one movie and as per pick model will recommend 5 movies
pickle.dump(new_df.to_dict(),open('movies_dict.pkl','wb'))''')
    st.code('''new_df.to_dict()''')
    st.code('''# pickle the similarity matrix function for website
pickle.dump(similarity,open('similarity.pkl','wb'))''')
    st.write('\n')
    st.write('**Note** :Now model is ready for suggests the movies name. For build Web Application by using this model check 4th step - **Web Application** from top.')
    st.write('\n')
    st.write('\n')
    st.caption('''👨‍💻For code with output check my [GitHub](https://github.com/Rafikul10/Movies) repositories.''')   
    
    
    
if val == 3:
    st.write('----')
    st.markdown("<h2 style='text-align: center; color: #C059C0;;'> Web Application Build</h2>", unsafe_allow_html=True)
    # columns create for align the text in middle
    col1, col2, col3 = st.columns([0.3001,1,0.1])
    with col1:
        pass
    with col2:
        st.write('''[![Python](https://img.shields.io/badge/Python-3.10.0-brightgreen)](https://www.python.org/downloads/release/python-3100/)
                 [![Streamlit](https://img.shields.io/badge/Streamlit%20-1.14.0-Ff0000)](https://docs.streamlit.io/library/get-started)
                 [![MYSQL](https://img.shields.io/badge/DataBase-MySQL-blueviolet)](https://dev.mysql.com/doc/)
                 [![streamlit](https://camo.githubusercontent.com/3a41f9e3f8001983f287f5447462446e6dc1bac996fedafa9ac5dae629c2474f/68747470733a2f2f62616467656e2e6e65742f62616467652f69636f6e2f4769744875623f69636f6e3d67697468756226636f6c6f723d626c61636b266c6162656c)](https://github.com/Rafikul10?tab=repositories)''')
    st.write('\n')
    st.markdown(f'''<h4 style = 'text-align: left;'> Dependencies :</h4>''',
                    unsafe_allow_html=True)
    st.markdown(f'''* Python 3.10.0''')
    st.markdown(f'''* Streamlit 1.14.0''')
    st.markdown(f'''* Pandas''')
    st.markdown(f'''* Numpy''')
    st.markdown(f'''* MySQL''')
    st.caption('''This website Application build by using Python, steamlit library and to store the data of all users i used MySQL.
It's an secured🔐 safe Application for safe all data of the users i used **HASHED** function.''')
    
    st.write('')
    st.subheader('Pages :')
    st.caption('''
               
               >web Application build with total 4pages which are shown below for individual page code is diiferent
               >. If you wnana check how i build
               >the full website and used the machine learning model(.pkl) file in it.
               >check my [GitHub](https://github.com/Rafikul10/Movies) Repositories. Thank You!''')
    st.markdown(f'''* Login page''')
    st.markdown(f'''* Home page''') 
    st.markdown(f'''* Project Workflow page''') 
    st.markdown(f'''* Other's page''') 
    st.write('---')
    st.markdown(f'''<h4 style = 'text-align: center;color:#9277E8;'> Login Page </h4>''',
                    unsafe_allow_html=True)
    st.write('\n')
    st.markdown(f'''<h8 style='text-align: center; color: #fffff; opacity: 50%;'>In this page user can create a account or can login a previously created account. All details of 
                user is stored in HASHEd format. After create a account sucessfully the 
                data is store in MySQL DataBase when user try to log in user given password match with the password used to create the account.
                </h8>''',
                    unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    
    st.markdown(f'''<h5 style = 'text-align: left;'>🔒 How Password Hashes Work :</h5>''',
                    unsafe_allow_html=True)
    st.caption('''
>Most passwords are hashed using a one-way hashing function.
 >Hashing functions take the user’s password and use an algorithm 
 >to turn it into a fixed-length of data. The result is like a unique fingerprint,
 >called the digest, that cannot be reversed to find the original input. So, even if 
 >someone gets access to the database storing your hash password, there is no key to 
 >decrypt it back to its original form. For better understaning i attached a image from my Application 
 >DataBase check it out -''')
    
    st.image('https://i.ibb.co/L1bJbvC/pass.png')
    st.markdown(f'''<h7 style = 'text-align: left;opacity: 50%;'>**👨‍💻Note:** For all code of the login page check out [GitHub](https://github.com/Rafikul10/Movies) Repositories :</h7>''',
                    unsafe_allow_html=True)
    
    st.markdown(f'''<h4 style = 'text-align: center; color: #9277E8;'> Home Page </h4>''',
                    unsafe_allow_html=True)
    st.write('\n')
    
    st.markdown(f'''<h7 style='text-align: center; color: #fffff; opacity: 50%;'>Home page is for recommendation of movies and to check out top TV Shows
                this two are different paged nested in Home page. In order to fetch the poster ,movie name, type of movie
                ratings,release date of the movie, trailer and overview by Movie Name  i used **API** key which i got from[TMDB](https://www.themoviedb.org/settings/api) official website.
                Check i attached a image of **API** key</h7>''',
                    unsafe_allow_html=True)
    st.image('https://i.ibb.co/DGPQ5xY/api.png')
    st.write('\n')
    st.write('\n')
    st.markdown(f'''<h4 style='text-align: left; color: #fffff; '>Request of json file using API Key :</h4>''',unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.markdown(f'''<h7 style='text-align: left; color: #fffff; opacity: 50%;'> 
                
>By using the above API key i request json file of every movie_id ehich is predicted by machien learning model for user.
>and from there fetched all the data and used it for my Application. I share a image for guidance how to use API key to 
>get json file for every movies and for TV shows i did the same things. Click [here](https://developers.themoviedb.org/3/movies/get-movie-details) for more info.
                    ''',unsafe_allow_html=True)
    st.image('https://i.ibb.co/d54TWnt/The-Movie-Database-API.png')
    st.caption('NOTE: For all code check [GitHub](https://github.com/Rafikul10/Movies) Repositries.')
    
    st.markdown(f'''<h4 style = 'text-align: center;color:#9277E8;'>Project Workflow Page :</h4>''',
                unsafe_allow_html=True)
    st.caption('''In this page i added all the information with links about **Movie Recommendation System** projet. All code is written in [VS Code](https://code.visualstudio.com/) editor
               .''')
    st.caption('👨‍💻NOTE: For all code check [GitHub](https://github.com/Rafikul10/Movies) Repositries.')
    
    st.markdown(f'''<h4 style = 'text-align: center;color:#9277E8;'>Other's Page :</h4>''',
                unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')

    st.caption('''Other's page devided with three different section 'Feedback', 'Reports' and 'User DataBase' -
               \n * I added Feedback page for user to give there feedbacks so, i can improve teh Application in future.
               \n * Reports page is for report if something going wrong with the Application. I'll try to fixed it after recived a report from user(s).
               \n * User DataBase is not accessable page for anyone. Only admin can acccess beacuse there have some credintials information about 
               all users. It's complete secured with password and if someone decrypt the password they can't do anything with user information
                , beacuse all password is in **HASHED** from as i mentioned earlier with a iamge. Feel free to use the Application 
                I hope You like the whole application. Thank you! for use it. I appriciate it!❤️
               ''')
    st.write('\n')
    st.write('\n')    
    st.caption('''👨‍💻NOTE: For code check [GitHub](https://github.com/Rafikul10/Movies) repositories.''')   

    
if val == 4:
    st.write('---')    
    st.markdown("<h2 style='text-align: center; color: #C059C0;;'> Deployment</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.39,1,0.1])
    with col1:
        pass
    with col2:
        st.write('''[![Cloud](https://img.shields.io/badge/CloudPlatform-Heroku-blue)](https://devcenter.heroku.com/categories/reference)
                 [![Streamlit](https://img.shields.io/badge/Streamlit%20-1.14.0-Ff0000)](https://streamlit.io/)
                 [![streamlit](https://camo.githubusercontent.com/3a41f9e3f8001983f287f5447462446e6dc1bac996fedafa9ac5dae629c2474f/68747470733a2f2f62616467656e2e6e65742f62616467652f69636f6e2f4769744875623f69636f6e3d67697468756226636f6c6f723d626c61636b266c6162656c)](https://github.com/Rafikul10?tab=repositories)
                 ''')
    with col3:
        pass  
        
    st.caption('''Now it's ready for deploy in any cloud server. In my case i choose Heroku cloud server for deploy the Application. In
               order to deploy the Application on Heroku first create an account and login to your account. After sucessfully logged in.
               You can deploy your application directly by downloading the CLI from official website of
               Heroku for all processs check [Heroku](https://devcenter.heroku.com/categories/reference) official website.''')
    
    st.caption('''👨‍💻NOTE: For code check [GitHub](https://github.com/Rafikul10/Movies) repositories.''')   
    
    