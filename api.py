from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model # type: ignore
import joblib  # Importar joblib para cargar escaladores

# Inicializar Flask
app = Flask(__name__)

# Cargar el modelo entrenado
model = load_model('best_model.keras')  # Cargar modelo

# Cargar los escaladores previamente entrenados
scaler_X = joblib.load('scaler_X.joblib')  # Escalador para las características
scaler_y = joblib.load('scaler_y.joblib')  # Escalador para el precio

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 📌 Recibir los datos JSON
        data = request.get_json(force=True)
        df = pd.DataFrame([data])

        # 📌 Verificar los datos que llegan al API
        print("\n🔎 Datos recibidos:")
        print(df)

        # 📌 Crear las características de ingeniería
        df['area_per_bedroom'] = df['area'] / df['bedrooms']
        df['bathrooms_per_bedroom'] = df['bathrooms'] / df['bedrooms']
        df['stories_per_area'] = df['stories'] / df['area']
        df['stories_per_bathroom'] = df['stories'] / df['bathrooms']

        feature_columns = [
            'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea',
            'furnishingstatus_furnished', 'furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished'
        ]
        df['additional_features_count'] = df[feature_columns].sum(axis=1)
        df['bedrooms_bathrooms_interaction'] = df['bedrooms'] * df['bathrooms']
        df['area_stories_interaction'] = df['area'] * df['stories']

        # 📌 Asegurarse de que las columnas estén en el orden correcto
        columns = [
            'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating',
            'airconditioning', 'parking', 'prefarea', 'furnishingstatus_furnished', 'furnishingstatus_semi-furnished',
            'furnishingstatus_unfurnished', 'area_per_bedroom', 'bathrooms_per_bedroom', 'stories_per_area',
            'stories_per_bathroom', 'additional_features_count', 'bedrooms_bathrooms_interaction',
            'area_stories_interaction'
        ]
        df = df[columns]

        # 📌 Escalar los datos usando el escalador cargado
        df_scaled = scaler_X.transform(df)

        # 📊 🔹 **Mostrar los datos escalados en consola**
        df_scaled_df = pd.DataFrame(df_scaled, columns=columns)
        print("\n📊 Datos escalados enviados al modelo:")
        print(df_scaled_df)

        # 📌 Hacer la predicción con el modelo
        y_pred_scaled = model.predict(df_scaled_df)

        # Desescalar la predicción utilizando el escalador para el precio
        y_pred_original = scaler_y.inverse_transform(y_pred_scaled)

        # 📌 Retornar la predicción
        return jsonify({'predicted_price': float(y_pred_original)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
