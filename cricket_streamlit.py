import streamlit as st
import pickle
import pandas as pd

with open("C:/Users/HP/Downloads/cricket.pkl","rb") as file:
    cricket = pickle.load(file)

# def add_background_image(image_url):
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background: url("{image_url}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# Add your image URL here
# image_url = "https://img.freepik.com/premium-photo/poster-cricket-game-called-game_1167368-215.jpg?semt=ais_hybrid"
# add_background_image(image_url)


st.title('Cricket Score Prediction Model')

# Input fields for user data
st.header("Enter Match Details")

# Dropdowns for batting and bowling teams
teams = [
    'Australia', 'Bangladesh', 'England', 'India', 'Ireland',
    'Netherlands', 'New Zealand', 'Pakistan', 'South Africa',
    'Sri Lanka', 'West Indies', 'Zimbabwe'
]
batting_team = st.selectbox("Select the batting team", teams)
bowling_team = st.selectbox("Select the bowling team", teams)

# Dropdown for city
cities={'Dubai': 36,
 'Hambantota': 45,
 'St Lucia': 90,
 'Bengaluru': 9,
 'Colombo': 27,
 'London': 63,
 'Lauderhill': 61,
 'Dublin': 37,
 'Edinburgh': 40,
 'Pallekele': 76,
 'Jamaica': 51,
 'Cardiff': 19,
 'Sydney': 92,
 'Christchurch': 26,
 'Lahore': 60,
 'Mirpur': 67,
 'Delhi': 31,
 'Bristol': 15,
 'Al Amarat': 3,
 'Harare': 47,
 'Nelson': 73,
 'Thiruvananthapuram': 96,
 'Ahmedabad': 2,
 'Belfast': 8,
 'Cuttack': 29,
 'Birmingham': 10,
 'Durban': 39,
 'Sharjah': 86,
 'Cape Town': 18,
 'Hobart': 48,
 'Johannesburg': 52,
 'Nagpur': 70,
 'Auckland': 5,
 'Southampton': 87,
 'St Kitts': 89,
 'Centurion': 21,
 'Abu Dhabi': 0,
 'Hamilton': 46,
 'Barbados': 6,
 'The Hague': 95,
 'Chattogram': 23,
 'Sylhet': 93,
 'Brisbane': 14,
 'Adelaide': 1,
 'Lucknow': 64,
 'Melbourne': 66,
 'Wellington': 100,
 'Manchester': 65,
 'Dhaka': 33,
 'Pune': 81,
 'Bulawayo': 16,
 'Kolkata': 59,
 'Bready': 12,
 'Rajkot': 82,
 'Chandigarh': 22,
 'Antigua': 4,
 'Chennai': 24,
 'Nottingham': 74,
 'Mumbai': 69,
 'Gros Islet': 42,
 'Indore': 50,
 'Trinidad': 97,
 'Port Elizabeth': 78,
 'Paarl': 75,
 'Dharamsala': 34,
 'Kandy': 53,
 'Chester-le-Street': 25,
 "St George's": 88,
 'Rawalpindi': 84,
 'Dehradun': 30,
 'Napier': 72,
 'St Vincent': 91,
 'Perth': 77,
 'Nairobi': 71,
 'Khulna': 56,
 'Dominica': 35,
 'Bridgetown': 13,
 'Basseterre': 7,
 'King City': 58,
 'Guyana': 44,
 'Mount Maunganui': 68,
 'Greater Noida': 41,
 'Potchefstroom': 79,
 'Karachi': 55,
 'Coolidge': 28,
 'Providence': 80,
 'Kimberley': 57,
 'Bloemfontein': 11,
 'Taunton': 94,
 'Victoria': 98,
 'Hyderabad': 49,
 'Rotterdam': 85,
 'Leeds': 62,
 'Dunedin': 38,
 'Visakhapatnam': 99,
 'Ranchi': 83,
 'Canberra': 17,
 'Kanpur': 54,
 'Guwahati': 43,
 'Derry': 32,
 'Carrara': 20}
city = st.selectbox("Select the city", list(cities.keys()))  # Ensure the city dropdown uses keys

# Numerical Inputs
power_play = st.selectbox("Is it PowerPlay? (0 = No, 1 = Yes)", [0, 1])
average_score = st.number_input("Enter average score for the venue", value=150, step=1)
deliveries_left = st.number_input("Enter deliveries left", value=60, step=1)
current_score = st.number_input("Enter current score", value=100, step=1)
current_run_rate = st.number_input("Enter current run rate", value=8.5, step=0.1)
wickets_left = st.number_input("Enter wickets left", value=5, step=1)
run_in_last5 = st.number_input("Enter runs scored in the last 5 overs", value=50, step=1)
wickets_in_last5 = st.slider("Wickets lost in the last 5 overs", min_value=0, max_value=10, value=2)
innings = st.selectbox("Select innings", [1, 2])

# Initialize input dictionary with all columns set to 0
input_data = {
    'powerPlay': power_play,
    'AverageScore': average_score,
    'city': cities[city],
    'delivery_left': deliveries_left,
    'score': current_score,
    'CurrentRunRate': current_run_rate,
    'wicketsLeft': wickets_left,
    'Run_In_Last5': run_in_last5,
    'Wickets_In_Last5': wickets_in_last5,
    'innings': innings,
}
# for batting team
for team in teams:
 if team == batting_team:
  input_data[f'battingTeam_{team}']=1
 else:
  input_data[f'battingTeam_{team}']=0

#for bowling team
for team in teams:
 if team == bowling_team:
  input_data[f'bowlingTeam_{team}']=1
 else:
  input_data[f'bowlingTeam_{team}']=0

# Convert to DataFrame for prediction
input_df = pd.DataFrame([input_data])

# Predict final score
if st.button("Predict Final Score"):
    prediction = cricket.predict(input_df)
    st.success(f"The predicted final score is: {prediction[0]:.2f}")
