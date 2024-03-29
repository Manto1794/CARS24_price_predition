import streamlit as st
import pandas as pd
import pickle
import datetime

st.header('Car Price Prediction App')

# df = pd.read_csv('cars24-car-price.csv')
# st.dataframe(df)

# Inputs from user

col1, col2, col3 = st.columns(3)

with col1:
    today = datetime.datetime.now()
    today = today.year
    year_input = st.number_input('Enter the Manufactured Year of Car', 
                                 value=None, step=1, min_value=1950, max_value=today, placeholder='Year')
with col2:
    fuel_type_input = st.selectbox("Enter the Fuel Type: ", ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'))
with col3:
    transmission_type_input = st.selectbox("Enter the Transmission Type: ", ('Manual', 'Automatic'))

col1, col2, col3 = st.columns(3)

with col1:
    engine_input = st.slider('Provide the Engine power: ', min_value=500, max_value=5000, step=100)
with col2:
    seats_input = st.slider('Provide the seating Capacity: ', max_value=11, min_value=4, step=1)
with col3:
    seller_type_input = st.selectbox('Provide the Seller Type: ', ('Dealer', 'Individual', 'Trustmark Dealer'))

km_driven_input = st.slider('Provide the approx Kilometers driven: ', max_value=500000, min_value=10000, step=100)

encoding_dict = {
    "fuel_type":{"Diesel":1, "Petrol":2, "CNG": 3, "LPG":4, "Electric":5},
    "seller_type":{"Dealer":1, "Individual":2, "Trustmark Dealer": 3},
    "transmission_type":{"Manual":1, "Automatic":2}
}

def model_pred(year_input, seller_type_encoded, km_driven_input, fuel_type_encoded, transmission_type_encoded, engine_input, seats_input):
    with open("car_pred_ModelFile", "rb") as file:
        model = pickle.load(file)

        #Features are:
        #year, seller_type, km_driven, fuel_type, transmission_type, mileage, engine, max_power, seats

        input_feature = [[year_input, seller_type_encoded, km_driven_input, fuel_type_encoded, transmission_type_encoded, 19.7, engine_input, 46.3, seats_input]]
        return model.predict(input_feature)


if st.button('Predict'):

    fuel_type_encoded = encoding_dict['fuel_type'][fuel_type_input]
    transmission_type_encoded = encoding_dict['transmission_type'][transmission_type_input]
    seller_type_encoded = encoding_dict['seller_type'][seller_type_input]

    second_hand_price = model_pred(year_input, seller_type_encoded, km_driven_input, fuel_type_encoded, transmission_type_encoded, engine_input, seats_input)

    st.write('Predicted Price is: ', str(second_hand_price), 'Lakhs')