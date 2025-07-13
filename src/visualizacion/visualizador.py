##Importarcion de librerias
import matplotlib.pyplot as plt
import seaborn as sns

##Creamos la clase visualizador
class Visualizador:
    def __init__(self, dataframe):
        self.df = dataframe

    def histograma_goles(self):
        plt.hist(self.df['goles_local'], bins=10, alpha=0.7, label="Local")
        plt.hist(self.df['goles_visitante'], bins=10, alpha=0.7, label="Visitante")
        plt.legend()
        plt.title("Distribución de goles")
        plt.xlabel("Goles")
        plt.ylabel("Frecuencia")
        plt.show()
