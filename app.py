import streamlit as st
import pandas as pd
import numpy as np
import time

# Parameters for field dimensions (NFL field)
field_width_yards = 53.3  # Width in yards
field_length_yards = 100  # Length in yards
field_width_px = 500  # Width in pixels
field_length_px = 1000  # Length in pixels

# Scale factors to convert pixel positions to yards
x_scale = field_length_px / field_length_yards
y_scale = field_width_px / field_width_yards

# Streamlit page configuration
st.set_page_config(page_title="Interactive NFL Field", layout="centered")

# Title and description
st.title("Interactive NFL Field")
st.write("Move the players and the ball on the field. Save positions in yards.")

# Container for the field (background image, interactive divs)
st.markdown("""
    <style>
    .field { position: relative; width: 1000px; height: 500px; background-color: #006400; border: 2px solid white; border-radius: 10px; margin-bottom: 10px; }
    .player { position: absolute; width: 30px; height: 30px; border-radius: 50%; cursor: pointer; display: flex; justify-content: center; align-items: center; }
    .blue { background-color: blue; }
    .red { background-color: red; }
    .ball { position: absolute; width: 20px; height: 20px; background-color: white; border-radius: 50%; cursor: pointer; }
    .yellow-line { position: absolute; width: 4px; background-color: yellow; height: 100%; cursor: pointer; }
    </style>
    """, unsafe_allow_html=True)

# Initialize positions for players and ball
players_blue = [{'id': f'blue{i}', 'x': 100 + (i * 30), 'y': 50} for i in range(1, 12)]
players_red = [{'id': f'red{i}', 'x': 100 + (i * 30), 'y': 400} for i in range(1, 12)]
ball = {'id': 'ball', 'x': 480, 'y': 240}

# Streamlit components to display interactive field
def update_positions():
    # Get updated positions of players and ball (use slider or text input in Streamlit to adjust positions)
    positions = []
    for player in players_blue + players_red:
        positions.append({
            'id': player['id'],
            'x': st.slider(f"{player['id']} X Position", 0, field_length_px, player['x'], key=f"{player['id']}_x"),
            'y': st.slider(f"{player['id']} Y Position", 0, field_width_px, player['y'], key=f"{player['id']}_y")
        })
    
    # Ball position
    ball['x'] = st.slider("Ball X Position", 0, field_length_px, ball['x'], key="ball_x")
    ball['y'] = st.slider("Ball Y Position", 0, field_width_px, ball['y'], key="ball_y")
    
    # Display the field
    st.markdown('<div class="field" id="field">', unsafe_allow_html=True)
    for player in positions:
        st.markdown(f'<div class="player {player["id"]}" style="left:{player["x"]}px; top:{player["y"]}px;"></div>', unsafe_allow_html=True)
    
    # Display the ball
    st.markdown(f'<div class="ball" style="left:{ball["x"]}px; top:{ball["y"]}px;"></div>', unsafe_allow_html=True)
    
    # Optionally save the positions in yards
    if st.button('Save Position'):
        positions_in_yards = []
        for p in positions:
            positions_in_yards.append({
                'id': p['id'],
                'x_yard': round(p['x'] * (field_length_yards / field_length_px), 2),
                'y_yard': round((field_width_px - p['y']) * (field_width_yards / field_width_px), 2)
            })
        ball_in_yards = {'id': ball['id'], 'x_yard': round(ball['x'] * (field_length_yards / field_length_px), 2),
                         'y_yard': round((field_width_px - ball['y']) * (field_width_yards / field_width_px), 2)}
        positions_in_yards.append(ball_in_yards)
        
        # Show the saved positions in yards
        st.write("Positions saved (in yards):")
        st.write(pd.DataFrame(positions_in_yards))

# Display the field and sliders for user input
update_positions()
