# weather_dashboard
## Overview

The Weather Dashboard is a web application that allows users to check current weather conditions and retrieve 5-day weather forecasts for cities around the world. Users can also manage their favorite cities for quick access.

## Features

- Current weather data display.
- 5-day weather forecast display.
- User authentication (registration and login).
- User-friendly interface with Bootstrap styling.
- Adding and removing favorite cities.
- Responsive design for mobile and desktop.

## Technologies Used

- **Django**: Backend web framework for Python.
- **Bootstrap**: Frontend framework for responsive styling.
- **jQuery**: JavaScript library for DOM manipulation and AJAX interactions.
- **OpenWeatherMap API**: Used to fetch weather data and forecasts.
- **HTML5** and **CSS3**: For structuring and styling the web page.
- **JavaScript**: For adding interactivity and handling user actions.

## Usage

1. **Clone the Repository**

git clone https://github.com/ecemyigit/weather-dashboard.git
cd weather-dashboard

2. **Install Dependencies**

pip install -r requirements.txt


3. **Run the Application**

python manage.py runserver


The application will be accessible at `http://localhost:8000` by default.

4. **Register and Login**

- Register for a new account or log in with your credentials.
- Once logged in, you can add favorite cities, retrieve weather information, and manage your favorites.

5. **Retrieve Weather Data**

- Enter a city name in the input field and click "Get Weather" to retrieve current weather information.
- Click "Get 5-Day Forecast" to retrieve a 5-day weather forecast for the specified city.

6. **Manage Favorite Cities**

- Enter a city name in the "Enter city to favorite" field and click "Add to Favorites" to add it to your favorites list.
- Click on a favorite city to retrieve its weather data.
- Click "Remove" next to a favorite city to remove it from your favorites list.


## Credits

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/).
- Bootstrap CSS framework: [Bootstrap](https://getbootstrap.com/).



- Built as a learning project for web development with Django, Bootstrap, and jQuery.
