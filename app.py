import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from PIL import Image, ImageEnhance
from astropy.constants import G, c, M_sun
from astropy import units as u

# Streamlit app settings
st.title("Enhanced Black Hole Visualization with Gravitational Lensing")
st.write("Adjust the parameters to visualize the black hole lensing effect.")

# User-adjustable parameters
black_hole_mass = st.slider("Black Hole Mass (in Solar Masses)", min_value=1.0, max_value=10.0, value=4.0, step=0.5)
grid_size = st.slider("Grid Size", min_value=500, max_value=1500, value=1000, step=100)
strength = st.slider("Lensing Strength", min_value=0.5, max_value=3.0, value=1.5, step=0.1)
blur_sigma = st.slider("Gaussian Blur Sigma", min_value=5, max_value=30, value=15, step=1)

# Grid setup for visualization
x = np.linspace(-10, 10, grid_size)
y = np.linspace(-10, 10, grid_size)
X, Y = np.meshgrid(x, y)
r = np.sqrt(X**2 + Y**2)

# Black hole parameters
mass = black_hole_mass * M_sun  # Black hole mass in Solar masses
schwarzschild_radius = (2 * G * mass / c**2).to(u.km).value

# Define lensing effect
def blackhole_lens_effect(r, rs, strength):
    return strength / (r + rs)

# Apply lensing and Gaussian blur
lensing_effect = blackhole_lens_effect(r, schwarzschild_radius, strength)
lensed_blur = gaussian_filter(lensing_effect, sigma=blur_sigma)

# Visualization
plt.figure(figsize=(8, 8))
plt.imshow(lensed_blur, extent=[-10, 10, -10, 10], cmap='inferno')
plt.title("Enhanced Black Hole Visualization")
plt.xlabel("X (scaled units)")
plt.ylabel("Y (scaled units)")
plt.colorbar(label="Lensing Intensity")
plt.gca().set_aspect('equal', adjustable='box')

# Save the plot to a buffer and display
plt.savefig("output/blackhole_lensing_enhanced.png", dpi=300)
plt.close()

# Load and enhance the image for better contrast
img = Image.open("output/blackhole_lensing_enhanced.png")
img = ImageEnhance.Contrast(img).enhance(2)
st.image(img, caption="Black Hole Visualization", use_column_width=True)
