"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    # Cargar los datos desde el archivo CSV
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Diccionarios para estilos del gráfico
    colors = {
        "Television": "dimgrey",
        "Newspaper": "grey",
        "Radio": "lightgrey",
        "Internet": "tab:blue",
    }
    zorders = {"Television": 1, "Newspaper": 1, "Radio": 1, "Internet": 2}
    linewidths = {"Television": 1.5, "Newspaper": 1.5, "Radio": 1.5, "Internet": 4}

    # Crear la figura y los ejes
    plt.figure(figsize=(10, 6))

    # Graficar cada línea
    for column in df.columns:
        plt.plot(
            df.index,
            df[column],
            color=colors[column],
            zorder=zorders[column],
            linewidth=linewidths[column],
        )

    # Añadir título
    plt.title("People get news from", fontsize=16)

    # Ocultar los bordes superior y derecho y el eje Y
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_visible(False)

    # Añadir etiquetas de texto al inicio y al final de cada línea
    for column in df.columns:
        # Punto y etiqueta inicial
        plt.scatter(df.index[0], df[column].iloc[0], color=colors[column])
        plt.text(
            df.index[0] - 0.5,
            df[column].iloc[0],
            f"{column} {df[column].iloc[0]}%",
            ha="right",
            va="center",
        )
        # Punto y etiqueta final
        plt.scatter(df.index[-1], df[column].iloc[-1], color=colors[column])
        plt.text(
            df.index[-1] + 0.5,
            df[column].iloc[-1],
            f"{df[column].iloc[-1]}%",
            ha="left",
            va="center",
        )

    # Configurar las marcas del eje X
    plt.xticks(ticks=df.index, labels=df.index, ha="center")

    # Asegurarse de que el directorio de salida exista
    if not os.path.exists("files/plots"):
        os.makedirs("files/plots")

    # Guardar el gráfico
    plt.tight_layout()
    plt.savefig("files/plots/news.png")