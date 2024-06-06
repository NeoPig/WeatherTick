

#    Logs weather data requests to a text file.

  #  Parameters:

  #  place (str): The city for which the request was made.
  #  days (int): The number of forecast days requested.
  # option (str): The option selected (e.g., "Sky").


def log_request(place, days, option):

    # Opens the request_log.txt file in append mode.
    with open('request_log.txt', 'a') as file:

        # Writes a log entry to the file with the place, days, and option.
        file.write(f"Place: {place}, Days: {days}, Option: {option}\n")
