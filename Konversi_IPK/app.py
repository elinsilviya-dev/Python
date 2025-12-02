import streamlit as st

st.set_page_config(page_title="Penentu Nilai Huruf")
st.title("Aplikasi Penentu Nilai Huruf Otomatis 📝")
st.markdown("Masukkan nilai angka Anda (0-100) untuk mendapatkan nilai huruf (grade).")

# 1. Input Angka Menggunakan Streamlit
# Widget input angka dengan batas minimum dan maksimum
nilai = st.number_input(
    "Masukkan nilai angka Anda:",
    min_value=0.0,
    max_value=100.0,
    step=0.1,
    value=50.0 # Nilai awal
)

# Tombol untuk memicu pengecekan
if st.button("Cek Nilai Huruf"):
    st.markdown("---") # Garis pemisah

    # 2. Logika Penentuan Nilai
    
    # Cek nilai tidak valid (di luar rentang 0-100)
    if nilai > 100 or nilai < 0:
        st.error(f"Nilai **{nilai}** tidak valid. Nilai harus dalam rentang 0-100. ❌")
    
    # Cek Nilai A (85-100)
    elif nilai >= 85:
        st.success(f"Nilai Anda adalah **A** (Sangat Baik) 🎉")
        st.balloons() # Efek visual
    
    # Cek Nilai B (70-84.99...)
    elif nilai >= 70:
        st.info(f"Nilai Anda adalah **B** (Baik) 👍")
    
    # Cek Nilai C (55-69.99...)
    elif nilai >= 55:
        st.warning(f"Nilai Anda adalah **C** (Cukup) 😊")
    
    # Cek Nilai D (40-54.99...)
    elif nilai >= 40:
        st.error(f"Nilai Anda adalah **D** (Kurang) 😟")
    
    # Sisanya adalah Nilai E (0-39.99...)
    else:
        st.error(f"Nilai Anda adalah **E** (Gagal) 🙁")
