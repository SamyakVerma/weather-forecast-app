import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter.font import Font
from PIL import Image, ImageTk
import io
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Constants
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Utility Functions
def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

def get_weather_emoji(description):
    desc = description.lower()
    if "rain" in desc:
        return "\U0001F327"
    elif "cloud" in desc:
        return "\u2601"
    elif "clear" in desc:
        return "\u2600"
    elif "snow" in desc:
        return "\u2744"
    elif "storm" in desc or "thunder" in desc:
        return "\u26C8"
    return "\U0001F324"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception:
        return None

def show_forecast():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    data = get_weather(city)
    if not data:
        messagebox.showerror("Error", "Could not retrieve weather data. Check your city name or internet connection.")
        return

    forecast_text.config(state='normal')
    forecast_text.delete('1.0', tk.END)

    forecast_text.insert(tk.END, f"\U0001F4CD Weather Forecast: {data['city']['name']}, {data['city']['country']}\n")
    forecast_text.insert(tk.END, "=" * 70 + "\n\n")

    shown_dates = set()
    for entry in data['list']:
        date_time = datetime.fromtimestamp(entry['dt'])
        date_key = date_time.date()

        if date_key not in shown_dates and len(shown_dates) < 7:
            shown_dates.add(date_key)

            temp_c = entry['main']['temp']
            temp_f = celsius_to_fahrenheit(temp_c)
            humidity = entry['main']['humidity']
            description = entry['weather'][0]['description'].capitalize()
            rain = entry.get('rain', {}).get('3h', 0)
            emoji = get_weather_emoji(description)

            forecast_text.insert(tk.END, f"\U0001F4C5 {date_time.strftime('%A, %d %B %Y')}\n", 'header')
            forecast_text.insert(tk.END, f"{emoji} {description}\n", 'desc')
            forecast_text.insert(tk.END, f"\U0001F321 Temperature: {temp_c}°C / {temp_f}°F\n")
            forecast_text.insert(tk.END, f"\U0001F4A7 Humidity: {humidity}%\n")
            forecast_text.insert(tk.END, f"\U0001F327 Rain (next 3h): {rain} mm\n")
            forecast_text.insert(tk.END, "-" * 70 + "\n\n")

    forecast_text.config(state='disabled')

# GUI Setup
root = tk.Tk()
root.title("\U0001F30D World Weather Forecast")
root.geometry("720x700")
root.configure(bg='#e6f2ff')
root.resizable(False, False)

font_header = Font(family="Helvetica", size=18, weight="bold")
font_label = Font(family="Arial", size=12)

# Title
title_label = tk.Label(root, text="\U0001F324 World Weather Forecast App", font=font_header, fg="#003366", bg='#e6f2ff')
title_label.pack(pady=20)

# City Input Frame
frame = tk.Frame(root, bg='#e6f2ff')
frame.pack(pady=10)

city_label = tk.Label(frame, text="\U0001F3D9 Enter City:", font=font_label, bg='#e6f2ff')
city_label.pack(side=tk.LEFT, padx=5)

city_entry = tk.Entry(frame, font=font_label, width=30)
city_entry.pack(side=tk.LEFT)

get_btn = tk.Button(root, text="Get Forecast", font=font_label, command=show_forecast, bg="#007ACC", fg="white", padx=10, pady=5)
get_btn.pack(pady=10)

# Forecast Display Frame
forecast_frame = tk.Frame(root, bg='#e6f2ff')
forecast_frame.pack(padx=15, pady=10, fill='both', expand=True)

forecast_text = scrolledtext.ScrolledText(forecast_frame, font=("Consolas", 11), width=85, height=25, wrap=tk.WORD, bg='white')
forecast_text.pack(padx=10, pady=10, fill='both', expand=True)
forecast_text.tag_config('header', foreground="#004080", font=("Helvetica", 12, "bold"))
forecast_text.tag_config('desc', font=("Arial", 11, "italic"))
forecast_text.config(state='disabled')

# Start GUI
root.mainloop()
