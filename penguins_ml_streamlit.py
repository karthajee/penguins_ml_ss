import streamlit as st
import seaborn as sns
import pickle
from sklearn.ensemble import RandomForestClassifier

with open('random_forest_penguin.pickle', 'rb') as f:
    rfc = pickle.load(f)
with open('output_penguin.pickle', 'rb') as f:
    uniques = pickle.load(f)

# Add some information to the app
st.title('Palmer\'s Penguins app')
st.header('Demonstrating Streamlit Sharing')

# Add password checking
password_check = st.text_input('Enter the password:')
if password_check != 'password':
    st.stop()

# Get user input for the features!
island = st.selectbox('Penguin Island:', options=['Biscoe', 'Dream', 'Torgerson'])
sex = st.selectbox('Penguin Sex:', options=['Female', 'Male'])
bill_length = st.number_input('Bill Length in mm', min_value=0)
bill_depth = st.number_input('Bill Depth in mm', min_value=0)
flipper_length = st.number_input('Flipper Length in mm', min_value=0)
body_mass = st.number_input('Body mass in g', min_value=0)

# Display
st.write(f'User inputs are\n:{[island, sex, bill_length, bill_depth, flipper_length, body_mass]}')

# Get user inputs
island_biscoe, island_dream, island_torgerson = 0, 0, 0
if island == "Biscoe":
    island_biscoe = 1
elif island == "Dream":
    island_dream = 1
elif island == "Torgerson":
    island_torgerson = 1

sex_female, sex_male = 0, 0
if sex == "Female":
    sex_female = 1
elif sex == "Male":
    sex_male = 1

new_prediction = rfc.predict(
    [
        [
            bill_length,
            bill_depth,
            flipper_length,
            body_mass,
            island_biscoe,
            island_dream,
            island_torgerson,
            sex_female,
            sex_male,
        ]
    ]
)
st.subheader("Predicting Your Penguin's Species:")
prediction_species = uniques[new_prediction][0]
st.write(f"We predict your penguin is of the {prediction_species} species")

st.write(
    """We used a machine learning
    (Random Forest) model to predict the
    species, the features used in this
    prediction are ranked by relative
    importance below."""
)
st.image("feature_importance.png")