# 1. Gunakan base image 'slim' untuk meminimalkan jejak ukuran (Green Computing)
FROM python:3.11-slim

# 2. Mencegah Python menulis file .pyc (menghemat I/O disk) dan memastikan log real-time
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Tetapkan direktori kerja di dalam container
WORKDIR /app

# 4. Salin requirements terlebih dahulu untuk memanfaatkan Docker Layer Caching
# Jika baris kode (app.py) berubah, Docker tidak perlu mengunduh ulang pustaka
COPY requirements.txt .

# 5. Instal pustaka tanpa menyimpan cache untuk menekan ukuran image
RUN pip install --no-cache-dir -r requirements.txt

# 6. Salin sisa kode frontend aplikasi (misalnya app.py)
COPY . .

# 7. Buka port standar Streamlit
EXPOSE 8501

# 8. Perintah untuk menjalankan aplikasi ketika container menyala
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]