
import streamlit as st
import pandas as pd
import joblib

# Cargar modelo y columnas
modelo = joblib.load("modelo_suscripcion.pkl")
columnas_esperadas = joblib.load("columnas_modelo.pkl")

st.title("¿Tendrás suscripción mensual?")

# Entradas del usuario
gender = st.selectbox("Género", ["Male", "Female"])
age = st.slider("Edad", 18, 35)
study_year = st.slider("Año de estudios", 1, 6)
living = st.selectbox("Vivienda", ["Home", "Hostel"])
scholarship = st.selectbox("Beca", ["Yes", "No"])
job = st.selectbox("Trabajo de medio tiempo", ["Yes", "No"])
transport = st.selectbox("Transporte", ["Motorcycle", "No"])
smoking = st.selectbox("Fuma", ["Yes", "No"])
drinks = st.selectbox("Toma alcohol", ["Yes", "No"])
hobbies = st.selectbox("Juega videojuegos o hobbies", ["Yes", "No"])
cosmetics = st.selectbox("Usa cosméticos/autocuidado", ["Yes", "No"])

# Crear DataFrame base
entrada = pd.DataFrame({
    "Age": [age],
    "Study_year": [study_year],
    "Gender_Male": [1 if gender == "Male" else 0],
    "Living_Hostel": [1 if living == "Hostel" else 0],
    "Scholarship_Yes": [1 if scholarship == "Yes" else 0],
    "Part_time_job_Yes": [1 if job == "Yes" else 0],
    "Transporting_Motorcycle": [1 if transport == "Motorcycle" else 0],
    "Smoking_Yes": [1 if smoking == "Yes" else 0],
    "Drinks_Yes": [1 if drinks == "Yes" else 0],
    "Games_&_Hobbies_Yes": [1 if hobbies == "Yes" else 0],
    "Cosmetics_&_Self-care_Yes": [1 if cosmetics == "Yes" else 0]
})

# Reordenar columnas y llenar con ceros si faltan
entrada = entrada.reindex(columns=columnas_esperadas, fill_value=0)

# Predecir
pred = modelo.predict(entrada)[0]

if pred == 1:
    st.success("✅ El estudiante probablemente tiene suscripción mensual.")
else:
    st.warning("❌ El estudiante probablemente NO tiene suscripción mensual.")
