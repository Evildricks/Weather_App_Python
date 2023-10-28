#importing the necessary libraries
import streamlit as st
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import json
from streamlit_lottie import st_lottie

# Setting the page configuration ,wide mode
st.set_page_config(layout="wide")


with open("cities.txt", "r") as f:
    cities = f.read()
    cities = cities.split("\n")
    cities = tuple(cities)

# Heading and logo
col1, col2 = st.columns(2)
with col1:
    # container = st.container()
    st.title("Weather App", anchor="center")
with col2:
    st.image("Images/logo.png", width=120)


# Create a text input field for entering the city name from the selection box

city = st.selectbox("Select a city name:", cities)
if not city:
    st.warning("Please enter a city name.")
    st.stop()
if st.button("Get Weather"):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    country = location.address.split(",")[-1].strip()

    # Display the location and current time
    col1, col2, col3, col4 = st.columns(4)
    col1.header(home)
    col2.header(f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")
    col3.header(f"{current_time}")
    col4.header(f"{country}")

    # Initializing the API URL
    # Requesting the data from the API

    url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(location.latitude) + "&lon=" + str(
        location.longitude) + "&units=metric&exclude=hourly&appid=646824f2b7b86caffec1d0b16ea77f79"# Replace the API key with your own
    st.divider()

    try:
        json_data = requests.get(url).json()

        # Extract and display current weather data
        temp = json_data["current"]['temp']
        humidity = json_data['current']['humidity']
        pressure = json_data['current']['pressure']
        wind = json_data['current']['wind_speed']
        description = json_data['current']['weather'][0]['description']


        # Displaying the weather data in columns
        col1, col2, col3, col4, col5= st.columns(5)
        col1.metric("Temperature", f"{temp}°C")
        col2.metric("Wind Speed", f"{wind}m/s")
        col3.metric("Humidity", f"{humidity}%")
        col4.metric("Pressure", f"{pressure}hPa")
        col5.metric("Description", f"{description}")
        st.divider()

        # Storing the  7-day forecast data in variables and displaying them
        #DAY1 data
        day1_day_temp = json_data['daily'][0]['temp']['day']
        day1_night_temp = json_data['daily'][0]['temp']['night']
        day1_desc = json_data['daily'][0]['weather'][0]['description']
        day1_icon = json_data['daily'][0]['weather'][0]['icon']
        # day1_image = "icon/" + day1_icon + "@2x.png"
        day1_anime = "Animations/" + day1_icon + "@2x.json"

        #DAY2 data
        day2_day_temp = json_data['daily'][1]['temp']['day']
        day2_night_temp = json_data['daily'][1]['temp']['night']
        day2_desc = json_data['daily'][1]['weather'][0]['description']
        day2_icon = json_data['daily'][1]['weather'][0]['icon']
        # day2_image = "icon/" + day2_icon + "@2x.png"
        day2_anime = "Animations/" + day2_icon + "@2x.json"

        #DAY3 data
        day3_day_temp = json_data['daily'][2]['temp']['day']
        day3_night_temp = json_data['daily'][2]['temp']['night']
        day3_desc = json_data['daily'][2]['weather'][0]['description']
        day3_icon = json_data['daily'][2]['weather'][0]['icon']
        # day3_image = "icon/" + day3_icon + "@2x.png"
        day3_anime = "Animations/" + day3_icon + "@2x.json"

        #DAY4 data
        day4_day_temp = json_data['daily'][3]['temp']['day']
        day4_night_temp = json_data['daily'][3]['temp']['night']
        day4_desc = json_data['daily'][3]['weather'][0]['description']
        day4_icon = json_data['daily'][3]['weather'][0]['icon']
        # day4_image = "icon/" + day4_icon + "@2x.png"
        day4_anime = "Animations/" + day4_icon + "@2x.json"

        #DAY5 data
        day5_day_temp = json_data['daily'][4]['temp']['day']
        day5_night_temp = json_data['daily'][4]['temp']['night']
        day5_desc = json_data['daily'][4]['weather'][0]['description']
        day5_icon = json_data['daily'][4]['weather'][0]['icon']
        # day5_image = "icon/" + day5_icon + "@2x.png"
        day5_anime = "Animations/" + day5_icon + "@2x.json"

        #DAY6 data
        day6_day_temp = json_data['daily'][5]['temp']['day']
        day6_night_temp = json_data['daily'][5]['temp']['night']
        day6_desc = json_data['daily'][5]['weather'][0]['description']
        day6_icon = json_data['daily'][5]['weather'][0]['icon']
        # day6_image = "icon/" + day6_icon + "@2x.png"
        day6_anime = "Animations/" + day6_icon + "@2x.json"

        #DAY7 data
        day7_day_temp = json_data['daily'][6]['temp']['day']
        day7_night_temp = json_data['daily'][6]['temp']['night']
        day7_desc = json_data['daily'][6]['weather'][0]['description']
        day7_icon = json_data['daily'][6]['weather'][0]['icon']
        # day7_image = "icon/" + day7_icon + "@2x.png"
        day7_anime = "Animations/" + day7_icon + "@2x.json"


        #WEEK days data
        weekday1= datetime.fromtimestamp(json_data['daily'][0]['dt']).strftime('%A')
        weekday2 = datetime.fromtimestamp(json_data['daily'][1]['dt']).strftime('%A')
        weekday3 = datetime.fromtimestamp(json_data['daily'][2]['dt']).strftime('%A')
        weekday4 = datetime.fromtimestamp(json_data['daily'][3]['dt']).strftime('%A')
        weekday5 = datetime.fromtimestamp(json_data['daily'][4]['dt']).strftime('%A')
        weekday6 = datetime.fromtimestamp(json_data['daily'][5]['dt']).strftime('%A')
        weekday7 = datetime.fromtimestamp(json_data['daily'][6]['dt']).strftime('%A')

        # Displaying the 7-day forecast data in columns
        st.subheader(weekday1,anchor='center')
        col1, col2, col3,col4 = st.columns(4)
        # col1.image(day1_image)
        with col1:
            with open(day1_anime) as json_file:
                animation = json.load(json_file)
                st_lottie(animation, speed=1, height=100,width=100)
        col2.metric("Day Temperature", f"{day1_day_temp}°C")
        col3.metric("Night Temperature", f"{day1_night_temp}°C")
        col4.metric("Description", f"{day1_desc}")

        st.subheader(weekday2, anchor='center')
        col1, col2, col3, col4 = st.columns(4)
        # col1.image(day2_image)
        with col1:
            with open("Animations/" + day2_icon + "@2x.json") as f:
                day2_json = json.load(f)
            st_lottie(day2_json, speed=1, height=120,width=120)
        col2.metric("Day Temperature", f"{day2_day_temp}°C")
        col3.metric("Night Temperature", f"{day2_night_temp}°C")
        col4.metric("Description",f"{day2_desc}")

        st.subheader(weekday3, anchor='center')
        col1, col2, col3, col4 = st.columns(4)
        # col1.image(day3_image)
        with col1:
            with open("Animations/" + day3_icon + "@2x.json") as f:
                day3_json = json.load(f)
            st_lottie(day3_json, speed=1, height=120,width=120)
        col2.metric("Day Temperature", f"{day3_day_temp}°C")
        col3.metric("Night Temperature", f"{day3_night_temp}°C")
        col4.metric("Description",f"{day3_desc}")

        st.subheader(weekday4, anchor='center')
        col1, col2, col3, col4 = st.columns(4)
        # col1.image(day4_image)
        with col1:
            with open("Animations/" + day4_icon + "@2x.json") as f:
                day4_json = json.load(f)
            st_lottie(day4_json, speed=1, height=120,width=120)
        col2.metric("Day Temperature", f"{day4_day_temp}°C")
        col3.metric("Night Temperature", f"{day4_night_temp}°C")
        col4.metric("Description",f"{day4_desc}")

        st.subheader(weekday5, anchor='center')
        col1, col2, col3, col4 = st.columns(4)
        # col1.image(day5_image)
        with col1:
            with open("Animations/" + day5_icon + "@2x.json") as f:
                day5_json = json.load(f)
            st_lottie(day5_json, speed=1, height=120,width=120)
        col2.metric("Day Temperature", f"{day5_day_temp}°C")
        col3.metric("Night Temperature", f"{day5_night_temp}°C")
        col4.metric("Description",f"{day5_desc}")

        st.subheader(weekday6, anchor='center')
        col1, col2, col3, col4 = st.columns(4)
        # col1.image(day6_image)
        with col1:
            with open("Animations/" + day6_icon + "@2x.json") as f:
                day6_json = json.load(f)
            st_lottie(day6_json, speed=1, height=120,width=120)
        col2.metric("Day Temperature", f"{day6_day_temp}°C")
        col3.metric("Night Temperature", f"{day6_night_temp}°C")
        col4.metric("Description",f"{day6_desc}")

        st.subheader(weekday7, anchor='center')
        col1, col2, col3, col4 = st.columns(4)
        # col1.image(day7_image)
        with col1:
            with open("Animations/" + day7_icon + "@2x.json") as f:
                day7_json = json.load(f)
            st_lottie(day7_json, speed=1, height=120,width=120)
        col2.metric("Day Temperature", f"{day7_day_temp}°C")
        col3.metric("Night Temperature", f"{day7_night_temp}°C")
        col4.metric("Description",f"{day7_desc}")

    except Exception as e:
        st.error("An error occurred while fetching weather data.")
        st.error(str(e))

# To run the Streamlit app, use the following command in your terminal:
# streamlit run weather_app.py