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
def add_players_and_ball(ax, player_positions, ball_position):
    # Menambahkan 11 pemain biru
    for pos in player_positions['blue']:
        ax.scatter(pos[0], pos[1], c='blue', s=100)

    # Menambahkan 11 pemain merah
    for pos in player_positions['red']:
        ax.scatter(pos[0], pos[1], c='red', s=100)

    # Menambahkan bola
    ax.scatter(ball_position[0], ball_position[1], c='white', s=200, marker='o')

# Fungsi untuk menggerakkan objek
def move_object(initial_position, new_position):
    return (new_position[0], new_position[1])

# Menampilkan lapangan dan pemain di Streamlit
def display_field():
    st.title("NFL Field Simulation")

    # Inisialisasi posisi pemain dan bola
    if 'player_positions' not in st.session_state:
        st.session_state.player_positions = {
            'blue': [(random.uniform(0, 53.3), random.uniform(0, 100)) for _ in range(11)],
            'red': [(random.uniform(0, 53.3), random.uniform(0, 100)) for _ in range(11)]
        }
    
    if 'ball_position' not in st.session_state:
        st.session_state.ball_position = (random.uniform(0, 53.3), random.uniform(0, 100))

    # Memasukkan kontrol untuk gerakan pemain dan bola
    st.sidebar.header('Move Players or Ball')
    selected_object = st.sidebar.radio('Select Object', ['Blue Players', 'Red Players', 'Ball'])
    
    move_x = st.sidebar.slider('Move X position', 0.0, 53.3, st.session_state.ball_position[0] if selected_object == 'Ball' else st.session_state.player_positions['blue'][0][0])
    move_y = st.sidebar.slider('Move Y position', 0.0, 100.0, st.session_state.ball_position[1] if selected_object == 'Ball' else st.session_state.player_positions['blue'][0][1])

    # Update posisi objek
    if selected_object == 'Ball':
        st.session_state.ball_position = (move_x, move_y)
    elif selected_object == 'Blue Players':
        st.session_state.player_positions['blue'][0] = (move_x, move_y)
    elif selected_object == 'Red Players':
        st.session_state.player_positions['red'][0] = (move_x, move_y)

    # Membuat lapangan dan menambahkan objek
    fig, ax = create_nfl_field()
    add_players_and_ball(ax, st.session_state.player_positions, st.session_state.ball_position)

    ax.set_xlim(0, 53.3)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    st.pyplot(fig)

# Menampilkan aplikasi
if __name__ == "__main__":
    display_field()
