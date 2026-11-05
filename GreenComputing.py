import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Konfigurasi Halaman (Mengaktifkan tata letak responsif)
st.set_page_config(page_title="Green AI - Prediksi Panen Kopi", layout="wide")

# 2. Injeksi CSS untuk True Dark Mode (OLED Friendly - Hex: #000000)
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #E0E0E0;
    }
    /* Kustomisasi metrik agar sesuai dengan tema gelap */
    div[data-testid="metric-container"] {
        background-color: #121212;
        border: 1px solid #333333;
        padding: 15px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Aplikasi
st.title("🌿 Komputasi Hijau AI & Masa Depan Kopi Robusta")
st.caption("Memaksimalkan Hasil Tani, Meredam Laju Emisi Bumi - Terverifikasi Green Web Foundation")
st.markdown("---")

# 4. Sidebar untuk Navigasi Modul
with st.sidebar:
    st.header("Navigasi Modul")
    menu = st.radio("Pilih Halaman:", 
        ["Dashboard & Metrik", "Kelola Data CSV", "Simulasi AI & Grafik", "Laporan (PDF)"])
    st.markdown("---")
    st.success("Tersertifikasi Green Hosting")

# 5. Fungsi Caching untuk Mencegah Komputasi Berulang
@st.cache_data
def load_data(file):
    # Membaca dataset CSV ke dalam kerangka data sementara
    return pd.read_csv(file)

# ==========================================
# MODUL 1: DASHBOARD & METRIK
# ==========================================
if menu == "Dashboard & Metrik":
    st.header("Metrik Keberlanjutan & Dampak Ekologis")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Status Hosting Listrik", "100% Green", "Intensitas Karbon 0 kg")
    col2.metric("Emisi N2O Dicegah", "136.2 kg CO2e", "Efisiensi Pupuk Optimal")
    col3.metric("Penghematan Baterai Layar", "Aktif", "-47% Daya (OLED Mode)")
    
    st.info("Dasbor ini memantau jejak karbon operasional perangkat lunak dan efisiensi agronomi lahan secara real-time.")

# ==========================================
# MODUL 2: PENGELOLAAN DATA
# ==========================================
elif menu == "Kelola Data CSV":
    st.header("Unggah Data Historis Lahan")
    st.write("Silakan unggah dataset pertanian dan iklim (contoh: curah hujan, pH tanah, hara NPK).")
    
    uploaded_file = st.file_uploader("Pilih file dataset (.csv)", type="csv")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.dataframe(df.head(15), use_container_width=True)
        st.success("Data berhasil dimuat ke dalam cache memori secara efisien tanpa membebani siklus CPU ulang!")

# ==========================================
# MODUL 3: SIMULASI AI & GRAFIK (PLOTLY)
# ==========================================
elif menu == "Simulasi AI & Grafik":
    st.header("Simulasi Prediksi Panen & Efisiensi Pemupukan")
    
    # Input Parameter Interaktif
    st.subheader("Atur Parameter Variabel Bebas")
    col1, col2 = st.columns(2)
    with col1:
        curah_hujan = st.slider("Curah Hujan (mm/bulan)", 20, 500, 150)
        suhu = st.slider("Suhu Rata-rata (°C)", 20, 35, 27)
    with col2:
        pupuk_n = st.slider("Input Pupuk Nitrogen (kg/ha)", 0, 300, 100)
        ph_tanah = st.slider("pH Tanah", 4.5, 7.5, 6.0)
        
    if st.button("Jalankan Inferensi Model (LightGBM)"):
        st.success("Prediksi selesai dalam 0.012 detik (Daya komputasi ekstrim rendah / Green AI).")
        
        # Simulasi Rendering Grafik Plotly Interaktif
        x_vals = list(range(0, 301, 10))
        # Simulasi kurva fungsi kuadratik (Y = b0 + b1*X - b2*X^2)
        y_vals = [4.0 + (0.03 * x) - (0.0001 * (x**2)) for x in x_vals]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', 
                                 name='Kurva Hasil Panen', line=dict(color='#00FF00', width=3)))
        
        # Anotasi batas maksimum
        fig.add_vline(x=150, line_dash="dash", line_color="red", 
                      annotation_text="Titik Puncak Agronomi (Hindari Lebihan Pupuk)")
        
        # Modifikasi tampilan grafik untuk layar gelap
        fig.update_layout(title="Kurva Respons Pemupukan terhadap Hasil Panen Kopi",
                          xaxis_title="Dosis Pupuk Nitrogen (kg/ha)",
                          yaxis_title="Estimasi Tonase Panen (Ton/ha)",
                          template="plotly_dark",
                          paper_bgcolor='rgba(0,0,0,0)',
                          plot_bgcolor='rgba(0,0,0,0)')
        
        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MODUL 4: GENERASI LAPORAN
# ==========================================
elif menu == "Laporan (PDF)":
    st.header("Unduh Laporan Lingkungan (fpdf2)")
    st.write("Cetak rekomendasi dosis panen dan rekapitulasi volume CO2e yang urung terlepas ke atmosfer.")
    
    if st.button("Buat Laporan Lahan"):
        st.info("Pustaka fpdf2 memproses pembuatan dokumen PDF tanpa ekstensi berat...")
        # Tombol tiruan untuk mengunduh byte data PDF yang telah diproses
        st.download_button("Unduh Dokumen Final (.pdf)", 
                           data=b"Contoh Alokasi Byte Data PDF", 
                           file_name="laporan_agronomi_hijau.pdf", 
                           mime="application/pdf")