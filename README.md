# La Liga Insights ⚽

Proyecto desarrollado en Python para analizar partidos de La Liga Española 2024-2025.

## Instalación de dependencias

Ejecuta este comando para instalar todas las librerías necesarias:
## ```bash
## pip install -r requirements.txt


## Estructura

la_liga_insights/
├── src/
│ ├── basedatos/
│ │ └── gestor_base_datos.py
│ ├── eda/
│ │ └── procesador_eda.py (opcional)
│ ├── visualizacion/
│ │ └── visualizador.py (opcional)
│ └── main.py
├── data/
│ └── raw/
│ ├── partidos-laliga-2024-2025.csv
│ └── laliga.db
├── notebooks/
│ ├── 01_EDA.ipynb
│ └── 02_Visualizacion.ipynb
├── dashboard/
│ └── app.py
└── README.md

La estructura de mi proyecto se basa en:

- `src/`: código fuente en POO
- `notebooks/`: análisis EDA y visualizaciones
- `data/`: CSV y base de datos SQLite
- `dashboard/`: app en Streamlit (opcional)
- `README.md`: documentación del proyecto


---

## Requisitos

- Python 3.10+
- pandas
- matplotlib
- seaborn
- plotly
- sqlite3 (incluido con Python)
- streamlit
- jupyter

## Librerias
Las librerias importadas que se usaron en el proyecto fueron:

- pandas
- matplotlib
- seaborn
- sqlite3
- jupyter
- streamlit (Como punto extra)

## Cómo ejecutar
Para ejecutar el proyecto debemos seguir estos pasos:

1. Ejecuta `crear_bd.py` para crear la base.
2. Ejecuta `main.py` para insertar y consultar datos.
3. Abre `01_EDA.ipynb` para el análisis.
4. Abre `02_Visualizacion.ipynb` para las gráficas.


## Autor
Nombre: Brayton Jhuler Briceño Peñaloza

Curso: BD-143 Programación II

Profesor: Osvaldo González Chaves

## Dashboard con Streamlit (Puntos Extra)

Para visualizar el dashboard necesitamos ejecutar el siguiente link:
```bash
streamlit run dashboard/app.py
