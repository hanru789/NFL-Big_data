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
def add_players_and_ball(ax):
    # Menambahkan 11 pemain biru
    for i in range(11):
        ax.scatter(random.uniform(0, 53.3), random.uniform(0, 100), c='blue', s=100, label="Blue Team" if i == 0 else "")

    # Menambahkan 11 pemain merah
    for i in range(11):
        ax.scatter(random.uniform(0, 53.3), random.uniform(0, 100), c='red', s=100, label="Red Team" if i == 0 else "")

    # Menambahkan bola
    ax.scatter(random.uniform(0, 53.3), random.uniform(0, 100), c='white', s=200, marker='o', label="Ball")

# Menampilkan lapangan dan pemain di Streamlit
def display_field():
    st.title("NFL Field Simulation")

    fig, ax = create_nfl_field()
    add_players_and_ball(ax)

    ax.set_xlim(0, 53.3)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    st.pyplot(fig)

# Menampilkan aplikasi
if __name__ == "__main__":
    display_field()
