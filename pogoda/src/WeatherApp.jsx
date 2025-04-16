import React, { useState } from 'react';

const WeatherApp = () => {
    const [city, setCity] = useState('');
    const [weather, setWeather] = useState(null);

    const fetchWeather = async () => {
        const apiKey = 'your_api_key_here'; // Replace with your OpenWeatherMap API key
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${city},PL&appid=${apiKey}&units=metric`;

        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error('City not found');
            }
            const data = await response.json();
            setWeather(data);
        } catch (error) {
            alert(error.message);
        }
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Weather App</h1>
            <input
                type="text"
                placeholder="Enter city name"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                style={{ padding: '10px', fontSize: '16px' }}
            />
            <button onClick={fetchWeather} style={{ padding: '10px', fontSize: '16px', marginLeft: '10px' }}>
                Get Weather
            </button>

            {weather && (
                <div style={{ marginTop: '20px' }}>
                    <h2>{weather.name}</h2>
                    <p>Temperature: {weather.main.temp}°C</p>
                    <p>Weather: {weather.weather[0].description}</p>
                </div>
            )}
        </div>
    );
};

export default WeatherApp;