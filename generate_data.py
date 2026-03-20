import pandas as pd
import numpy as np

# Number of days
n = 100

# Create date range
dates = pd.date_range(start="2024-01-01", periods=n)

# Generate realistic temperature (smooth variation)
temperature = 26 + 2 * np.sin(np.linspace(0, 3*np.pi, n)) + np.random.normal(0, 0.5, n)

# Generate wind speed (random but smooth)
wind = 10 + 8 * np.sin(np.linspace(0, 5*np.pi, n)) + np.random.normal(0, 2, n)

# Ensure wind is positive
wind = np.clip(wind, 2, None)

# Generate wave height based on wind (correlated)
wave = 0.1 * wind + np.random.normal(0, 0.3, n)

# Add occasional storm spikes
for i in range(0, n, 20):
    wave[i] += np.random.uniform(2, 4)
    wind[i] += np.random.uniform(10, 20)

# Ensure wave is positive
wave = np.clip(wave, 0.5, None)

# Create dataframe
data = pd.DataFrame({
    "Date": dates,
    "Temperature": np.round(temperature, 1),
    "WindSpeed": np.round(wind, 1),
    "WaveHeight": np.round(wave, 1)
})

# Save to CSV
data.to_csv("data/weather_data.csv", index=False)

print("Realistic dataset generated!")