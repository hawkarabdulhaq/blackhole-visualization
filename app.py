import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from PIL import Image, ImageEnhance
from astropy.constants import G, c, M_sun
from astropy import units as u
from dashboard import set_font_style, display_banner, get_user_inputs

# Apply font style
set_font_style()

# Rest of the code for visualization...

# Display the banner and get user input from sliders
display_banner()
black_hole_mass, grid_size, strength, blur_sigma = get_user_inputs()

# Set up grid and parameters
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

# Save and display the image
plt.savefig("output/blackhole_lensing_enhanced.png", dpi=300)
plt.close()

img = Image.open("output/blackhole_lensing_enhanced.png")
img = ImageEnhance.Contrast(img).enhance(2)
st.image(img, caption="Black Hole Visualization", use_column_width=True)
