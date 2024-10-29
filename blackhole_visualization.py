# blackhole_visualization.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from PIL import Image, ImageEnhance
from astropy.constants import G, c, M_sun
from astropy import units as u

# Grid setup for visualization
GRID_SIZE = 1000
x = np.linspace(-10, 10, GRID_SIZE)
y = np.linspace(-10, 10, GRID_SIZE)
X, Y = np.meshgrid(x, y)

# Calculate distance from center
r = np.sqrt(X**2 + Y**2)

# Black hole parameters: mass and Schwarzschild radius
black_hole_mass = 4 * M_sun  # 4 solar masses
schwarzschild_radius = (2 * G * black_hole_mass / c**2).to(u.km).value

# Define the enhanced lensing effect function
def blackhole_lens_effect(r, rs, strength=1.5):
    """Calculate the lensing effect for a black hole of a given mass."""
    return strength / (r + rs)

# Apply gravitational lensing effect with Gaussian blur
lensing_effect = blackhole_lens_effect(r, schwarzschild_radius)
lensed_blur = gaussian_filter(lensing_effect, sigma=15)

# Plotting the visualization
plt.figure(figsize=(8, 8))
plt.imshow(lensed_blur, extent=[-10, 10, -10, 10], cmap='inferno')
plt.title("Enhanced Black Hole Visualization with Gravitational Lensing")
plt.xlabel("X (scaled units)")
plt.ylabel("Y (scaled units)")
plt.colorbar(label="Lensing Intensity")
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig("output/blackhole_lensing_enhanced.png", dpi=300)
plt.close()  # Close the plot to save memory

# Saving the image with enhanced contrast
img = Image.fromarray(np.uint8(lensed_blur * 255))
img = ImageEnhance.Contrast(img).enhance(2)
img.save("output/blackhole_lensing_enhanced.png")
