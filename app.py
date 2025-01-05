import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Mengatur ukuran lapangan NFL
field_length = 120  # panjang lapangan (yard)
field_width = 53.3  # lebar lapangan (yard)

# Membuat fungsi untuk menggambar lapangan NFL
def draw_field():
    fig = go.Figure()

    # Menambahkan lapangan
    fig.add_shape(type="rect",
                  x0=0, y0=0, x1=field_length, y1=field_width,
                  line=dict(color="green", width=4))

    # Menambahkan garis tengah
    fig.add_shape(type="line", x0=field_length / 2, y0=0, x1=field_length / 2, y1=field_width,
                  line=dict(color="white", width=2))

    # Menambahkan end zones
    fig.add_shape(type="rect", x0=0, y0=0, x1=10, y1=field_width,
                  line=dict(color="red", width=4))
    fig.add_shape(type="rect", x0=field_length - 10, y0=0, x1=field_length, y1=field_width,
                  line=dict(color="blue", width=4))

    # Menambahkan garis 50 yard
    for y in range(0, int(field_width), 5):
        fig.add_shape(type="line", x0=field_length / 2 - 1, y0=y, x1=field_length / 2 + 1, y1=y,
                      line=dict(color="white", width=1))

    # Mengatur tampilan
    fig.update_layout(
        width=800,
        height=600,
        plot_bgcolor="green",
        xaxis=dict(range=[0, field_length], showgrid=False, zeroline=False),
        yaxis=dict(range=[0, field_width], showgrid=False, zeroline=False),
        showlegend=False,
    )
    return fig

# Membuat posisi pemain dan bola
player_positions = pd.DataFrame({
    'name': ['Player 1', 'Player 2', 'Player 3'],
    'x': [20, 40, 60],
    'y': [20, 30, 40]
})

ball_position = pd.DataFrame({
    'name': ['Ball'],
    'x': [50],
    'y': [25]
})

# Membuat antarmuka untuk menggeser pemain dan bola
st.title("NFL Field with Draggable Players and Ball")

# Menampilkan lapangan NFL
fig = draw_field()

# Menambahkan pemain dan bola
for _, row in player_positions.iterrows():
    fig.add_trace(go.Scatter(x=[row['x']], y=[row['y']], mode='markers', marker=dict(size=12, color='blue'),
                             name=row['name'], hoverinfo='text'))  # Menghilangkan customdata

fig.add_trace(go.Scatter(x=ball_position['x'], y=ball_position['y'], mode='markers', marker=dict(size=16, color='red'),
                         name='Ball', hoverinfo='text'))  # Menghilangkan customdata

# Menampilkan plot
st.plotly_chart(fig)

# Slider untuk mengganti posisi pemain
for index, row in player_positions.iterrows():
    player_positions.at[index, 'x'] = st.slider(f"Move {row['name']} (X)", 0, field_length, row['x'])
    player_positions.at[index, 'y'] = st.slider(f"Move {row['name']} (Y)", 0, field_width, row['y'])

# Slider untuk bola
ball_position.at[0, 'x'] = st.slider("Move Ball (X)", 0, field_length, ball_position['x'][0])
ball_position.at[0, 'y'] = st.slider("Move Ball (Y)", 0, field_width, ball_position['y'][0])

# Menampilkan perubahan posisi pemain dan bola
st.write("Player Positions:")
st.write(player_positions)

st.write("Ball Position:")
st.write(ball_position)
