#Importar librerias
import sqlite3
#Funcion para crear la base de datos
def crear_base_datos():
    ruta_sql = r"C:\Users\98248\Downloads\PYCHAR\la_liga_insights\data\raw\La Liga Española Insights.sql"
    ruta_db = r"C:\Users\98248\Downloads\PYCHAR\la_liga_insights\data\raw\laliga.db"

    with open(ruta_sql, "r", encoding="utf-8") as archivo_sql:
        script = archivo_sql.read()

    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.executescript(script)
    conexion.commit()
    conexion.close()
    print("Base de datos creada con éxito.")
#Ejecutar la función main()
if __name__ == "__main__":
    crear_base_datos()
