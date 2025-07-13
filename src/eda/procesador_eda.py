##Procesador eda
class ProcesadorEDA:
    def __init__(self, dataframe):
        self.df = dataframe

    def limpieza_datos(self):
        self.df.dropna(inplace=True)

    def resumen_descriptivo(self):
        return self.df.describe()

    def matriz_correlacion(self):
        return self.df.select_dtypes(include=["number"]).corr()

    def graficar_correlacion(self):
        numericas = self.df.select_dtypes(include=['number'])
        if numericas.empty or numericas.corr().isna().all().all():
            print("No hay datos numéricos válidos para graficar.") ##Solo si existieran datos numéricos, sino no se graficaría nada.
            return
        plt.figure(figsize=(10, 6))
        sns.heatmap(numericas.corr(), annot=True, cmap='coolwarm')
        plt.title("Matriz de Correlación")
        plt.show()
