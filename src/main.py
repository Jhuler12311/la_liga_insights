##Importar gestor_base_datos del gestor de base de datos
from src.basedatos.gestor_base_datos import GestorBaseDatos

def mostrar_partidos():
    gestor = GestorBaseDatos()
    partidos = gestor.obtener_todos_los_partidos()
    for partido in partidos:
        print(partido)
    gestor.cerrar()
#Ejecutar la función main()
if __name__ == "__main__":
    mostrar_partidos()
