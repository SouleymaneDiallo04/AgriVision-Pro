import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Charger vos modèles
seed_recommendation_model = joblib.load('../Models/naive_bayes.pkl')
yield_prediction_model = joblib.load('../Models/model_pipeline.pkl')
feature_scaler = joblib.load('../Models/feature_scaler.pkl')

# definitions des donnees d'entrees:

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

list_culture = ['Maize', 'Potatoes', 'Rice', 'paddy', 'Sorghum', 'Soybeans', 'Wheat',
                'Cassava', 'Sweet potatoes', 'Plantains and others', 'Yams']
# crops:  ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
#          'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']


normalized_list_culture_yield_pred = [
    culture.lower() for culture in list_culture]


# Titre de l'application
st.title("Application de Prédiction du Rendement et Recommandation de Semence")

# Entrées pour les caractéristiques de prédiction de la semence
n = st.number_input('Nitrogen (N)', value=0.0)
p = st.number_input('Phosphorus (P)', value=0.0)
k = st.number_input('Potassium (K)', value=0.0)
temperature = st.number_input('Temperature (°C)', value=0.0)
humidity = st.number_input('Humidity (%)', value=0.0)
ph = st.number_input('PH', value=0.0)
rainfall = st.number_input('Rainfall (mm)', value=0.0)

# Création d'un vecteur de caractéristiques
features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])

# Mise à l'échelle des caractéristiques
features_scaled = feature_scaler.transform(features)

# Prédiction de la semence recommandée
if st.button('Predict Crop Type'):
    predicted_seed = seed_recommendation_model.predict(features_scaled)[0]
    st.info("Semence recommandée")
    st.write(f"Le modèle a prédit : {predicted_seed}")

    if predicted_seed in normalized_list_culture_yield_pred:
        input_data = {
            'Area': st.selectbox('Choisir le pays', list_pays, key='pays'),
            'avg_temp': st.text_input('La temperature moyenne', key='temperature'),
            'pesticides_tonnes': st.text_input('Pesticides utilisés en tonnes', key='pesticides_tonnes'),
            'average_rain_fall_mm_per_year': st.text_input('La pluviométrie moyenne', key='pluviometrie'),
            'Item': st.text(f'Le type de culture:  {predicted_seed} '),
        }

        if st.button('Faire une prédiction', key='predict_button'):
            df = pd.DataFrame([input_data])
            # Faire la prédiction
            prediction = yield_prediction_model.predict(df)
            # Afficher le résultat de la prédiction
            st.write(f"Prédiction du rendement: {prediction[0]}")
    else:
        st.write(f'Veuillez reessayer la prediction, cette semence n\'est pas\n dans la base d\'entrainement du model de prediction des rendement')
