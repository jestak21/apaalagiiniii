import streamlit as st
import time

# Konfigurasi halaman
st.set_page_config(page_title="Birthday?", page_icon="🎂", layout="centered")

# Inisialisasi session_state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'just_logged_in' not in st.session_state:
    st.session_state.just_logged_in = False

# Fungsi: Halaman Login
def login_page():
    st.title("🎉 Ada apaan Lagi sih ini tuhh 🎂")

    nama = st.text_input("Masukkan nama kamu dulu ya:")

    if st.button("Masuk"):
        if nama.strip().lower() == "veren":
            st.session_state.logged_in = True
            st.session_state.just_logged_in = True
            st.session_state.nama = nama
            st.experimental_rerun()
        else:
            st.error("❌ Kamu siapaa kamu SIAPAA!!! 😤😤😤😤")

# Fungsi: Halaman Ucapan
def birthday_page():
    st.balloons()
    st.markdown("<h1 style='text-align: center; color: #ff69b4;'>🎂 Selamat Ulang Tahun, Sayangku Cintaku My Fuufu! 💖</h1>", unsafe_allow_html=True)
    st.image("img/1.jpg", caption="Untuk kamu yang paling aku sayang 🌹", use_column_width=True)

    st.markdown("""
    <div style='font-size:18px; line-height:1.8; text-align: center;'>
        Terima kasih karena sudah selalu ada untukku.<br>
        Terima kasih atas kesabaranmu menghadapi segala kekuranganku.<br>
        Terima kasih atas perhatianmu yang tak pernah habis setiap hari.<br>
        Terima kasih karena kamu terus bertahan, mencintai dan menyayangiku dengan tulus.<br><br>
        Di hari spesial ini, aku hanya ingin kamu tahu...<br>
        Kamu adalah hal terindah yang pernah hadir dalam hidupku.<br>
        Semoga semua doa baik yang kamu panjatkan hari ini, Tuhan jawab satu per satu, ya.<br><br>
        Aku sayang kamu, selalu. 💕<br><br>
        💕 Selamat ulang tahun, sayangku. 💕
    </div>
    """, unsafe_allow_html=True)

    # Tambahkan sentuhan akhir
    with st.expander("Klik untuk melihat pesan tambahan"):
        st.markdown("""
        - Kamu itu spesial, lebih dari kata-kata bisa ungkapkan.  
        - Setiap hari bersamamu adalah berkah.  
        - Jangan lupa aku selalu ada buat kamu, selalu inget sama goals kita dalam hubungan ini, always be happy my fuufuuu. 😊  
        """)

    # Musik latar (jika sudah punya file mp3 lokal)
    # audio_file = open('musik_ultah.mp3', 'rb')
    # audio_bytes = audio_file.read()
    # st.audio(audio_bytes, format='audio/mp3')

    # Penutup
    st.markdown(
        "<p style='text-align: center; color: gray;'>Dari yang selalu mencintaimu ❤️</p>",
        unsafe_allow_html=True
    )

    # Tombol logout
    if st.button("Keluar"):
        st.session_state.logged_in = False
        st.session_state.just_logged_in = False
        st.experimental_rerun()

# Routing halaman
if st.session_state.logged_in:
    if st.session_state.just_logged_in:
        st.success("🎉 Halooo my fuufuuu, ciee Ulang Tahunnn 🥳🥳🥳💖💖💖🎊🎊😘😘")
        time.sleep(2)  # Delay sebelum pindah halaman
        st.session_state.just_logged_in = False
        st.experimental_rerun()
    else:
        birthday_page()
else:
    login_page()
