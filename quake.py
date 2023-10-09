import plotly.express as px
import random

# Simulated seismic data (replace with real data)
num_earthquakes = 50
earthquake_locations = [(random.uniform(-180, 180), random.uniform(-90, 90), random.uniform(0, 500))
                        for _ in range(num_earthquakes)]
earthquake_magnitudes = [random.uniform(2.0, 6.0) for _ in range(num_earthquakes)]

# Create a DataFrame for Plotly
import pandas as pd
df = pd.DataFrame({
    'Longitude': [loc[0] for loc in earthquake_locations],
    'Latitude': [loc[1] for loc in earthquake_locations],
    'Depth (km)': [loc[2] for loc in earthquake_locations],
    'Magnitude': earthquake_magnitudes
})

# Create an interactive 3D scatter plot
fig = px.scatter_3d(df, x='Longitude', y='Latitude', z='Depth (km)', color='Magnitude',
                     color_continuous_scale='viridis', size_max=10, opacity=0.7,
                     title='Interactive 3D Lunar Earthquakes Visualization',
                     labels={'Longitude': 'Longitude', 'Latitude': 'Latitude', 'Depth (km)': 'Depth (km)'})
fig.update_layout(scene=dict(aspectmode="cube"))

# Show the interactive plot
fig.show()
