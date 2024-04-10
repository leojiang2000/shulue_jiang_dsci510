import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv('car_data.csv')

# Setting up the sidebar
st.sidebar.header('Filter Options')

# Car name text input
car_name = st.sidebar.text_input('Car Name')

# Transmission type multiselect
transmission_type = st.sidebar.multiselect('Transmission Type', ['Manual', 'Automatic'], default=['Manual', 'Automatic'])

# Selling price slider
selling_price_range = st.sidebar.slider('Selling Price Range', min_value=0, max_value=20, value=(0, 20))

# Year range slider
year_range = st.sidebar.slider('Year Range', min_value=2000, max_value=2024, value=(2000, 2024))

# Submit button
if st.sidebar.button('Submit'):
    # Filtering data based on the selections
    filtered_data = data.copy()
    
    if car_name:
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(car_name, case=False, na=False)]
    
    if transmission_type:
        filtered_data = filtered_data[filtered_data['Transmission'].isin(transmission_type)]
    
    filtered_data = filtered_data[(filtered_data['Selling_Price'] >= selling_price_range[0]) & 
                                  (filtered_data['Selling_Price'] <= selling_price_range[1])]
    
    filtered_data = filtered_data[(filtered_data['Year'] >= year_range[0]) & 
                                  (filtered_data['Year'] <= year_range[1])]
    
    # Displaying the filtered data
    st.dataframe(filtered_data)
else:
    # Displaying the original data
    st.dataframe(data)
