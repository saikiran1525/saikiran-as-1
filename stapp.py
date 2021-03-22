import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

user = st.text_input("User Name:")
file = st.file_uploader("File Upload: ",type=['csv'])

Button=st.button("Submit")

if (Button==True):
    df=pd.read_csv(file)
    st.write(df.head())
    fig = plt.figure()
    plt.scatter(df['PetalLengthCm'],df['SepalLengthCm'])
    plt.xlabel('petallength')
    plt.ylabel('sepallength')
    st.write(fig)
