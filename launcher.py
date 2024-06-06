import tkinter as tk
import subprocess

# Function to open the Weather App using subprocess to run the Streamlit script
def open_weather_app():
    # Use subprocess.Popen to launch the Weather App
    subprocess.Popen(["streamlit", "run", "main.py"])

# Function to read logs from a log file and display them in the Tkinter text widget

def read_logs():
    try:

        # Open the log file and read its contents
        with open("request_log.txt", "r") as file:
            logs = file.read()
            log_text.delete(1.0, tk.END)  # Clear existing text in the text widget
            log_text.insert(tk.END, logs) # Insert log data into the text widget
    except FileNotFoundError:

        # Handle case where log file does not exist
        log_text.delete(1.0, tk.END)  # Clear existing text
        log_text.insert(tk.END, "Log file not found.") # Inform the user that the log file is missing

# Create the main window
root = tk.Tk()
root.title("WeatherTick")

# Create a button to launch the weather app
launch_button = tk.Button(root, text="Launch WeatherTick ", command=open_weather_app)
launch_button.pack(pady=10)

# Create a button to display logs
log_button = tk.Button(root, text="View Logs", command=read_logs)
log_button.pack(pady=10) # Add padding around the button

# Create a text widget to display logs
log_text = tk.Text(root, wrap=tk.WORD)
log_text.pack(expand=True, fill=tk.BOTH) # Make the text widget expand and fill the available space

# Run the main event loop
root.mainloop()
