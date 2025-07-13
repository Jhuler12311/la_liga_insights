##Importacion de librerias a usar
import streamlit as st
import pandas as pd
import sqlite3
import os

##Configuracion general que se usara en la app
st.set_page_config(page_title="La Liga Insights", layout="wide")

st.title("⚽ La Liga Insights 2024-2025")

#Funciones para la app
def cargar_datos(ruta_db):
    if not os.path.exists(ruta_db):
        st.error("No se encontró la base de datos.")
        return pd.DataFrame()
    conexion = sqlite3.connect(ruta_db)
    df = pd.read_sql_query("SELECT * FROM partidos", conexion)
    conexion.close()
    return df

##Cargamos los datos de nuestra base de datos

db_path = r"C:\Users\98248\Downloads\PYCHAR\la_liga_insights\data\raw\laliga.db"
df = cargar_datos(db_path)

if not df.empty:
    st.subheader("📋 Tabla de partidos")
    st.dataframe(df)

    # --- Filtros dinámicos ---
    equipos = sorted(pd.unique(df["equipo_local"].tolist() + df["equipo_visita"].tolist()))
    equipo_seleccionado = st.selectbox("Selecciona un equipo", equipos)

    filtro = df[(df["equipo_local"] == equipo_seleccionado) | (df["equipo_visita"] == equipo_seleccionado)]
    st.subheader(f"📊 Partidos del equipo: {equipo_seleccionado}")
    st.dataframe(filtro)

    # --- Resumen estadístico ---
    if st.checkbox("Mostrar resumen estadístico"):
        st.write(df.describe())

else:
    st.warning("Cargue la base de datos para comenzar.")

