# Reporte de Predicción de Precios de Airbnb en NYC

## 1. Objetivo

El objetivo de este proyecto es desarrollar un modelo de Machine Learning capaz de estimar el precio de una noche de alojamiento en Airbnb en la ciudad de Nueva York, basándose en características como la ubicación y el tipo de habitación.

## 2. Preparación y Limpieza de Datos (ETL)

Se utilizaron tres fuentes de datos (`reviews`, `prices`, `room_type`).

- **Transformación:** Se estandarizaron los precios a formato numérico y los tipos de habitación a minúsculas.
- **Ingeniería de Características:** Se desglosó la columna `nbhood_full` para obtener el **Distrito (Borough)** y el **Barrio**.
- **Tratamiento de Outliers:** Se eliminó el 1% de los precios más altos (superiores a ~$650) y los valores de $0 para evitar sesgos en el modelo.

## 3. Análisis Exploratorio (Insights)

- **Distribución:** La mayoría de los precios oscilan entre $50 y $150.
- **Ubicación:** Manhattan es el distrito más costoso (~$184 promedio), seguido de Brooklyn (~$122).
- **Oferta:** El mercado se divide casi equitativamente entre "Apartamentos completos" y "Habitaciones privadas".

## 4. Modelado Predictivo

Se entrenó un modelo de **Regresión Lineal Múltiple**.

- **Variables predictoras (Features):** Distrito (Borough) y Tipo de Habitación.
- **Métrica de desempeño ($R^2$):** 0.38. (El modelo explica el 38% de la variabilidad del precio).
- **Margen de error (RMSE):** +/- $73.50 dólares por noche.

## 5. Conclusiones del Modelo

Los coeficientes nos indican que:

1.  **Ubicación:** Alojarse en **Manhattan** incrementa el precio base en aprox. **$66 USD** comparado con el Bronx.
2.  **Privacidad:** Elegir una **Habitación Privada** en lugar de un apartamento completo reduce el precio en aprox. **$96 USD**.
