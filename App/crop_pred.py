import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import joblib


# Charger le modèle sauvegardé
loaded_model = joblib.load('../Models/model_pipeline.pkl')

st.set_page_config(page_title="Prédictions de Modèle", page_icon=":star:")

st.title('Prédictions de Modèle')

st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
        color: #1E90FF;
    }
    .custom-button {
        background-color: #FF6347;
        color: white;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.header('Entrer les données pour prédiction')

list_pays = ['Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia',
             'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
             'Bangladesh', 'Belarus', 'Belgium', 'Botswana', 'Brazil',
             'Bulgaria', 'Burkina Faso', 'Burundi', 'Cameroon', 'Canada',
             'Central African Republic', 'Chile', 'Colombia', 'Croatia',
             'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
             'Eritrea', 'Estonia', 'Finland', 'France', 'Germany', 'Ghana',
             'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'Honduras',
             'Hungary', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Italy',
             'Jamaica', 'Japan', 'Kazakhstan', 'Kenya', 'Latvia', 'Lebanon',
             'Lesotho', 'Libya', 'Lithuania', 'Madagascar', 'Malawi',
             'Malaysia', 'Mali', 'Mauritania', 'Mauritius', 'Mexico',
             'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal',
             'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Norway',
             'Pakistan', 'Papua New Guinea', 'Peru', 'Poland', 'Portugal',
             'Qatar', 'Romania', 'Rwanda', 'Saudi Arabia', 'Senegal',
             'Slovenia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
             'Suriname', 'Sweden', 'Switzerland', 'Tajikistan', 'Thailand',
             'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Kingdom',
             'Uruguay', 'Zambia', 'Zimbabwe']

list_culture = ['Maize', 'Potatoes', 'Rice, paddy', 'Sorghum', 'Soybeans', 'Wheat',
                'Cassava', 'Sweet potatoes', 'Plantains and others', 'Yams']

# Formulaire pour entrer les données avec des clés uniques
input_data = {
    'Area': st.selectbox('Choisir le pays', list_pays, key='pays'),
    'avg_temp': st.text_input('La temperature moyenne', key='temperature'),
    'pesticides_tonnes': st.text_input('Pesticides utilisés en tonnes', key='pesticides_tonnes'),
    'average_rain_fall_mm_per_year': st.text_input('La pluviométrie moyenne', key='pluviometrie'),
    'Item': st.selectbox('Le type de culture', list_culture, key='culture'),
}


# ['Area', 'Item', 'Year', 'hg/ha_yield', 'average_rain_fall_mm_per_year',
#  'pesticides_tonnes', 'avg_temp']

# Bouton pour soumettre les données avec une clé unique
if st.button('Faire une prédiction', key='predict_button'):
    df = pd.DataFrame([input_data])
    # Faire la prédiction
    prediction = loaded_model.predict(df)
    # Afficher le résultat de la prédiction
    st.write(f"Prédiction du rendement: {prediction[0]}")
