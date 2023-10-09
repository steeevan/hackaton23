import pandas as pd
import random
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


# Simulate real-time seismic data
def generate_seismic_data(num_entries):
    data = []
    for _ in range(num_entries):
        magnitude = round(random.uniform(2.0, 5.0), 2)  # Simulated earthquake magnitude
        latitude = round(random.uniform(-90, 90), 2)     # Simulated latitude on the Moon
        longitude = round(random.uniform(-180, 180), 2)  # Simulated longitude on the Moon
        duration = round(random.uniform(1.0, 10.0), 2)   # Simulated earthquake duration in seconds
        data.append([magnitude, latitude, longitude, duration])
    return data

# Process and organize seismic data using Pandas
def process_seismic_data(seismic_data):
    columns = ['Magnitude', 'Latitude', 'Longitude', 'Duration']
    df = pd.DataFrame(seismic_data, columns=columns)
    return df

def plot_magnitude(data):
    plt.figure(figsize=(8, 6))
    plt.hist(data['Magnitude'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Magnitude Distribution')
    plt.xlabel('Magnitude')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_latitude_longitude(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Longitude'], data['Latitude'], c=data['Magnitude'], cmap='viridis', s=data['Magnitude'] * 50, alpha=0.5)
    plt.title('Latitude vs Longitude (Color-coded by Magnitude)')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(label='Magnitude')
    plt.grid(True)
    plt.show()
def plot_seismic_data_3d(data):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extract data
    longitude = data['Longitude']
    latitude = data['Latitude']
    magnitude = data['Magnitude']
    
    # Create the 3D scatter plot
    ax.scatter(longitude, latitude, magnitude, c=magnitude, cmap='viridis', s=magnitude*50, alpha=0.7)
    
    # Set labels and title
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Magnitude')
    ax.set_title('3D Seismic Data Visualization')
    
    # Add a colorbar
    cbar = fig.colorbar(plt.cm.ScalarMappable(cmap='viridis'), ax=ax)
    cbar.set_label('Magnitude')
    
    plt.show()

def plot_seismic_data_sphere(data):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extract data
    longitude = np.radians(data['Longitude'])  # Convert longitude to radians
    latitude = np.radians(data['Latitude'])    # Convert latitude to radians
    magnitude = data['Magnitude']
    
    # Convert spherical coordinates to Cartesian coordinates
    x = magnitude * np.cos(latitude) * np.cos(longitude)
    y = magnitude * np.cos(latitude) * np.sin(longitude)
    z = magnitude * np.sin(latitude)
    
    # Create the 3D scatter plot
    ax.scatter(x, y, z, c=magnitude, cmap='viridis', s=magnitude*50, alpha=0.7)
    
    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Seismic Data Sphere Visualization')
    
    # Add a colorbar
    cbar = fig.colorbar(plt.cm.ScalarMappable(cmap='viridis'), ax=ax)
    cbar.set_label('Magnitude')
    
    plt.show()
# Matplotlib 3D Scatter Plot
def matplotlib_3d_plot(data):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(data['Longitude'], data['Latitude'], data['Magnitude'], c=data['Magnitude'], cmap='viridis', s=data['Magnitude']*50, alpha=0.7)
    
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Magnitude')
    ax.set_title('Matplotlib 3D Scatter Plot')
    
    plt.show()

# Plotly 3D Scatter Plot
def plotly_3d_plot(data):
    fig = px.scatter_3d(data, x='Longitude', y='Latitude', z='Magnitude', color='Magnitude', size='Magnitude', opacity=0.7)
    fig.update_layout(title='Plotly 3D Scatter Plot')
    fig.show()

# Mayavi 3D Scatter Plot
# Main function
def main():
    num_entries = 10  # Number of simulated seismic data entries
    seismic_data = generate_seismic_data(num_entries)
    processed_data = process_seismic_data(seismic_data)
      # Call the plotting functions
    matplotlib_3d_plot(processed_data)
    plotly_3d_plot(processed_data)
    print("Simulated Seismic Data:")
    print(processed_data)

if __name__ == "__main__":
    main()
