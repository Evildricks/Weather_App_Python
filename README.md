![img.png](img.png)

![](https://img.shields.io/badge/Open_Source-Project-orange)
![](https://img.shields.io/badge/Hacktoberfest_Contribution-2023-yellow)
[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)
[![OpenWeatherMap API](https://img.shields.io/badge/OpenWeatherMap-API-brightgreen)](https://openweathermap.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-0.90.1-red)](https://www.streamlit.io/)
---

# Weather Forecast App

![Copy of logo](https://github.com/HariNithyaRao/Weather_App_Python/assets/73685642/cc76db7c-fe68-45f0-b4c6-3380e10a5722)


A simple weather forecast app built for accessing the weather forecast of any city in the world.

---

## Table of Contents

- [Features](#features)
- [How It works](#how-it-works)
- [Have a look](#have-a-look)
- [Installation](#installation)


---

## Features :sparkles: 

- Real-time weather data
- Location-based weather forecasts
- Hourly and daily forecasts
- Multiple units of measurement (e.g., Celsius, Fahrenheit)
- Weather history and trends

---

## How It works 🛠️

This Weather Forecast app is built using Streamlit, Python, and the OpenWeatherMap API. It provides real-time weather data for user-specified cities.

1. **Enter City Name:** Users input the name of the city for which they want to check the weather forecast.

2. The app utilizes the Geopy library to geolocate the city and determine its latitude and longitude coordinates.

3. **Real-Time Data:** It then uses the OpenWeatherMap API to fetch the current weather conditions and 7-day weather forecast for that location.

4. The app displays the current temperature, humidity, pressure, wind speed, and weather description, along with an icon representing the weather condition.

5. **7-Day Forecast:** Users can also view a 7-day forecast, with icons, temperatures, and weather descriptions for each day.

6. **Interactive UI:** The app determines the local time and timezone of the selected city and displays it. Additionally, it displays the country in which the city is located.

This project serves as a simple and effective tool for obtaining weather information for various cities worldwide.


---
## Have a look 👀


https://github.com/HariNithyaRao/Weather_App_Python/assets/73685642/198d2e7f-9e92-422e-9ed0-761549ddd531


---
## Installation :inbox_tray:

Here's the step-by-step instructions on how to install the project:

```bash
# First, fork the repository to your account (using the button on the top-right corner)

# Clone the repository to your local machine
git clone https://github.com/your-username/your-repo.git

# Change directory to project folder
cd your-repo

# Install dependencies provided in requirements.txt
pip install -r requirements.txt

# Run the app
streamlit run main.py

# And there you have it! project will be running on http://localhost:8501 by default
```



