import streamlit as st
import pandas as pd

data = pd.read_csv('day.csv')

data.drop_duplicates(inplace=True)

numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
for feature in numerical_features:
    data[feature].fillna(data[feature].mean(), inplace=True)

categorical_features = data.select_dtypes(include=['object']).columns
for feature in categorical_features:
    data[feature].fillna(data[feature].mode()[0], inplace=True)

st.title('Streamlit Dashboard - Submission Dicoding')

st.sidebar.header('Options')
option = st.sidebar.selectbox('Select an Option', ('Show Data', 'Show Visualization'))

if option == 'Show Data':
    st.subheader('Raw Data')
    st.write(data)

elif option == 'Show Visualization':
    st.subheader('Data Visualization')

    column_to_visualize = st.selectbox('Select a Column for Visualization', data.columns)
    if data[column_to_visualize].dtype == 'int64' or data[column_to_visualize].dtype == 'float64':
        st.write(f'Visualization of {column_to_visualize}')
        st.bar_chart(data[column_to_visualize])

st.sidebar.write("Created by Nabil Mufti")
