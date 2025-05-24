const apiKey = '9df4541ba098f112d0acb8dbf904cce0'; // Replace with your OpenWeatherMap API key

document.getElementById('searchButton').addEventListener('click', getWeather);

function getWeather() {
  const city = document.getElementById('locationInput').value.trim();
  if (!city) return;

  fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
    .then(response => {
      if (!response.ok) throw new Error('City not found');
      return response.json();
    })
    .then(data => {
      document.getElementById('location').textContent = `${data.name}, ${data.sys.country}`;
      document.getElementById('temperature').textContent = `Temperature: ${data.main.temp}°C`;
      document.getElementById('description').textContent = `Weather: ${data.weather[0].description}`;
    })
    .catch(() => {
      document.getElementById('location').textContent = '';
      document.getElementById('temperature').textContent = '';
      document.getElementById('description').textContent = 'City not found. Please try again.';
    });
}

document.addEventListener("DOMContentLoaded", function() {
  const rain = document.querySelector('.rain');
  for (let i = 0; i < 60; i++) {
    const drop = document.createElement('div');
    drop.className = 'rain-drop';
    drop.style.left = Math.random() * 100 + 'vw';
    drop.style.animationDuration = (0.7 + Math.random() * 0.6) + 's';
    drop.style.animationDelay = (Math.random() * 2) + 's';
    rain.appendChild(drop);
  }
});
