import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np

# Ukuran lapangan NFL (dalam pixel)
FIELD_WIDTH = 533  # Setara dengan 53.3 yard
FIELD_HEIGHT = 1000  # Setara dengan 100 yard

# Fungsi untuk menggambar lapangan NFL
def draw_field(canvas):
    # Menambahkan background warna lapangan
    canvas.create_rectangle(0, 0, FIELD_WIDTH, FIELD_HEIGHT, fill="lightgreen")

    # Membuat garis-garis lapangan
    for i in range(10, 101, 10):
        canvas.create_line(0, i * (FIELD_HEIGHT // 100), FIELD_WIDTH, i * (FIELD_HEIGHT // 100), fill="white", width=2)

    # Menambahkan garis gawang
    canvas.create_line(0, 0, 0, FIELD_HEIGHT, fill="white", width=2)
    canvas.create_line(FIELD_WIDTH, 0, FIELD_WIDTH, FIELD_HEIGHT, fill="white", width=2)

    # Zona akhir
    canvas.create_text(FIELD_WIDTH // 2, 15, text="End Zone", fill="white", font=("Arial", 12, "bold"))
    canvas.create_text(FIELD_WIDTH // 2, FIELD_HEIGHT - 15, text="End Zone", fill="white", font=("Arial", 12, "bold"))

# Fungsi untuk menambahkan pemain dan bola
def add_players_and_ball(canvas, players_positions, ball_position):
    # Menambahkan pemain biru
    for (x, y) in players_positions['blue']:
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="blue")

    # Menambahkan pemain merah
    for (x, y) in players_positions['red']:
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="red")

    # Menambahkan bola
    bx, by = ball_position
    canvas.create_oval(bx-10, by-10, bx+10, by+10, fill="white")


# Fungsi utama untuk menangani logika aplikasi
def display_field():
    st.title("NFL Field Simulation with Draggable Players and Ball")

    # Setup canvas
    canvas = st_canvas(
        fill_color="lightgreen",  # Warna lapangan
        stroke_width=2,
        width=FIELD_WIDTH,
        height=FIELD_HEIGHT,
        drawing_mode="freedraw",  # Membuat objek bisa digambar
        key="canvas",
        display_toolbar=False,
    )

    # Posisi awal pemain dan bola
    initial_positions = {
        'blue': [(100, 100), (150, 100), (200, 100), (250, 100), (300, 100), (350, 100), (400, 100), (450, 100), (500, 100), (550, 100), (600, 100)],
        'red': [(100, 900), (150, 900), (200, 900), (250, 900), (300, 900), (350, 900), (400, 900), (450, 900), (500, 900), (550, 900), (600, 900)],
    }
    ball_position = (FIELD_WIDTH // 2, FIELD_HEIGHT // 2)

    # Gambar lapangan NFL
    draw_field(canvas)

    # Gambar pemain dan bola
    add_players_and_ball(canvas, initial_positions, ball_position)

# Menampilkan aplikasi
if __name__ == "__main__":
    display_field()
