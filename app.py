import streamlit as st
import pandas as pd
import joblib
model = joblib.load("model.joblib")

st.title("Предсказание цены дома в Калифорнии (учебный проект)")

income = st.slider("Средний доход района (×10 000 $)", 0.5, 15.0, 3.5)
age = st.slider("Возраст дома (лет)", 1, 52, 20)
rooms = st.slider("Среднее число комнат", 1.0, 10.0, 5.0)
bedrooms = st.slider("Среднее число спален", 0.5, 5.0, 1.0)
population = st.number_input("Население района", 3, 35000, 1400)
occupancy = st.slider("Среднее число жильцов", 1.0, 10.0, 3.0)
lat = st.slider("Широта", 32.5, 42.0, 34.0)
lon = st.slider("Долгота", -124.3, -114.3, -118.0)

USD_TO_KZT = 500
if st.button("Предсказать цену"):
    row = pd.DataFrame([[income, age, rooms, bedrooms,
                         population, occupancy, lat, lon]],
                       columns=["MedInc", "HouseAge", "AveRooms", "AveBedrms",
                                "Population", "AveOccup", "Latitude", "Longitude"])
    price_usd = model.predict(row)[0] * 100_000
    price_kzt = price_usd * USD_TO_KZT
    st.success(f"Примерная цена: {price_kzt:,.0f} ₸")
    