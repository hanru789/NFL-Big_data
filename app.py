import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Define the field dimensions (in pixels)
field_width_yards = 53.3  # Width of the NFL field in yards
field_length_yards = 100  # Length of the NFL field in yards
field_width_px = 500  # Width of the field in pixels
field_length_px = 1000  # Length of the field in pixels

# Scale factors for converting between yards and pixels
x_scale = field_length_px / field_length_yards
y_scale = field_width_px / field_width_yards

# Function to save positions and convert from pixels to yards
def save_positions(positions):
    field_height_px = 500  # Height of the field in pixels
    field_width_px = 1000  # Width of the field in pixels

    # Convert positions from pixels to yards
    for p in positions:
        p['x_yard'] = round(p['x'] * (field_length_yards / field_length_px), 2)  # Convert x to yards
        p['y_yard'] = round((field_height_px - p['y']) * (field_width_yards / field_height_px), 2)  # Convert y to yards

    position_df = pd.DataFrame(positions)
    st.write("Positions (in yards):")
    st.write(position_df[['id', 'x_yard', 'y_yard']])

# Create the NFL field interface in Streamlit
st.title("Interactive NFL Field")

# Create a canvas for the field (background)
fig, ax = plt.subplots(figsize=(field_length_px / 100, field_width_px / 100))  # Size in inches
ax.set_xlim(0, field_length_px)
ax.set_ylim(0, field_width_px)
ax.set_facecolor("#006400")  # Green background for the field

# Draw the field lines (yard lines and center)
for i in range(10, 110, 10):
    ax.axvline(x=i * x_scale, color="white", linestyle="--", linewidth=1)

# Draw the end zones (optional)
ax.fill_betweenx([0, field_width_px], 0, 10 * x_scale, color="blue", alpha=0.1)
ax.fill_betweenx([0, field_width_px], 90 * x_scale, field_length_px, color="red", alpha=0.1)

# Draw the midfield line
ax.axvline(x=50 * x_scale, color="white", linewidth=2)

# Display the players and ball (as circles)
players_blue = []
players_red = []
ball = []

# Create interactive sliders for each player
positions = []
for i in range(1, 12):
    blue_x = st.slider(f"Blue Player {i} X Position", 0, field_length_px, 100)
    blue_y = st.slider(f"Blue Player {i} Y Position", 0, field_width_px, 50)
    red_x = st.slider(f"Red Player {i} X Position", 0, field_length_px, 100)
    red_y = st.slider(f"Red Player {i} Y Position", 0, field_width_px, 400)
    
    # Create blue player
    ax.plot(blue_x, blue_y, 'bo', markersize=10)
    # Create red player
    ax.plot(red_x, red_y, 'ro', markersize=10)
    
    # Store the positions of the players
    positions.append({"id": f"blue{i}", "x": blue_x, "y": blue_y})
    positions.append({"id": f"red{i}", "x": red_x, "y": red_y})

# Create the ball
ball_x = st.slider("Ball X Position", 0, field_length_px, 480)
ball_y = st.slider("Ball Y Position", 0, field_width_px, 240)
ax.plot(ball_x, ball_y, 'wo', markersize=15)  # White ball

# Create the yellow vertical line
yellow_line_x = st.slider("Yellow Line X Position", 0, field_length_px, 500)
ax.plot([yellow_line_x, yellow_line_x], [0, field_width_px], 'y-', linewidth=4)  # Yellow line

# Save button to record positions
if st.button("Save Player Positions"):
    save_positions(positions)

# Display the field
st.pyplot(fig)
