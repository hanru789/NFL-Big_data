import streamlit as st
import pandas as pd

# Setup for Streamlit
st.set_page_config(page_title="Interactive NFL Field", layout="wide")

# Function to save positions
def save_positions(positions):
    field_height_px = 500  # Height of the field in pixels
    field_width_px = 1000  # Width of the field in pixels

    for p in positions:
        # Convert X and Y positions to yards
        p['x_yard'] = round(p['x'] * (field_length_yards / field_length_px), 2)  # Convert x to yards
        p['y_yard'] = round((field_height_px - p['y']) * (field_width_yards / field_height_px), 2)  # Convert y to yards with center at the bottom left

    return pd.DataFrame(positions)

# Define field size
field_width_yards = 53.3  # Width of NFL field in yards
field_length_yards = 100  # Length of NFL field in yards
field_width_px = 500  # Width in pixels
field_length_px = 1000  # Length in pixels

# Create a placeholder for the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interactive NFL Field</title>
  <style>
    body { margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; background-color: #f4f4f4; }
    .field { position: relative; width: 1000px; height: 500px; background-color: #006400; border: 2px solid white; border-radius: 10px; margin-bottom: 10px; }
    button { padding: 10px 20px; font-size: 16px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer; }
    button:hover { background-color: #0056b3; }
    .player { position: absolute; width: 30px; height: 30px; border-radius: 50%; cursor: pointer; display: flex; justify-content: center; align-items: center; }
    .blue { background-color: blue; }
    .red { background-color: red; }
    .ball { position: absolute; width: 20px; height: 20px; background-color: white; border-radius: 50%; cursor: pointer; }
    .yellow-line { position: absolute; width: 4px; background-color: yellow; height: 100%; cursor: pointer; }
  </style>
</head>
<body>
  <div class="field" id="field">
    <div class="yard-line" style="left: 100px;"></div> <!-- 10-yard line -->
    <div class="yard-line" style="left: 200px;"></div> <!-- 20-yard line -->
    <div class="yard-line" style="left: 300px;"></div> <!-- 30-yard line -->
    <div class="yard-line" style="left: 400px;"></div> <!-- 40-yard line -->
    <div class="yard-line" style="left: 500px;"></div> <!-- 50-yard line -->

    <div class="player blue" id="blue1" style="left: 100px; top: 50px;"></div>
    <div class="player red" id="red1" style="left: 100px; top: 400px;"></div>

    <div class="ball" id="ball" style="left: 480px; top: 240px;"></div>
    <div class="yellow-line" id="yellowLine" style="left: 500px;"></div>
  </div>

  <script>
    const elements = [...document.querySelectorAll(".player"), document.getElementById("ball"), document.getElementById("yellowLine")];

    elements.forEach(el => {
      el.addEventListener("mousedown", (e) => {
        const offsetX = e.clientX - el.offsetLeft;
        const offsetY = e.clientY - el.offsetTop;
        const move = (moveEvent) => {
          el.style.left = `${moveEvent.clientX - offsetX}px`;
          el.style.top = `${moveEvent.clientY - offsetY}px`;
        };
        const stop = () => {
          document.removeEventListener("mousemove", move);
          document.removeEventListener("mouseup", stop);
        };
        document.addEventListener("mousemove", move);
        document.addEventListener("mouseup", stop);
      });
    });

    // Function to save positions (for demo, simply log the positions)
    document.getElementById("savePosition").addEventListener("click", () => {
      const positions = elements.map(el => ({
        id: el.id,
        x: parseInt(el.style.left, 10),
        y: parseInt(el.style.top, 10)
      }));
      console.log(positions);
    });
  </script>
</body>
</html>
"""

# Display the HTML content using Streamlit's components
st.components.v1.html(html_content, height=600)

# Add a button to save the positions (you can call the save_positions function here)
if st.button('Save Player Positions'):
    st.write("Player positions have been saved!") # Process to save coordinates in the backend
