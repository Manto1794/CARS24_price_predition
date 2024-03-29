import streamlit as st
import pandas as pd
import pickle

st.header('Car Price Prediction App')
st.write('This is car prediction')
df = pd.read_csv('cars24-car-price.csv')

# st.dataframe(df)

# Inputs from user

year = st.number_input('Enter the Manufactured Year of Car')
fuel_type = st.selectbox("Enter the Fuel Type: ", ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'))
transmission = st.selectbox("Enter the Transmission Type: ", ('Manual', 'Automatic'))
engine = st.slider('Provide the Engine power: ', min_value=500, max_value=5000, step=100)
seats = st.slider('Provide the seating Capacity: ', max_value=11, min_value=2, step=1)


encoding_dict = {
    "fuel_type":{"Diesel":1, "Petrol":2, "CNG": 3, "LPG":4, "Electric":5},
    # "seller_type":{"Dealer":1, "Individual":2, "Trustmark Dealer": 3},
    "transmission_type":{"Manual":1, "Automatic":2}
}

def model_pred():
    with open("car_pred_ModelFile", "rb") as file:
        pickle.load(file)

        #Features are:
        #year, seller_type, km_driven, fuel_type, transmission_type, mileage, engine, max_power, seats

        input_feature = [2014, 2, 130000, Petrol, Manual, 19.7, 796, 46.3, 5]
