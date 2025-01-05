import streamlit as st

# Ukuran lapangan NFL dalam yard
field_width_yards = 53.3  # Lebar lapangan NFL dalam yard
field_length_yards = 100  # Panjang lapangan NFL dalam yard

# Ukuran lapangan dalam piksel (untuk tinggi dan lebar)
field_width_px = 500  # Lebar lapangan dalam piksel
field_length_px = 1000  # Panjang lapangan dalam piksel

# Faktor skala
x_scale = field_length_px / field_length_yards
y_scale = field_width_px / field_width_yards

# Membuat elemen visual untuk lapangan
st.title("Interactive NFL Field")

# Posisi X dan Y pemain atau bola
x_pos = st.number_input("Posisi X (yard)", min_value=0.0, max_value=field_length_yards, value=50.0, step=0.1)  # Tengah lapangan
y_pos = st.number_input("Posisi Y (yard)", min_value=0.0, max_value=field_width_yards, value=26.65, step=0.1)  # Tengah lapangan

# Menampilkan posisi saat ini
st.write(f"Posisi X (yard): {x_pos} | Posisi Y (yard): {y_pos}")

# Visualisasi Lapangan NFL
st.markdown("""
    <div style="width: 1000px; height: 500px; background-color: #006400; border: 2px solid white; position: relative; border-radius: 10px;">
        <!-- Garis Yard -->
        <div style="position: absolute; top: 50%; left: 100px; width: 2px; height: 100%; background-color: white;"></div>
        <div style="position: absolute; top: 50%; left: 200px; width: 2px; height: 100%; background-color: white;"></div>
        <div style="position: absolute; top: 50%; left: 300px; width: 2px; height: 100%; background-color: white;"></div>
        <div style="position: absolute; top: 50%; left: 400px; width: 2px; height: 100%; background-color: white;"></div>
        <div style="position: absolute; top: 50%; left: 500px; width: 2px; height: 100%; background-color: white;"></div>
        <div style="position: absolute; top: 50%; left: 600px; width: 2px; height: 100%; background-color: white;"></div>
        <div style="position: absolute; top: 50%; left: 700px; width: 2px; height: 100%; background-color: white;"></div>
        <div style="position: absolute; top: 50%; left: 800px; width: 2px; height: 100%; background-color: white;"></div>
        <div style="position: absolute; top: 50%; left: 900px; width: 2px; height: 100%; background-color: white;"></div>

        <!-- Pemain Biru -->
        <div style="position: absolute; left: {}px; top: {}px; width: 30px; height: 30px; background-color: blue; border-radius: 50%;"></div>
        
        <!-- Bola -->
        <div style="position: absolute; left: 480px; top: 240px; width: 20px; height: 20px; background-color: white; border-radius: 50%;"></div>
    </div>
""".format(x_pos * x_scale, (field_width_yards - y_pos) * y_scale), unsafe_allow_html=True)

# Menyediakan opsi untuk menyimpan posisi
if st.button("Save Position"):
    st.write("Posisi disimpan.")
    # Anda dapat menambahkan logika penyimpanan posisi ke database atau file di sini.

# Menambahkan keterangan untuk posisi yang tersimpan
st.write(f"Posisi yang disimpan: X = {x_pos} yard, Y = {y_pos} yard.")
