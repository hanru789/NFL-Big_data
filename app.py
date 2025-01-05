import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

# Fungsi untuk membuat lapangan NFL
def create_nfl_field():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Membuat lapangan NFL (dalam orientasi horizontal)
    field = patches.Rectangle((0, 0), 100, 53.3, linewidth=1, edgecolor='green', facecolor='lightgreen')
    ax.add_patch(field)

    # Membuat garis-garis lapangan
    for i in range(1, 11):
        ax.plot([i * 10, i * 10], [0, 53.3], color='white', lw=1)

    # Menambahkan garis gawang
    ax.plot([0, 0], [0, 53.3], color='white', lw=2)
    ax.plot([100, 100], [0, 53.3], color='white', lw=2)

    # Menambahkan nama-nama area
    ax.text(2, 26.65, 'End Zone', fontsize=12, ha='center', color='white', weight='bold')
    ax.text(98, 26.65, 'End Zone', fontsize=12, ha='center', color='white', weight='bold')

    return fig, ax

# Fungsi untuk menambahkan pemain dan bola
def add_players_and_ball(ax, blue_players, red_players, ball_position):
    # Menambahkan 11 pemain biru
    for player in blue_players:
        ax.scatter(player[1], player[0], c='blue', s=100, label="Blue Team")

    # Menambahkan 11 pemain merah
    for player in red_players:
        ax.scatter(player[1], player[0], c='red', s=100, label="Red Team")

    # Menambahkan bola
    ax.scatter(ball_position[1], ball_position[0], c='white', s=200, marker='o', label="Ball")

# Menampilkan lapangan dan pemain di Streamlit
def display_field():
    st.title("NFL Field Simulation")

    # Inisialisasi posisi pemain dan bola
    blue_players = [(random.uniform(0, 53.3), random.uniform(0, 100)) for _ in range(11)]
    red_players = [(random.uniform(0, 53.3), random.uniform(0, 100)) for _ in range(11)]
    ball_position = (random.uniform(0, 53.3), random.uniform(0, 100))

    # Membuat dua kolom untuk input Blue Team dan Red Team
    col1, col2 = st.columns(2)

    # Input posisi untuk Blue Team di kolom pertama
    with col1:
        st.header("Blue Team")
        blue_players_input = []
        for i in range(11):
            x_pos = st.number_input(f"Player {i+1} X Position (Blue Team)", min_value=0.0, max_value=100.0, value=blue_players[i][1], step=0.1)
            y_pos = st.number_input(f"Player {i+1} Y Position (Blue Team)", min_value=0.0, max_value=53.3, value=blue_players[i][0], step=0.1)
            blue_players_input.append((y_pos, x_pos))

    # Input posisi untuk Red Team di kolom kedua
    with col2:
        st.header("Red Team")
        red_players_input = []
        for i in range(11):
            x_pos = st.number_input(f"Player {i+1} X Position (Red Team)", min_value=0.0, max_value=100.0, value=red_players[i][1], step=0.1)
            y_pos = st.number_input(f"Player {i+1} Y Position (Red Team)", min_value=0.0, max_value=53.3, value=red_players[i][0], step=0.1)
            red_players_input.append((y_pos, x_pos))

    # Menampilkan lapangan dan pemain di Streamlit
    fig, ax = create_nfl_field()
    add_players_and_ball(ax, blue_players_input, red_players_input, ball_position)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 53.3)
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    st.pyplot(fig)

# Menampilkan aplikasi
if __name__ == "__main__":
    display_field()
