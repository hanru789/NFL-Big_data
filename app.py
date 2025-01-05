import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

# Fungsi untuk membuat lapangan NFL
def create_nfl_field():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Membuat lapangan NFL
    field = patches.Rectangle((0, 0), 53.3, 100, linewidth=1, edgecolor='green', facecolor='lightgreen')
    ax.add_patch(field)

    # Membuat garis-garis lapangan
    for i in range(1, 11):
        ax.plot([0, 53.3], [i * 10, i * 10], color='white', lw=1)

    # Menambahkan garis gawang
    ax.plot([0, 0], [0, 100], color='white', lw=2)
    ax.plot([53.3, 53.3], [0, 100], color='white', lw=2)

    # Menambahkan nama-nama area
    ax.text(26.65, 2, 'End Zone', fontsize=12, ha='center', color='white', weight='bold')
    ax.text(26.65, 98, 'End Zone', fontsize=12, ha='center', color='white', weight='bold')

    return fig, ax

# Fungsi untuk menambahkan pemain dan bola
def add_players_and_ball(ax, blue_players, red_players, ball_position):
    # Menambahkan 11 pemain biru
    for player in blue_players:
        ax.scatter(player[0], player[1], c='blue', s=100, label="Blue Team")

    # Menambahkan 11 pemain merah
    for player in red_players:
        ax.scatter(player[0], player[1], c='red', s=100, label="Red Team")

    # Menambahkan bola
    ax.scatter(ball_position[0], ball_position[1], c='white', s=200, marker='o', label="Ball")

# Menampilkan lapangan dan pemain di Streamlit
def display_field():
    st.title("NFL Field Simulation")

    # Inisialisasi posisi pemain dan bola
    blue_players = [(random.uniform(0, 53.3), random.uniform(0, 100)) for _ in range(11)]
    red_players = [(random.uniform(0, 53.3), random.uniform(0, 100)) for _ in range(11)]
    ball_position = (random.uniform(0, 53.3), random.uniform(0, 100))

    # Pilih tim dan pemain yang ingin digerakkan
    team_choice = st.selectbox("Choose the team", ["Blue Team", "Red Team"])
    player_choice = st.slider("Choose a player number to move (1-11)", 1, 11)

    if team_choice == "Blue Team":
        selected_player = blue_players[player_choice - 1]
    else:
        selected_player = red_players[player_choice - 1]

    # Input posisi baru untuk pemain yang dipilih
    new_x = st.slider("Move X position", 0, 53, int(selected_player[0]))
    new_y = st.slider("Move Y position", 0, 100, int(selected_player[1]))

    # Update posisi pemain yang dipilih
    if team_choice == "Blue Team":
        blue_players[player_choice - 1] = (new_x, new_y)
    else:
        red_players[player_choice - 1] = (new_x, new_y)

    # Menampilkan lapangan dan pemain di Streamlit
    fig, ax = create_nfl_field()
    add_players_and_ball(ax, blue_players, red_players, ball_position)

    ax.set_xlim(0, 53.3)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    st.pyplot(fig)

# Menampilkan aplikasi
if __name__ == "__main__":
    display_field()
