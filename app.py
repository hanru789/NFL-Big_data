import streamlit as st
import pandas as pd

# Definisikan ukuran lapangan NFL dalam yard
field_width_yards = 53.3  # Lebar lapangan NFL dalam yard
field_length_yards = 100  # Panjang lapangan NFL dalam yard

# Tampilan lapangan
st.title("Lapangan NFL Interaktif")

# Posisi Pemain dan Bola
x_pos = st.number_input(
    "Posisi X (yard)", 
    min_value=0.0, 
    max_value=float(field_length_yards), 
    value=50.0, 
    step=0.1
)  # Tengah lapangan

y_pos = st.number_input(
    "Posisi Y (yard)", 
    min_value=0.0, 
    max_value=float(field_width_yards), 
    value=26.65, 
    step=0.1
)  # Tengah lapangan

# Konversi posisi dari yard ke piksel
x_scale = 1000 / field_length_yards
y_scale = 500 / field_width_yards

x_px = x_pos * x_scale
y_px = (field_width_yards - y_pos) * y_scale  # Pusat lapangan ada di bagian bawah

# Tampilkan posisi pemain dan bola
st.write(f"Posisi Pemain: X = {x_pos} yard, Y = {y_pos} yard")
st.write(f"Posisi Pemain dalam piksel: X = {x_px} px, Y = {y_px} px")

# Gambar lapangan NFL
st.write("Lapangan NFL (Ukuran 100x53.3 yard)")

# Tampilkan posisi pemain dalam lapangan (sebagai marker)
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))

# Gambar lapangan (garis besar)
ax.plot([0, field_length_yards], [0, 0], color='white')  # Garis bawah
ax.plot([0, field_length_yards], [field_width_yards, field_width_yards], color='white')  # Garis atas
ax.plot([0, 0], [0, field_width_yards], color='white')  # Garis kiri
ax.plot([field_length_yards, field_length_yards], [0, field_width_yards], color='white')  # Garis kanan

# Garis yard
for i in range(10, 101, 10):
    ax.plot([i, i], [0, field_width_yards], color='white', linestyle='--')
    ax.text(i, field_width_yards + 1, str(i), color='white', fontsize=12, ha='center')

# Gambar pemain dan bola
ax.scatter(x_pos, y_pos, color='blue', s=100, label="Pemain", zorder=5)  # Pemain
ax.scatter(x_pos, y_pos, color='red', s=100, label="Bola", zorder=5)  # Bola
ax.text(x_pos, y_pos + 1, 'Pemain 1', color='white', ha='center', fontsize=10)

# Set batas dan layout
ax.set_xlim(0, field_length_yards)
ax.set_ylim(0, field_width_yards)
ax.set_facecolor('#006400')  # Warna lapangan NFL
ax.set_xticks(range(0, 101, 10))
ax.set_yticks(range(0, 54, 10))

# Hapus label sumbu
ax.set_xticklabels([])
ax.set_yticklabels([])

# Judul dan tampilan
ax.set_title("Lapangan NFL - Posisi Pemain dan Bola", color='white')

# Tampilkan gambar
st.pyplot(fig)

# Menyimpan posisi dalam DataFrame untuk penggunaan lebih lanjut
positions = pd.DataFrame({
    'Pemain': ['Pemain 1'],
    'Posisi X (yard)': [x_pos],
    'Posisi Y (yard)': [y_pos],
    'Posisi X (px)': [x_px],
    'Posisi Y (px)': [y_px]
})

st.write(positions)
