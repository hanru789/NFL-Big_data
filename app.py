import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Ukuran lapangan dalam yard
field_width_yards = 53.3  # Lebar lapangan NFL dalam yard
field_length_yards = 100  # Panjang lapangan NFL dalam yard
field_width_px = 500  # Lebar lapangan dalam piksel (untuk tinggi)
field_length_px = 1000  # Panjang lapangan dalam piksel (untuk lebar)

# Faktor skala
x_scale = field_length_px / field_length_yards
y_scale = field_width_px / field_width_yards

# Fungsi untuk konversi posisi piksel ke yard
def pixel_to_yard(x_px, y_px):
    x_yard = round(x_px * (field_length_yards / field_length_px), 2)
    y_yard = round((field_width_px - y_px) * (field_width_yards / field_width_px), 2)
    return x_yard, y_yard

# Menampilkan lapangan NFL sebagai latar belakang
st.title("Interaktif Lapangan NFL")

# Slider untuk memilih posisi pemain atau bola
x_pos = st.slider("Posisi X (yard)", 0, field_length_yards, 50)
y_pos = st.slider("Posisi Y (yard)", 0, field_width_yards, 26.65)  # Tengah lapangan

# Convert posisi dari yard ke piksel
x_px = x_pos * (field_length_px / field_length_yards)
y_px = (field_width_yards - y_pos) * (field_width_px / field_width_yards)

# Visualisasi lapangan NFL
st.write("Lapangan NFL")

# Gambar latar belakang lapangan (menggunakan gambar sederhana untuk representasi lapangan)
# Misalnya menggunakan plot dengan Altair
field = alt.Chart(pd.DataFrame({
    'x': [0, field_length_yards, field_length_yards, 0],
    'y': [0, 0, field_width_yards, field_width_yards]
})).mark_area(
    color='green', opacity=0.6
).encode(
    x='x:Q',
    y='y:Q'
)

# Pemain atau bola yang dapat dipindahkan
player = alt.Chart(pd.DataFrame({
    'x': [x_pos],
    'y': [y_pos],
    'color': ['blue']
})).mark_point(
    size=100, shape='circle'
).encode(
    x='x:Q',
    y='y:Q',
    color='color:N'
)

# Tampilkan lapangan dan pemain
st.altair_chart(field + player, use_container_width=True)

# Menyimpan posisi
if st.button("Simpan Posisi"):
    x_yard, y_yard = pixel_to_yard(x_px, y_px)
    st.write(f"Posisi pemain/bola disimpan pada {x_yard} yard dan {y_yard} yard.")

