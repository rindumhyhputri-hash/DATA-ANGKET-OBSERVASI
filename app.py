import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Analisis Angket Kebutuhan Peserta Didik")

# Upload file
file = st.file_uploader("Upload file angket (.csv)", type=["csv"])

if file is not None:

    df = pd.read_csv(file)

    st.subheader("Data Responden")
    st.dataframe(df)

    st.subheader("Jumlah Responden")
    st.write(len(df), "responden")

    # Distribusi kelas
    if "Kelas" in df.columns:
        st.subheader("Distribusi Kelas")

        kelas = df["Kelas"].value_counts()

        fig, ax = plt.subplots()
        ax.bar(kelas.index, kelas.values)
        ax.set_xlabel("Kelas")
        ax.set_ylabel("Jumlah")
        st.pyplot(fig)

    # Pilih pertanyaan
    st.subheader("Analisis Jawaban Angket")

    kolom_pertanyaan = st.selectbox(
        "Pilih pertanyaan",
        df.columns[4:22]
    )

    data_jawaban = df[kolom_pertanyaan].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.bar(data_jawaban.index.astype(str), data_jawaban.values)
    ax2.set_xticklabels(data_jawaban.index.astype(str), rotation=45)
    ax2.set_ylabel("Jumlah Jawaban")

    st.pyplot(fig2)

    # Jawaban terbuka
    st.subheader("Jawaban Terbuka")

    st.write("Kesulitan terbesar belajar Fisika:")
    st.write(df["Menurut Anda, apa kesulitan terbesar dalam mempelajari Fisika?  "])

    st.write("Harapan pembelajaran:")
    st.write(df["Pembelajaran seperti apa yang Anda harapkan agar lebih mudah memahami Fisika? "])

else:
    st.info("Silakan upload file CSV angket.")