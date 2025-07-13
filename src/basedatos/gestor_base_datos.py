#Importamos la libreria que usaremos
import sqlite3

#Clase para gestionar la conexión con la base de datos
class GestorBaseDatos:
    def __init__(self, db_path=r"C:\Users\98248\Downloads\PYCHAR\la_liga_insights\data\raw\laliga.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        print("Conectado a la base de datos.")

    def insertar_partidos(self, partidos):
        query = '''
        INSERT INTO partidos (
            id_partido, temporada, fecha, equipo_local, equipo_visita,
            goles_local, goles_visita, xg_local, xg_visita,
            posesion_local, posesion_visita, amarillas_local, amarillas_visita,
            rojas_local, rojas_visita, tiros_local, tiros_visita,
            tiros_a_puerta_local, tiros_a_puerta_visita,
            corners_local, corners_visita, faltas_local, faltas_visita
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.executemany(query, partidos)
        self.conn.commit()
        print("Partidos insertados correctamente.")

    def cerrar(self):
        self.conn.close()
        print("Conexión cerrada.")

    def obtener_todos_los_partidos(self, limite=5):
        self.cursor.execute("SELECT * FROM partidos LIMIT ?", (limite,))
        return self.cursor.fetchall()

    def get_por_equipo(self, nombre_equipo):
        self.cursor.execute("""
            SELECT * FROM partidos
            WHERE equipo_local = ? OR equipo_visita = ?
        """, (nombre_equipo, nombre_equipo))
        return self.cursor.fetchall()
