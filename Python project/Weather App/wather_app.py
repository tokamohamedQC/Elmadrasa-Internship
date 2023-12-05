import tkinter as tk
import requests

def search_weather():
    api_key = "11e424b5cb4636861cf1ef0006ad2dc9"
    city_name = txt_edit.get()
    if not city_name:
        print("Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    response = requests.get(url)

    status_code = response.status_code
    if status_code != 200:
        print(f"Sorry, server error: {response.text}")
        return

    result = response.json()
    
    temperature.config(text=f"Temperature: {result['main']['temp']}°C")
    humidity.config(text=f"Humidity: {result['main']['humidity']}%")
    pressure.config(text=f"Pressure: {result['main']['pressure']} hPa")
    wind_speed.config(text=f"Wind Speed: {result['wind']['speed']} m/s")
    precipitation.config(text=f"Precipitation: N/A")


window = tk.Tk()
window.title("Weather App")
window.rowconfigure(0, minsize=500)
window.columnconfigure(1, minsize=500)

location = tk.Label(window, text="Location: ")
location.grid(column=0, row=0, sticky="n")

txt_edit = tk.Entry(window)
txt_edit.grid(column=1, row=0, sticky="n")

frame_buttons = tk.Frame(window, relief=tk.RAISED)
search_button = tk.Button(frame_buttons, text="Search", command=search_weather)
search_button.grid(column=1, row=1, pady=10)

frame_buttons.grid(column=0, row=0, sticky="e")

temperature = tk.Label(window, text="Temperature: ")
temperature.grid(row=1, sticky="nw")

humidity = tk.Label(window, text="Humidity: ")
humidity.grid(row=2, sticky="nw")

pressure = tk.Label(window, text="Pressure: ")
pressure.grid(row=3, sticky="nw")

wind_speed = tk.Label(window, text="Wind Speed: ")
wind_speed.grid(row=4, sticky="nw")

precipitation = tk.Label(window, text="Precipitation: ")
precipitation.grid(row=5, sticky="nw")

window.mainloop()
