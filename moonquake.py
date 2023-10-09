import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.decomposition import PCA

# Simulated moonquake data (Replace with your actual data)
moonquake_data = np.array([
    [10.0, 20.0, 10.0, 3.5],
    [-5.0, 15.0, 15.0, 4.2],
    [0.0, 30.0, 8.0, 3.0],
    [-15.0, 10.0, 12.0, 4.5],
    [5.0, -5.0, 7.0, 3.2],
    [25.0, 5.0, 9.0, 3.8],
    [-10.0, -15.0, 11.0, 4.0],
])

# Separate features and labels
features = moonquake_data[:, :-1]
labels = moonquake_data[:, -1]

# Apply Principal Component Analysis (PCA) for dimensionality reduction
pca = PCA(n_components=3)
reduced_features = pca.fit_transform(features)

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(reduced_features[:, 0], reduced_features[:, 1], reduced_features[:, 2], c=labels, cmap='viridis', s=labels * 100, alpha=0.7)

# Customize the plot
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
ax.set_title('Moonquake Data Visualization using PCA (Magnitude as Color and Size)')
cbar = fig.colorbar(sc, ax=ax, label='Magnitude')

# Show the plot
plt.show()
