import streamlit as st
import pickle
import pandas as pd

#page config
st.set_page_config(
    page_title="BALINEST|Rekomendasi Wisata",
    page_icon="https://code.iconify.design/2/2.2.1/iconify.min.js",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Loading data frame
rec_wisata = pickle.load(open('rec_wisata.pkl','rb'))
wisata = pd.DataFrame(rec_wisata)

# Loading similarity file
similarity = pickle.load(open('similarity.pkl','rb'))

st.image("images/logobalinest.png")
st.title('REKOMENDASI WISATA DI BALI')

def recommend(data):
    wisata_index = wisata[wisata['category'] == data].index[0]
    distances = similarity[wisata_index]
    wisata_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_wisata = []
    recommended_wisata_image = []
    recommended_wisata_city = []
    recommended_wisata_description = []
    recommended_wisata_weekend = []
    recommended_wisata_weekday = []

    for i in wisata_list:
        try:
            recommended_wisata_image.append(wisata.iloc[i[0]].image)
            recommended_wisata.append(wisata.iloc[i[0]].place_name)
            recommended_wisata_city.append(wisata.iloc[i[0]].city)
            recommended_wisata_description.append(wisata.iloc[i[0]].description)
            recommended_wisata_weekend.append(wisata.iloc[i[0]].weekend_price)
            recommended_wisata_weekday.append(wisata.iloc[i[0]].weekday_price)
        except:
            pass
    return recommended_wisata_image, recommended_wisata, recommended_wisata_city, recommended_wisata_description, recommended_wisata_weekend, recommended_wisata_weekday

selected_wisata_category = st.selectbox(
    "Pilih kategori wisata yang ingin dikunjungi :",
    ('Agrowisata', 'Alam', 'Belanja', 'Budaya', 'Pantai', 'Religius')
)

if st.button('Tampilkan Rekomendasi'):
    recommended_wisata_image, recommended_wisata, recommended_wisata_city, recommended_wisata_description, recommended_wisata_weekend, recommended_wisata_weekday = recommend(selected_wisata_category)

    #display with the columns
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[0], width=200, caption=recommended_wisata[0])
        with col2:
            st.subheader(recommended_wisata[0])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_wisata_city[0])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[0])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_wisata_weekend[0])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_wisata_weekday[0])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[1], width=200, caption=recommended_wisata[1])
        with col2:
            st.subheader(recommended_wisata[1])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_wisata_city[1])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[1])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_wisata_weekend[1])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_wisata_weekday[1])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[2], width=200, caption=recommended_wisata[2])
        with col2:
            st.subheader(recommended_wisata[2])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_wisata_city[2])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[2])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_wisata_weekend[2])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_wisata_weekday[2])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[3], width=200, caption=recommended_wisata[3])
        with col2:
            st.subheader(recommended_wisata[3])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_wisata_city[3])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[3])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_wisata_weekend[3])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_wisata_weekday[3])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[4], width=200, caption=recommended_wisata[4])
        with col2:
            st.subheader(recommended_wisata[4])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_wisata_city[4])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[4])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_wisata_weekend[4])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_wisata_weekday[4])