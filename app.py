import streamlit as st
import pandas as pd

# Ukuran lapangan dalam yard
field_width_yards = 53.3  # Lebar lapangan NFL dalam yard
field_length_yards = 100  # Panjang lapangan NFL dalam yard
field_width_px = 500  # Lebar lapangan dalam piksel (untuk tinggi)
field_length_px = 1000  # Panjang lapangan dalam piksel (untuk lebar)

# Faktor skala
x_scale = field_length_px / field_length_yards
y_scale = field_width_px / field_width_yards

# Function to save positions
def save_positions(positions):
    field_height_px = 500  # Height of the field in pixels
    field_width_px = 1000  # Width of the field in pixels

    # Convert positions from pixels to yards
    for p in positions:
        p['x_yard'] = round(p['x'] * (field_length_yards / field_length_px), 2)  # Convert x to yards
        p['y_yard'] = round((field_height_px - p['y']) * (field_width_yards / field_height_px), 2)  # Convert y to yards

    position_df = pd.DataFrame(positions)
    st.write("Posisi dalam yard disimpan (pusat kiri bawah):")
    st.write(position_df[['id', 'x_yard', 'y_yard']])

# Create interactive elements in Streamlit
st.title("Interactive NFL Field")

# Create widgets to simulate player and ball movement
field = st.empty()
with field:
    st.write("Move players and the ball!")

# Create placeholder for saving positions
save_button = st.button("Save Player Positions")

if save_button:
    # Simulate the positions of the players and ball
    positions = []
    for i in range(1, 12):
        positions.append({"id": f"blue{i}", "x": st.slider(f"Blue Player {i} X Position", 0, field_length_px, 100), "y": st.slider(f"Blue Player {i} Y Position", 0, field_width_px, 50)})
    for i in range(1, 12):
        positions.append({"id": f"red{i}", "x": st.slider(f"Red Player {i} X Position", 0, field_length_px, 100), "y": st.slider(f"Red Player {i} Y Position", 0, field_width_px, 400)})
    
    ball_position = {"id": "ball", "x": st.slider("Ball X Position", 0, field_length_px, 480), "y": st.slider("Ball Y Position", 0, field_width_px, 240)}
    
    positions.append(ball_position)
    
    # Save positions to the dataframe
    save_positions(positions)
