# Predicción de Precios de Casas con Redes Neuronales Artificiales

Este repositorio contiene un modelo de redes neuronales capaz de predecir el precio de una casa en función de diversas características. El modelo ha sido entrenado utilizando el conjunto de datos de [Kaggle](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset) y expuesto a través de una API con Flask.

## Descripción del Proyecto

1. **Carga de Datos**: Se utilizó el dataset de Kaggle que contiene información sobre precios de viviendas y sus características.
2. **Análisis y Preprocesamiento**: Se exploraron y limpiaron los datos en un Jupyter Notebook para garantizar su calidad.
3. **Creación del Modelo**: Se desarrollaron redes neuronales para predecir el precio de la casa.
4. **Entrenamiento del Modelo**: El modelo fue entrenado con los datos procesados.
5. **Implementación de API con Flask**: Se creó una API en Flask que permite realizar predicciones enviando un JSON con las características de la casa.

Toda la carga de datos y el desarrollo del modelo se encuentran en el notebook `Modelo_casas.ipynb`, mientras que la API está implementada en `api.py` y el envío de datos para predicción se realiza mediante `send.py`.

## Instalación y Uso

### Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

```sh
pip install flask tensorflow pandas numpy
```

### Ejecución del Servidor

Primero, ejecuta el script de la API:

```sh
python api.py
```

En otra terminal, ejecuta `send.py` con los datos que desees enviar:

```sh
python send.py
```

La predicción del precio de la casa se mostrará en la consola de `send.py`.

### Otra manera de hacer una predicción

Para obtener una predicción, envía una solicitud `POST` a la API con un JSON que contenga las características de la casa. Ejemplo de JSON:

```json
{
    "area": 13000,
    "bedrooms": 15,
    "bathrooms": 11,
    "stories": 11,
    "mainroad": 1,
    "guestroom": 0,
    "basement": 0,
    "hotwaterheating": 0,
    "airconditioning": 0,
    "parking": 5,
    "prefarea": 0,
    "furnishingstatus_furnished": 0,
    "furnishingstatus_semi-furnished": 0,
    "furnishingstatus_unfurnished": 1
}
```

Si la API está corriendo en `localhost:5000`, puedes hacer la solicitud con `curl`:

```sh
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"area":13000,"bedrooms":15,"bathrooms":11,"stories":11,"mainroad":1,"guestroom":0,"basement":0,"hotwaterheating":0,"airconditioning":0,"parking":5,"prefarea":0,"furnishingstatus_furnished":0,"furnishingstatus_semi-furnished":0,"furnishingstatus_unfurnished":1}'
```

La respuesta será un JSON con el precio predicho:

```json
{
    "predicted_price": 1250000
}
```

