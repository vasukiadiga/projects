import tkinter as tk
from tkinter import messagebox
import requests

# OpenWeatherMap API Key
API_KEY = "9bd1bfc7648800090cc081a4c8aca0f8"

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == "404":
            messagebox.showerror("Error", "City not found. Please enter a valid city.")
        else:
            weather_info = f"Weather in {city}:\n" \
                           f"Temperature: {data['main']['temp']}°C\n" \
                           f"Description: {data['weather'][0]['description']}"
            messagebox.showinfo("Weather Information", weather_info)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def get_weather_command():
    city = entry.get()
    if city:
        get_weather(city)
    else:
        messagebox.showwarning("Warning", "Please enter a city.")

# GUI setup
root = tk.Tk()
root.geometry("800x500")
root.title("Weather App")

label = tk.Label(root, text="ENTER CITY:",font=('Arial',20,'bold'))
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Get Weather",font=('Arial',18), command=get_weather_command)
button.pack(pady=10)

root.mainloop()
