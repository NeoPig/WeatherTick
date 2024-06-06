import requests

# API key for authenticating requests to the OpenWeatherMap API.
API_KEY ="648f9cd58fb3aa43999675c4d8d1d407"

#fetches weather forecast data for a specified place and number of forecast days from the OpenWeatherMap API.

#Parameters:
        #place (str): The city for which to fetch weather data.
        #forecast_days (int, optional): The number of days to forecast.

#Returns:
       # list: Filtered weather data for the specified number of forecast days.
def get_data(place, forecast_days=None):

    # Constructs the API request URL using the specified place and API key.
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    # Sends a GET request to the API.
    response = requests.get(url)

    # Parses the JSON response from the API.
    data = response.json()

    # Extracts the weather forecast data from the response
    filtered_data = data["list"]

    # Calculates the number of values to keep based on the number of forecast days (assuming 8 values per day).
    nr_values = 8 * forecast_days

    # Trims the data to the desired number of forecast days.
    filtered_data = filtered_data[:nr_values]

    # Returns the filtered weather data.
    return filtered_data


# used to test if toggle option (slider) was working, and can be used if any errors occur later to fix get_data()
if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3 ))

