# World Weather Forecast App

## Overview

The **World Weather Forecast App** is a GUI application that provides weather forecasts for cities worldwide. It retrieves real-time weather data from the OpenWeatherMap API, displaying key information including temperature, humidity, rain forecast, and a weather emoji based on the current conditions. 

The application uses **Tkinter** to build a user-friendly interface and **requests** to fetch data from the OpenWeatherMap API.

---

## Features

- **City Input**: Users can input the name of any city to get its weather forecast.
- **Weather Forecast**: Displays the weather forecast for the next 7 days, including:
  - Temperature (both Celsius and Fahrenheit)
  - Humidity
  - Rain forecast (in mm for the next 3 hours)
  - Weather description with an emoji
- **Weather Emojis**: Emojis are used alongside weather descriptions to enhance the user experience.
- **Scrollable Forecast**: The forecast for multiple days is displayed in a scrollable window.

---

## Requirements

- **Python**: Version 3.x or higher
- **Libraries**:
  - `requests`: To fetch weather data from OpenWeatherMap.
  - `tkinter`: For building the GUI.
  - `Pillow` (optional): For image handling (although not actively used in the code).

To install the required libraries, run the following commands:

```bash
pip install requests
pip install pillow
