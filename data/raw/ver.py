import sqlite3

def listar_tablas(ruta_db):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()
    conexion.close()

    print("📋 Tablas en la base de datos:")
    for tabla in tablas:
        print(f" - {tabla[0]}")

listar_tablas(r"C:\Users\98248\Downloads\PYCHAR\la_liga_insights\data\raw\laliga.db")

##Ver si existe la tabla partidos
