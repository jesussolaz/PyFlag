import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Función para limpiar datos
def clean_column(column):
    return (
        column.astype(str)
        .str.replace("[^0-9.,]", "", regex=True)
        .str.replace(",", ".", regex=False)
        .astype(float, errors='ignore')
    )

def clean_data(df, numeric_columns):
    cleaned_df = df.copy()
    for column in numeric_columns:
        cleaned_df[column] = pd.to_numeric(clean_column(cleaned_df[column]), errors='coerce')
    return cleaned_df.dropna(subset=numeric_columns)

# Función para detectar valores anómalos
def detect_anomalies(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    anomalies = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return anomalies

# Subida de archivos
st.title("Aplicación de Análisis de Datos")
uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file:
    # Leer el archivo subido
    data = pd.read_csv(uploaded_file, sep=";")
    st.subheader("Datos Originales")
    st.write(data.head())
    
    # Limpiar datos
    numeric_columns = ['Llamadas', 'Clientes_Satisfechos', 'Ventas']
    try:
        cleaned_data = clean_data(data, numeric_columns)
        st.subheader("Datos Limpiados")
        st.write(cleaned_data.head())
        
        # Detectar y mostrar valores anómalos
        st.subheader("Valores Anómalos")
        for column in numeric_columns:
            anomalies = detect_anomalies(cleaned_data, column)
            if not anomalies.empty:
                st.write(f"Anomalías en {column}:")
                st.write(anomalies)
        
        # Graficar datos
        st.subheader("Visualización de Datos")
        for column in numeric_columns:
            fig, ax = plt.subplots()
            ax.plot(
                cleaned_data["Mes"],
                cleaned_data[column],
                marker='o',  # Solo puntos
                linestyle='-'  # Línea para puntos consecutivos
            )
            ax.set_title(f"Tendencia de {column}")
            ax.set_xlabel("Mes")
            ax.set_ylabel(column)
            ax.tick_params(axis='x', labelsize=8, rotation=45)  # Reducir tamaño de etiquetas
            st.pyplot(fig)
    except Exception as e:
        st.error(f"Error en la limpieza de datos: {e}")
