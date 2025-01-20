import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open("C:/Users/HP/Downloads/imdb (1).pkl",'rb') as file:
    imdb=pickle.load(file)

st.title('IMDB rating prediction App')

st.header('Enter movie details : ')

genres={'Action, Adventure, Thriller': 13,
 'Crime, Drama, Thriller': 220,
 'Crime, Drama': 209,
 'Action, Adventure, Sci-Fi': 12,
 'Action, Adventure, Drama': 5,
 'Comedy, Drama, Sport': 168,
 'Action, Adventure, Comedy': 3,
 'Animation, Action, Adventure': 110,
 'Comedy, Drama': 158,
 'Crime, Drama, Mystery': 216,
 'Drama, Sci-Fi': 289,
 'Comedy, Crime, Drama': 149,
 'Action, Drama, History': 40,
 'Action, Fantasy, Mystery': 52,
 'Action, Adventure, Fantasy': 7,
 'Action, Horror, Mystery': 56,
 'Drama': 245,
 'Horror, Thriller': 321,
 'Horror, Mystery, Thriller': 318,
 'Crime, Horror, Mystery': 225,
 'Drama, Mystery, Thriller': 281,
 'Biography, Drama, Musical': 142,
 'Drama, Mystery, Sci-Fi': 280,
 'Action, Drama, Sci-Fi': 45,
 'Animation, Adventure, Comedy': 115,
 'Drama, Horror, Sci-Fi': 270,
 'Crime': 208,
 'Drama, Horror, Mystery': 268,
 'Comedy, Family, Fantasy': 172,
 'Adventure, Comedy, Crime': 71,
 'Action, Sci-Fi, Thriller': 64,
 'Adventure, Drama, Fantasy': 84,
 'Action': 0,
 'Comedy, Drama, Romance': 166,
 'Action, Crime, Drama': 30,
 'Thriller': 346,
 'Comedy, Fantasy': 178,
 'Drama, Western': 296,
 'Comedy, Crime': 148,
 'Action, Adventure, Crime': 4,
 'Drama, Thriller, Western': 294,
 'Drama, Sci-Fi, Thriller': 290,
 'Drama, Musical': 276,
 'Drama, Horror, Thriller': 271,
 'Comedy, Drama, Thriller': 169,
 'Drama, Romance': 283,
 'Romance': 331,
 'Biography, Crime, Drama': 137,
 'Western': 347,
 'Adventure, Comedy, Family': 73,
 'Crime, Horror, Thriller': 227,
 'Horror, Mystery': 316,
 'Drama, Thriller': 292,
 'Crime, Mystery, Thriller': 232,
 'Action, Drama, Mystery': 43,
 'Action, Sci-Fi': 63,
 'Biography, Comedy, Crime': 135,
 'Adventure, Family, Fantasy': 93,
 'Biography, Drama, Romance': 143,
 'Comedy': 147,
 'Drama, Musical, Romance': 277,
 'Action, Crime, Thriller': 36,
 'Comedy, Romance': 199,
 'Action, Crime, Mystery': 33,
 'Horror': 314,
 'Action, Thriller': 65,
 'Action, Horror, Thriller': 58,
 'Drama, Sport': 291,
 'Action, Adventure, Horror': 9,
 'Biography, Drama, Music': 141,
 'Animation, Family, Fantasy': 129,
 'Adventure, Drama, Sci-Fi': 89,
 'Comedy, Horror, Musical': 185,
 'Action, Drama, Horror': 41,
 'Crime, Drama, History': 212,
 'Action, Drama, War': 48,
 'Drama, Fantasy, Horror': 253,
 'Comedy, Horror': 183,
 'Drama, Romance, Western': 288,
 'Mystery, Romance, Sci-Fi': 325,
 'Comedy, Drama, Family': 159,
 'Action, Comedy, Fantasy': 21,
 'Short, Horror, Sci-Fi': 343,
 'Drama, Horror': 265,
 'Comedy, Drama, Sci-Fi': 167,
 'Comedy, Fantasy, Horror': 179,
 'Fantasy, Horror': 304,
 'Comedy, Drama, Horror': 162,
 'Fantasy, Horror, Mystery': 305,
 'Action, Comedy, Crime': 18,
 'Adventure, Drama, War': 91,
 'Drama, Music': 273,
 'Family, Fantasy, Horror': 298,
 'Drama, History, Thriller': 263,
 'Comedy, Mystery, Romance': 196,
 'Animation, Drama, Family': 124,
 'Drama, Fantasy, Romance': 255,
 'Biography, Drama, History': 140,
 'Drama, Fantasy, Mystery': 254,
 'Action, Mystery, Sci-Fi': 60,
 'Adventure, Sci-Fi, Thriller': 106,
 'Crime, Drama, Sci-Fi': 218,
 'Action, Comedy, Horror': 22,
 'Comedy, Mystery': 195,
 'Action, Horror, Sci-Fi': 57,
 'Adventure, Comedy, Sci-Fi': 80,
 'Horror, Mystery, Sci-Fi': 317,
 'Biography, Drama': 138,
 'Comedy, Music': 190,
 'Horror, Sci-Fi': 319,
 'Action, Drama': 37,
 'Action, Drama, Thriller': 47,
 'Adventure, Thriller': 107,
 'Adventure, Drama, Romance': 88,
 'Action, Adventure': 1,
 'Action, Crime, Horror': 32,
 'Action, Adventure, Romance': 11,
 'Action, Horror': 55,
 'Drama, Romance, Thriller': 286,
 'Biography, Comedy, Drama': 136,
 'Animation, Action, Drama': 113,
 'Animation, Comedy': 119,
 'Drama, War': 295,
 'Adventure, Drama, History': 85,
 'Action, Comedy, Drama': 19,
 'Action, Biography, Drama': 16,
 'Adventure, Drama, Family': 83,
 'Comedy, Horror, Thriller': 189,
 'Mystery, Thriller': 328,
 'Family, Fantasy': 297,
 'Adventure, Fantasy, Mystery': 96,
 'Comedy, Drama, Mystery': 165,
 'Fantasy, Horror, Thriller': 306,
 'Adventure, Drama, Mystery': 87,
 'Drama, Mystery, Romance': 279,
 'Short, Action, Thriller': 337,
 'Crime, Drama, Fantasy': 210,
 'Adventure, Biography, Crime': 68,
 'Drama, Fantasy, Sci-Fi': 256,
 'Adventure, Mystery, Sci-Fi': 103,
 'Comedy, Sci-Fi': 204,
 'Animation, Adventure, Family': 117,
 'Comedy, Drama, Fantasy': 160,
 'Drama, History': 261,
 'Crime, Drama, Musical': 215,
 'Action, Drama, Fantasy': 39,
 'Comedy, Drama, War': 170,
 'Drama, Thriller, War': 293,
 'Short, Mystery': 344,
 'Comedy, Crime, Mystery': 154,
 'Horror, Sci-Fi, Thriller': 320,
 'Adventure, Horror, Sci-Fi': 101,
 'Adventure, Horror, Mystery': 100,
 'Action, Adventure, Family': 6,
 'Comedy, Music, Romance': 192,
 'Drama, History, War': 264,
 'Drama, Romance, Sci-Fi': 284,
 'Action, Mystery, Thriller': 61,
 'Adventure, Comedy': 70,
 'Adventure, Fantasy': 94,
 'Adventure, Horror, Thriller': 102,
 'Crime, Drama, Horror': 213,
 'Adventure, Sci-Fi': 105,
 'Family, Sci-Fi': 302,
 'Drama, Fantasy, Thriller': 257,
 'Adventure, Biography, Drama': 69,
 'Comedy, Crime, Sport': 156,
 'Drama, Mystery, War': 282,
 'Animation, Comedy, Family': 120,
 'Documentary, Crime, Mystery': 240,
 'Adventure, Comedy, Drama': 72,
 'Comedy, Fantasy, Mystery': 181,
 'Animation, Adventure, Drama': 116,
 'Drama, Fantasy, War': 258,
 'Comedy, Drama, Music': 163,
 'Comedy, Mystery, Sci-Fi': 197,
 'Action, Fantasy, Sci-Fi': 53,
 'Musical, Romance': 323,
 'Comedy, Fantasy, Music': 180,
 'Drama, Music, Romance': 275,
 'Comedy, Family': 171,
 'Action, Comedy, Sci-Fi': 25,
 'Crime, Thriller': 235,
 'Crime, Horror': 224,
 'Action, Adventure, Western': 14,
 'Comedy, Romance, Sci-Fi': 201,
 'Mystery, Sci-Fi, Thriller': 327,
 'Drama, Film-Noir': 259,
 'Documentary, Reality-TV, Romance': 243,
 'Comedy, Crime, Romance': 155,
 'Comedy, Crime, Thriller': 157,
 'Adventure, Comedy, Fantasy': 74,
 'Adventure, Comedy, Romance': 79,
 'Adventure, Drama, Horror': 86,
 'Animation, Short, Adventure': 132,
 'Comedy, Horror, Mystery': 186,
 'Documentary, Comedy': 239,
 'Crime, Drama, Romance': 217,
 'Biography, Drama, Thriller': 145,
 'Comedy, Drama, Musical': 164,
 'Comedy, Sport': 205,
 'Drama, Mystery': 278,
 'Biography, Drama, Sport': 144,
 'Comedy, Musical': 193,
 'Adventure, Drama': 82,
 'Comedy, Fantasy, Romance': 182,
 'Documentary, Reality-TV': 242,
 'Action, Adventure, Mystery': 10,
 'Action, Fantasy, Thriller': 54,
 'Animation, Action, Comedy': 111,
 'Fantasy, Sci-Fi, Thriller': 309,
 'Animation, Short, Sci-Fi': 133,
 'Animation, Drama, Fantasy': 125,
 'Action, Drama, Family': 38,
 'Action, Drama, Sport': 46,
 'Game-Show, Reality-TV': 310,
 'Adventure, Drama, Thriller': 90,
 'Drama, Romance, War': 287,
 'Action, Comedy, War': 28,
 'Adventure, Comedy, Music': 76,
 'Family, Fantasy, Musical': 299,
 'Comedy, Horror, Sci-Fi': 188,
 'Comedy, Musical, Romance': 194,
 'Drama, Horror, Musical': 267,
 'Drama, Family, Fantasy': 247,
 'Sci-Fi, Thriller': 334,
 'Drama, History, Romance': 262,
 'Drama, Family': 246,
 'Action, Comedy, Mystery': 23,
 'Biography, Drama, Family': 139,
 'Action, Thriller, War': 66,
 'Action, Crime, Sci-Fi': 35,
 'Adventure, Horror': 99,
 'Action, Crime': 29,
 'Action, Fantasy, Horror': 51,
 'Adventure, Drama, Western': 92,
 'Fantasy': 303,
 'Crime, Horror, Western': 228,
 'Action, Adventure, History': 8,
 'Drama, Horror, Music': 266,
 'Animation, Adventure, Fantasy': 118,
 'Comedy, Horror, Romance': 187,
 'Action, Crime, Fantasy': 31,
 'Adventure, Fantasy, Romance': 97,
 'Talk-Show': 345,
 'Action, Adventure, Biography': 2,
 'Action, Biography, Crime': 15,
 'Action, Comedy, Thriller': 27,
 'Crime, Mystery, Sci-Fi': 231,
 'Comedy, Western': 207,
 'Mystery, Romance, Thriller': 326,
 'Animation, Short, Action': 131,
 'Drama, Horror, Western': 272,
 'Comedy, Drama, History': 161,
 'Comedy, Family, Horror': 173,
 'Comedy, Family, Romance': 175,
 'History, Sport': 313,
 'Action, Horror, War': 59,
 'Action, Drama, Western': 49,
 'Comedy, Crime, Fantasy': 151,
 'Action, Comedy': 17,
 'Animation, Drama, War': 128,
 'Documentary': 236,
 'Adventure, Crime, Drama': 81,
 'Action, Comedy, Family': 20,
 'Drama, Fantasy': 251,
 'Fantasy, Mystery, Sci-Fi': 308,
 'Adventure, Comedy, Reality-TV': 78,
 'Action, Drama, Romance': 44,
 'Action, Comedy, Romance': 24,
 'Crime, Fantasy, Horror': 222,
 'Fantasy, Mystery, Romance': 307,
 'Crime, Horror, Sci-Fi': 226,
 'Drama, Family, Romance': 250,
 'Family, Fantasy, Romance': 300,
 'Comedy, Romance, Sport': 202,
 'Drama, Film-Noir, Mystery': 260,
 'Crime, Drama, Music': 214,
 'Adventure, Fantasy, Sci-Fi': 98,
 'Animation, Drama': 123,
 'Comedy, Mystery, Thriller': 198,
 'Short, Family': 342,
 'Adventure, Mystery, Thriller': 104,
 'Animation': 109,
 'Short, Drama, Romance': 341,
 'Comedy, Family, Music': 174,
 'Comedy, Crime, Musical': 153,
 'Crime, Drama, Western': 221,
 'Documentary, Horror': 241,
 'Crime, Mystery': 229,
 'Adventure, Comedy, History': 75,
 'Drama, Family, Musical': 249,
 'Action, Comedy, Sport': 26,
 'Animation, Horror': 130,
 'Action, Fantasy': 50,
 'Short, Drama': 340,
 'Biography': 134,
 'Drama, Fantasy, History': 252,
 'Animation, Crime, Mystery': 122,
 'Short, Action': 335,
 'Documentary, Short, Action': 244,
 'Adventure, Comedy, Musical': 77,
 'Comedy, Family, Sport': 177,
 'Adventure, Thriller, Western': 108,
 'Documentary, Biography, Drama': 238,
 'Animation, Action, Crime': 112,
 'Reality-TV, Romance': 330,
 'Action, Western': 67,
 'Short, Adventure, Comedy': 338,
 'Game-Show, Reality-TV, Romance': 311,
 'Adventure, Fantasy, Horror': 95,
 'Action, Drama, Music': 42,
 'Reality-TV': 329,
 'Drama, Horror, Romance': 269,
 'Family, Musical, Romance': 301,
 'Action, Romance, Thriller': 62,
 'Documentary, Biography, Comedy': 237,
 'Animation, Drama, Music': 126,
 'Animation, Action, Horror': 114,
 'Crime, Mystery, Romance': 230,
 'Sci-Fi': 333,
 'Comedy, Crime, Horror': 152,
 'Comedy, War': 206,
 'Crime, Sci-Fi, Thriller': 234,
 'Music': 322,
 'Crime, Romance, Thriller': 233,
 'Animation, Comedy, Fantasy': 121,
 'Horror, Music, Thriller': 315,
 'Comedy, Crime, Family': 150,
 'Comedy, Romance, Musical': 200,
 'Comedy, Family, Sci-Fi': 176,
 'Action, Crime, Romance': 34,
 'Crime, Film-Noir, Mystery': 223,
 'Biography, Drama, War': 146,
 'Crime, Drama, Sport': 219,
 'Comedy, Music, Musical': 191,
 'Mystery, Romance': 324,
 'Drama, Music, Musical': 274,
 'Drama, Romance, Sport': 285,
 'Animation, Drama, Mystery': 127,
 'Comedy, Romance, Western': 203,
 'Short, Comedy': 339,
 'Short, Action, Sci-Fi': 336,
 'Romance, Sci-Fi, Thriller': 332,
 'Comedy, Horror, Music': 184,
 'History': 312,
 'Drama, Family, History': 248,
 'Crime, Drama, Film-Noir': 211}

types=['Film', 'Series']
nudity_lst=['Moderate', 'No Rate', 'Severe']
certificates=['Approved', 'E', 'G',
       'GP', 'M', 'M/PG',
       'NC-17', 'Not Rated', 'PG',
       'PG-13', 'Passed', 'R',
       'TV-14', 'TV-G', 'TV-MA',
       'TV-PG', 'TV-Y', 'TV-Y7',
       'Unrated', 'X']
profanity_lst=['Moderate', 'No Rate', 'Severe']
alcohol_lst=['Moderate', 'No Rate', 'Severe']
frightening_lst=['Moderate', 'No Rate', 'Severe']
violence_lst=['Moderate', 'No Rate', 'Severe']


# input data
votes = st.number_input("Votes", value=27145,step=5)
genre=st.selectbox('Select the Genre :',list(genres.keys()))
duration = st.number_input("Duration (in minutes)", value=90,step=1)
episodes = st.number_input("Episodes", value=1,step=1)
type_choice = st.selectbox("Type",types)
nudity = st.selectbox("Nudity Level",nudity_lst)
violence = st.selectbox("Violence Level",violence_lst)
profanity = st.selectbox("Profanity Level", profanity_lst)
alcohol = st.selectbox("Alcohol Usage Level", alcohol_lst)
frightening = st.selectbox("Frightening Scenes Level", frightening_lst)
certificate = st.selectbox("Certificate",certificates)


#input dictionary
input_data = {
    'Votes': votes,
    'Genre': genres[genre],
    'Duration': duration,
    'Episodes': episodes,
}

if type_choice == 'Series':
 input_data['Type_Series']=1
else:
 input_data['Type_Series']=0

for n in nudity_lst:
 if n == nudity:
  input_data[f'Nudity_{n}'] = 1
 else:
  input_data[f'Nudity_{n}'] = 0

for v in violence_lst:
 if v == violence:
  input_data[f'Violence_{v}'] = 1
 else:
  input_data[f'Violence_{v}'] = 0

for p in profanity_lst:
 if p == profanity:
  input_data[f'Profanity_{p}'] = 1
 else:
  input_data[f'Profanity_{p}'] = 0

for a in alcohol_lst:
 if a == alcohol:
  input_data[f'Alcohol_{a}'] = 1
 else:
  input_data[f'Alcohol_{a}'] = 0

for f in frightening_lst:
 if f == frightening:
  input_data[f'Frightening_{f}'] = 1
 else:
  input_data[f'Frightening_{f}'] = 0

for c in certificates:
 if c == certificate:
  input_data[f'Certificate_{c}'] = 1
 else:
  input_data[f'Certificate_{c}'] = 0

# Convert to DataFrame for prediction
input_df = pd.DataFrame([input_data])


# Predict final score
if st.button("Predict IMDB rating"):
    prediction = imdb.predict(input_df)
    st.success(f"The rating is : {prediction[0]:.2f}")