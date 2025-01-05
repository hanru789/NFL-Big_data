import streamlit as st
import plotly.graph_objects as go

# Ukuran lapangan NFL (panjang dan lebar)
field_length = 120  # Yard
field_width = 53.33  # Yard

# Fungsi untuk menggambar lapangan NFL
def draw_field():
    fig = go.Figure()

    # Lapangan NFL
    fig.add_shape(
        type="rect",
        x0=0, y0=0,
        x1=field_length, y1=field_width,
        line=dict(color="green", width=4),
        fillcolor="green"
    )

    # Garis-garis lapangan
    for y in range(0, field_width + 1, 10):
        fig.add_shape(
            type="line",
            x0=0, y0=y,
            x1=field_length, y1=y,
            line=dict(color="white", width=2)
        )
    for x in range(0, field_length + 1, 10):
        fig.add_shape(
            type="line",
            x0=x, y0=0,
            x1=x, y1=field_width,
            line=dict(color="white", width=2)
        )

    # Penanda yard (di setiap 10 yard)
    for x in range(0, field_length + 1, 10):
        fig.add_trace(go.Scatter(
            x=[x],
            y=[field_width / 2],
            mode='markers+text',
            marker=dict(size=10, color='white'),
            text=[f'{x}'],
            textposition="bottom center",
            showlegend=False
        ))

    return fig

# Daftar pemain (posisi awal)
players = [
    {"name": "Pemain 1", "x": 20, "y": 25},
    {"name": "Pemain 2", "x": 40, "y": 40},
    {"name": "Pemain 3", "x": 60, "y": 30},
    {"name": "Pemain 4", "x": 80, "y": 50},
]

# Fungsi untuk menggambar pemain
def draw_players(fig, players):
    for player in players:
        fig.add_trace(go.Scatter(
            x=[player["x"]],
            y=[player["y"]],
            mode='markers+text',
            marker=dict(size=12, color='red'),
            text=[player["name"]],
            textposition="top center",
            draggable=True,  # Menambahkan fitur drag (perlu implementasi tambahan)
            showlegend=False
        ))

# Membuat halaman Streamlit
st.title("Aplikasi Lapangan NFL")

# Gambar lapangan NFL
fig = draw_field()

# Gambar pemain di lapangan
draw_players(fig, players)

# Menampilkan plot
st.plotly_chart(fig)

