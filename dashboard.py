import streamlit as st
from datetime import datetime

def set_font_style():
    """Apply custom font style using CSS."""
    st.markdown(
        """
        <style>
        * {
            font-family: 'Courier', monospace;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_banner():
    """Display the title, author banner, and date."""
    st.title("Enhanced Black Hole Visualization with Gravitational Lensing")
    st.subheader("This Simulation made by Jegr and Hawkar")
    st.write(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def get_user_inputs():
    """Display sliders for user input and return the parameters."""
    black_hole_mass = st.slider("Black Hole Mass (in Solar Masses)", min_value=1.0, max_value=10.0, value=4.0, step=0.5)
    grid_size = st.slider("Grid Size", min_value=500, max_value=1500, value=1000, step=100)
    strength = st.slider("Lensing Strength", min_value=0.5, max_value=3.0, value=1.5, step=0.1)
    blur_sigma = st.slider("Gaussian Blur Sigma", min_value=5, max_value=30, value=15, step=1)
    return black_hole_mass, grid_size, strength, blur_sigma
