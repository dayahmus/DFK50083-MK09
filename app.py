import streamlit as st

# 1. Keperluan Antaramuka (UI) Streamlit
st.title("Kalkulator BMI Klinik")

# Input teks/nombor untuk Berat dan Tinggi
berat_str = st.text_input("Berat (kg)", value="")
tinggi_str = st.text_input("Tinggi (meter)", value="")

# Butang Kira BMI
if st.button("Kira BMI"):
    # 2. Keperluan Pengendalian Pengecualian (Exception Handling)
    try:
        # Cuba tukar input kepada nombor (float)
        berat = float(berat_str)
        tinggi = float(tinggi_str)
        
        bmi = berat / (tinggi * tinggi)
        
    except ValueError:
        # Ralat jika pengguna memasukkan abjad/huruf atau kosong
        st.error("Ralat: Sila masukkan nombor sahaja untuk berat dan tinggi.")
        
    except ZeroDivisionError:
        # Ralat jika tinggi dimasukkan sebagai 0.0
        st.error("Ralat: Tinggi tidak boleh bernilai sifar (0.0).")
        
    except Exception as e:
        # Blok pukal (catch-all) untuk ralat lain yang tidak dijangka
        st.error(f"Ralat tidak dijangka berlaku: {e}")
        
    else:
        # Blok else: Jika pengiraan berjaya (tiada ralat)
        st.success(f"Pengiraan berjaya! Nilai BMI anda ialah: {bmi:.2f}")
        
    finally:
        # Blok finally: Dijalankan tidak kira ada ralat atau tidak
        st.info("Sistem selesai memproses permintaan anda.")

st.markdown("---")

# 3. Keperluan Fail I/O (Mensimulasikan FileNotFoundHandling)
if st.button("Papar Rekod Lama"):
    try:
        # Cuba buka dan baca fail rekod_pesakit.txt
        with open("rekod_pesakit.txt", "r") as fail:
            kandungan = fail.read()
            st.text(kandungan)
            
    except FileNotFoundError:
        st.warning("Fail rekod belum diwujudkan")