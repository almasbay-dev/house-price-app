import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.joblib")

st.title("Предсказание цены дома в Калифорнии (учебный проект)")


def slider_with_input(label, min_val, max_val, default, step=0.1, key=""):
    """Слайдер + поле для ввода точного числа, синхронизированы."""
    col1, col2 = st.columns([3, 1])
    if key not in st.session_state:
        st.session_state[key] = default

    with col1:
        st.session_state[key] = st.slider(
            label, min_val, max_val, st.session_state[key],
            step=step, key=key + "_slider"
        )
    with col2:
        st.session_state[key] = st.number_input(
            " ", min_val, max_val, st.session_state[key],
            step=step, key=key + "_input", label_visibility="collapsed"
        )
    return st.session_state[key]


income = slider_with_input("Средний доход района (×10 000 $)", 0.5, 15.0, 3.5, key="income")
age = slider_with_input("Возраст дома (лет)", 1, 52, 20, step=1, key="age")
rooms = slider_with_input("Среднее число комнат", 1.0, 10.0, 5.0, key="rooms")
bedrooms = slider_with_input("Среднее число спален", 0.5, 5.0, 1.0, key="bedrooms")
population = slider_with_input("Население района", 3, 35000, 1400, step=1, key="population")
occupancy = slider_with_input("Среднее число жильцов", 1.0, 10.0, 3.0, key="occupancy")
lat = slider_with_input("Широта", 32.5, 42.0, 34.0, key="lat")
lon = slider_with_input("Долгота", -124.3, -114.3, -118.0, key="lon")

USD_TO_KZT = 500

if st.button("Предсказать цену"):
    row = pd.DataFrame(
        [[income, age, rooms, bedrooms, population, occupancy, lat, lon]],
        columns=["MedInc", "HouseAge", "AveRooms", "AveBedrms",
                 "Population", "AveOccup", "Latitude", "Longitude"],
    )
    price_usd = model.predict(row)[0] * 100_000
    price_kzt = price_usd * USD_TO_KZT
    st.success(f"Примерная цена: {price_kzt:,.0f} ₸")