import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Analisis Angket Peserta Didik")

file = st.file_uploader("Upload file CSV", type=["csv"])

if file is not None:

    df = pd.read_csv(file)

    # 1. DATA TABLE
    st.subheader("Tabel Data Responden")
    st.dataframe(df)

    # 2. INFORMASI DATA
    st.subheader("Informasi Dataset")
    st.write("Jumlah Responden:", df.shape[0])
    st.write("Jumlah Pertanyaan:", df.shape[1]-2)

    # 3. STATISTIK
    st.subheader("Statistik Sederhana")
    st.write(df.describe(include='all'))

    # 4. FILTER DATA
    st.subheader("Filter Data Berdasarkan Kelas")

    if "Kelas" in df.columns:
        kelas = st.selectbox("Pilih kelas", df["Kelas"].unique())

        data_kelas = df[df["Kelas"] == kelas]

        st.write("Jumlah siswa di kelas", kelas, ":", len(data_kelas))
        st.dataframe(data_kelas)

    # 5. ANALISIS PERTANYAAN
    st.subheader("Analisis Jawaban Angket")

    pertanyaan = st.selectbox("Pilih pertanyaan", df.columns[4:20])

    jawaban = df[pertanyaan].value_counts()

    st.write("Distribusi Jawaban:")
    st.table(jawaban)

    # 6. GRAFIK
    st.subheader("Visualisasi")

    fig, ax = plt.subplots()
    ax.bar(jawaban.index.astype(str), jawaban.values)
    ax.set_ylabel("Jumlah")
    ax.set_xlabel("Jawaban")

    st.pyplot(fig)

    # 7. PERSENTASE
    st.subheader("Persentase Jawaban")

    persentase = (jawaban / jawaban.sum()) * 100
    st.table(persentase)

    # 8. JAWABAN TERBUKA
    st.subheader("Jawaban Terbuka Peserta Didik")

    for col in df.columns[-2:]:
        st.write("Pertanyaan:", col)
        st.write(df[col])

else:
    st.info("Silakan upload file angket terlebih dahulu.")