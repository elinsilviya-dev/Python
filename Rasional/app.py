import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Virtual Lab: Fungsi Rasional",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Judul Aplikasi ---
st.title("🔬 Virtual Lab: Fungsi Rasional")
st.markdown("Eksplorasi interaktif asimtot dan sifat grafik $f(x) = \\frac{ax + b}{cx + d}$")

# --- Sidebar: Kontrol Parameter ---
st.sidebar.header("Kontrol Parameter Fungsi")
st.sidebar.markdown(r"Fungsi: $f(x) = \frac{ax + b}{cx + d}$")

# Sliders untuk Koefisien
a = st.sidebar.slider("Koefisien a", -5.0, 5.0, 1.0, 0.1)
b = st.sidebar.slider("Konstanta b", -5.0, 5.0, 0.0, 0.1)
c = st.sidebar.slider("Koefisien c", -5.0, 5.0, 1.0, 0.1)
d = st.sidebar.slider("Konstanta d", -5.0, 5.0, 0.0, 0.1)

st.sidebar.markdown("---")

# --- Perhitungan & Plotting ---
fig, ax = plt.subplots(figsize=(10, 6))

# Tentukan Domain X
x = np.linspace(-10, 10, 1000)

# Asimtot Vertikal: Terjadi saat penyebut = 0, yaitu cx + d = 0, atau x = -d/c
if c != 0:
    asimtot_vertikal = -d / c
else:
    # Jika c=0, fungsi menjadi linier (kecuali jika a juga 0) atau konstan, tidak ada asimtot vertikal
    asimtot_vertikal = None 
    st.warning("Perhatian: Karena c=0, fungsi bukan lagi rasional sejati (menjadi linier/konstan).")
    
# Asimtot Horizontal: Terjadi saat derajad pembilang = derajad penyebut, yaitu y = a/c
if c != 0:
    asimtot_horizontal = a / c
else:
    asimtot_horizontal = None

# Cek apakah ada asimtot vertikal dalam rentang x
if asimtot_vertikal is not None:
    # Buat dua set data x, menghindari titik diskontinuitas
    x_kiri = x[x < asimtot_vertikal - 0.01]
    x_kanan = x[x > asimtot_vertikal + 0.01]
    
    # Hitung nilai y
    def calculate_y(x_data):
        return (a * x_data + b) / (c * x_data + d)

    y_kiri = calculate_y(x_kiri)
    y_kanan = calculate_y(x_kanan)

    # Plot kedua bagian kurva
    ax.plot(x_kiri, y_kiri, label=f'$f(x)$', color='blue')
    ax.plot(x_kanan, y_kanan, color='blue')
    
    # Plot Asimtot Vertikal
    ax.axvline(asimtot_vertikal, color='red', linestyle='--', label=f'AV: $x = {asimtot_vertikal:.2f}$')
else:
    # Plot jika c=0 (fungsi linier/konstan)
    y_linier = (a * x + b) / d if d != 0 else np.nan
    ax.plot(x, y_linier, label=f'$f(x)$', color='blue')


# Plot Asimtot Horizontal
if asimtot_horizontal is not None:
    ax.axhline(asimtot_horizontal, color='green', linestyle='--', label=f'AH: $y = {asimtot_horizontal:.2f}$')

# --- Pengaturan Plot Umum ---
ax.set_title("Grafik Fungsi Rasional")
ax.set_xlabel("Sumbu X")
ax.set_ylabel("Sumbu Y")
ax.grid(True, linestyle=':', alpha=0.6)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_ylim(-10, 10)
ax.set_xlim(-10, 10)
ax.legend()

st.pyplot(fig)

# --- Analisis Sifat Fungsi ---
st.header("Analisis Sifat Fungsi")

# Tampilkan Persamaan Formal
st.subheader("Persamaan yang Diplot")
st.latex(f"f(x) = \\frac{{{a:.2f}x + {b:.2f}}}{{{c:.2f}x + {d:.2f}}}")

st.markdown("---")

# Perhitungan dan Penjelasan Asimtot
col1, col2 = st.columns(2)

with col1:
    st.subheader("Asimtot Vertikal (AV)")
    if c != 0:
        st.info(f"Asimtot Vertikal terjadi ketika **Penyebut = 0**.")
        st.latex(f"{c:.2f}x + {d:.2f} = 0")
        st.latex(f"x = -\\frac{{{d:.2f}}}{{{c:.2f}}}")
        st.success(f"AV: $x = {asimtot_vertikal:.2f}$")
        
    else:
        st.error("Tidak ada Asimtot Vertikal (karena c=0).")

with col2:
    st.subheader("Asimtot Horizontal (AH)")
    if c != 0:
        st.info(f"Karena Derajat Pembilang (1) = Derajat Penyebut (1), maka AH = rasio koefisien tertinggi.")
        st.latex(f"y = \\frac{{a}}{{c}} = \\frac{{{a:.2f}}}{{{c:.2f}}}")
        st.success(f"AH: $y = {asimtot_horizontal:.2f}$")
        
    else:
        st.error("Tidak ada Asimtot Horizontal (karena c=0, kecuali jika a=0, maka y=konstan).")

st.markdown("---")

# Perpotongan Sumbu
st.subheader("Perpotongan Sumbu")
try:
    # Perpotongan Sumbu Y (x=0)
    y_intercept = b / d if d != 0 else "Tidak ada"
    st.write(f"* **Perpotongan Sumbu Y (Titik (0, y))**: Substitusi $x=0$, $y = \\frac{{{b:.2f}}}{{{d:.2f}}}$")
    if d != 0:
        st.success(f"Titik Y: (0, {y_intercept:.2f})")
    else:
        st.error("Tidak ada perpotongan sumbu Y (karena d=0, y tidak terdefinisi pada x=0).")

    # Perpotongan Sumbu X (y=0)
    x_intercept = -b / a if a != 0 else "Tidak ada"
    st.write(f"* **Perpotongan Sumbu X (Titik (x, 0))**: Pembilang = 0, $ax + b = 0$")
    if a != 0:
        st.success(f"Titik X: ({x_intercept:.2f}, 0)")
    else:
        st.error("Tidak ada perpotongan sumbu X (karena a=0, kecuali jika b=0).")

except ZeroDivisionError:
    st.warning("Terjadi pembagian dengan nol. Periksa parameter Anda (misalnya, $c=0$ atau $d=0$).")


st.markdown("---")
st.caption("Dibuat dengan Python dan Streamlit. | Virtual Lab Matematika.")
