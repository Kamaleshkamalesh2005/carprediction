import pandas as pd
import numpy as np
import streamlit as st

# Load Dataset
cars_data = pd.read_csv('Cardetails (2).csv')

# Preprocessing
def get_brand_name(car_name):
    return car_name.split(' ')[0].strip()

cars_data['name'] = cars_data['name'].apply(get_brand_name)

# Streamlit UI
st.title('🚗 Car Price Prediction Web App')

# User Inputs
name = st.selectbox('Select Car Brand', cars_data['name'].unique())
year = st.slider('Car Manufactured Year', 1994, 2024)
km_driven = st.slider('No of kms Driven', 11, 200000)
fuel = st.selectbox('Fuel Type', cars_data['fuel'].unique())
seller_type = st.selectbox('Seller Type', cars_data['seller_type'].unique())
transmission = st.selectbox('Transmission Type', cars_data['transmission'].unique())
owner = st.selectbox('Owner Type', cars_data['owner'].unique())
mileage = st.slider('Car Mileage (km/l)', 10, 40)
engine = st.slider('Engine Capacity (CC)', 700, 5000)
max_power = st.slider('Max Power (bhp)', 0, 200)
seats = st.slider('Number of Seats', 2, 10)

# Simple Mock Prediction Logic
if st.button('Predict'):
    estimated_price = (2024 - year) * 1000 + (200000 - km_driven) * 0.05 + mileage * 100 + engine * 0.2
    st.success(f'💰 Estimated Car Price: ₹{round(estimated_price, 2)}')

