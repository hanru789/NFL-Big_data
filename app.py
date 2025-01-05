import streamlit as st
import plotly.graph_objects as go
import random

# Fungsi untuk membuat lapangan NFL
def create_nfl_field():
    fig = go.Figure()

    # Menambahkan lapangan NFL
    fig.add_shape(type="rect", x0=0, y0=0, x1=100, y1=53.3,
                  line=dict(color="green", width=2), fillcolor="lightgreen")

    # Membuat garis-garis lapangan
    for i in range(1, 11):
        fig.add_shape(type="line", x0=i * 10, y0=0, x1=i * 10, y1=53.3,
                      line=dict(color="white", width=1))

    # Menambahkan garis gawang
    fig.add_shape(type="line", x0=0, y0=0, x1=0, y1=53.3, line=dict(color="white", width=2))
    fig.add_shape(type="line", x0=100, y0=0, x1=100, y1=53.3, line=dict(color="white", width=2))

    # Menambahkan label "End Zone"
    fig.add_annotation(x=2, y=26.65, text="End Zone", showarrow=False, font=dict(size=12, color="white"), align="center")
    fig.add_annotation(x=98, y=26.65, text="End Zone", showarrow=False, font=dict(size=12, color="white"), align="center")

    return fig

# Fungsi untuk menambahkan pemain dan bola
def add_players_and_ball(fig, blue_players, red_players, ball_position):
    # Menambahkan 11 pemain biru dengan nomor
    for idx, player in enumerate(blue_players):
        fig.add_trace(go.Scatter(x=[player[1]], y=[player[0]], mode="markers+text", text=[str(idx+1)],
                                 marker=dict(color="blue", size=15), textposition="middle center"))

    # Menambahkan 11 pemain merah dengan nomor
    for idx, player in enumerate(red_players):
        fig.add_trace(go.Scatter(x=[player[1]], y=[player[0]], mode="markers+text", text=[str(idx+1)],
                                 marker=dict(color="red", size=15), textposition="middle center"))

    # Menambahkan bola
    fig.add_trace(go.Scatter(x=[ball_position[1]], y=[ball_position[0]], mode="markers",
                             marker=dict(color="white", size=20, symbol="circle")))

# Fungsi untuk mengatur interaksi drag-and-drop
def display_field():
    st.title("NFL Field Drag-and-Drop Simulation")

    # Input posisi untuk Blue Team
    blue_players_input = []
    for i in range(11):
        blue_players_input.append([random.uniform(0, 53.3), random.uniform(0, 100)])

    # Input posisi untuk Red Team
    red_players_input = []
    for i in range(11):
        red_players_input.append([random.uniform(0, 53.3), random.uniform(0, 100)])

    # Input posisi bola
    ball_position = [random.uniform(0, 53.3), random.uniform(0, 100)]

    # Membuat lapangan dan menambahkan pemain serta bola
    fig = create_nfl_field()
    add_players_and_ball(fig, blue_players_input, red_players_input, ball_position)

    # Menambahkan kemampuan untuk drag pemain dan bola
    fig.update_layout(
        dragmode="turntable",  # Mengizinkan drag
        xaxis=dict(range=[0, 100], showgrid=False, zeroline=False),
        yaxis=dict(range=[0, 53.3], showgrid=False, zeroline=False),
        title="NFL Field (Drag Players and Ball)",
    )

    # Menampilkan grafik di Streamlit
    st.plotly_chart(fig)

# Menampilkan aplikasi
if __name__ == "__main__":
    display_field()
