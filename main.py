import streamlit as st

st.title("Weather Tick")
place = st.text_input("place: ")
days = st.slider("Forecast Days ", min_value = 1, max_value = 5,
                 help= "Select the number of days you would like to see the forecast for")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")