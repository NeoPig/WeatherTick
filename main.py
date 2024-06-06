import streamlit as st
import plotly.express as px
from backend import get_data  # Import custom function to get weather data
from logger import log_request # Import custom function to log requests

# Set the title of the Streamlit app
st.title("Weather Tick 🌡️")
place = st.text_input("Place ",
                      help= "Type in desired location ") # Create a help icon to display the features of this specific function

# Create a slider to select the number of forecast days in which the user can toggle up to 5 days ahead
days = st.slider("Forecast Days ", min_value = 1, max_value = 5,
                 help= "Select the number of days you would like to see the forecast for ")

# Create a select box to choose between viewing temperature or sky conditions
option = st.selectbox("Select data to view", ("Temperature", "Sky"),
                      help= " Select to view temperature or sky conditions ")

# Display a subheader with the chosen options
st.subheader(f"{option} for the next {days} days in {place}")


if place:

    try:
        # logs the request
        log_request(place, days, option)

        # Get temp or sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":

            # Extract temperature data and corresponding dates for plotting
            temperatures = [dict["main"]["temp"]/ 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            # Create a line plot for the temperature data
            figure = px.line(x= dates , y= temperatures, labels = {"x": "Dates", "y": "Temperature(C)"})
            st.plotly_chart(figure) # Display the plot in the Streamlit app

        # If the "Sky" option is selected, display corresponding weather images.
        if option == "Sky":
            # Dictionary mapping sky conditions to image file paths.
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}

            # Extracts main weather condition (e.g., "Clear", "Clouds") from the filtered data.
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]

            # Maps each sky condition to its corresponding image path.
            image_paths = [images[condition] for condition in sky_conditions]

            # Print sky conditions for debugging purposes.
            print(sky_conditions)
            # Display the images with a specified width of 115 pixels.
            st.image(image_paths, width=115)
    # Handles the case where a place doesn't exist in the weather data.
    except KeyError:

        # Display an error message.
        st.write(" THAT PLACE DOESN'T EXIST. TRY AGAIN")