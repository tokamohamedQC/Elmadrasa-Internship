import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_info = {
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
            }
            return weather_info
        else:
            messagebox.showerror("Error", f"Failed to fetch weather data: {data['message']}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def get_weather_button_clicked():
    city_name = city_entry.get()
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"

    if not api_key:
        messagebox.showerror("Error", "Please provide your OpenWeatherMap API key.")
        return

    if city_name:
        weather_info = get_weather(api_key, city_name)
        if weather_info:
            result_label.config(
                text=f"Temperature: {weather_info['temperature']}°C\nDescription: {weather_info['description']}"
            )
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

# GUI setup
app = tk.Tk()
app.title("Weather App")

city_label = tk.Label(app, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(app)
city_entry.pack(pady=10)

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather_button_clicked)
get_weather_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()
