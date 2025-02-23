# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
"""
El archivo `files//shipping-data.csv` contiene información sobre los envios
de productos de una empresa. Cree un dashboard estático en HTML que
permita visualizar los siguientes campos:

* `Warehouse_block`

* `Mode_of_Shipment`

* `Customer_rating`

* `Weight_in_gms`

El dashboard generado debe ser similar a este:

https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

Para ello, siga las instrucciones dadas en el siguiente video:

https://youtu.be/AgbWALiAGVo

Tenga en cuenta los siguientes cambios respecto al video:

* El archivo de datos se encuentra en la carpeta `data`.

* Todos los archivos debe ser creados en la carpeta `docs`.

* Su código debe crear la carpeta `docs` si no existe.

"""

   
import os
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    # Cargamos el archivo CSV desde la carpeta "data"
    return pd.read_csv("files\input\shipping-data.csv")

def plot_shipping_per_warehouse(df):
    plt.figure(figsize=(6, 4))
    # Contamos la cantidad de registros por bloque de almacén
    counts = df["Warehouse_block"].value_counts()
    counts.sort_index().plot(kind="bar", color="cornflowerblue")
    plt.title("Shipping per Warehouse")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Cantidad de Registros")
    # Removemos los bordes superior y derecho para darle un estilo limpio
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

def plot_mode_of_shipment(df):
    plt.figure(figsize=(6, 4))
    # Se cuenta la frecuencia de cada modo de envío
    counts = df["Mode_of_Shipment"].value_counts()
    counts.plot.pie(
        autopct="%1.1f%%",
        startangle=90,
        colors=["mediumseagreen", "goldenrod", "slateblue"],
        wedgeprops={"width": 0.4},
    )
    plt.title("Mode of Shipment")
    plt.ylabel("")  # Quitar etiqueta del eje y
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

def plot_average_customer_rating(df):
    plt.figure(figsize=(6, 4))
    # Se agrupa por modo de envío y se obtienen estadísticas de la calificación
    stats = df.groupby("Mode_of_Shipment")["Customer_rating"].agg(["min", "mean", "max"])
    stats = stats.sort_values("mean")
    
    # Graficamos el rango total (min a max) con una barra de fondo
    plt.barh(
        y=stats.index,
        width=stats["max"] - stats["min"],
        left=stats["min"],
        color="lightgray",
        height=0.8,
        alpha=0.7,
    )
    
    # La barra que representa la media tendrá un color según la calificación
    colors = ["seagreen" if x >= 3.0 else "tomato" for x in stats["mean"]]
    plt.barh(
        y=stats.index,
        width=stats["mean"] - stats["min"],
        left=stats["min"],
        color=colors,
        height=0.5,
    )
    plt.title("Average Customer Rating")
    # Ajustamos los ejes para un look limpio
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

def plot_weight_distribution(df):
    plt.figure(figsize=(6, 4))
    # Histograma de la columna Weight_in_gms
    plt.hist(df["Weight_in_gms"], bins=30, color="coral", edgecolor="white")
    plt.title("Weight Distribution")
    plt.xlabel("Weight in gms")
    plt.ylabel("Frecuencia")
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()

def create_dashboard_html():
    # Se construye el dashboard HTML referenciando las imágenes generadas.
    html = """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Shipping Dashboard</title>
      </head>
      <body>
        <h1>Shipping Dashboard</h1>
        <div style="width:45%; float:left;">
          <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse" style="width:100%; margin-bottom:10px;">
          <img src="mode_of_shipment.png" alt="Mode of Shipment" style="width:100%;">
        </div>
        <div style="width:45%; float:right;">
          <img src="average_customer_rating.png" alt="Average Customer Rating" style="width:100%; margin-bottom:10px;">
          <img src="weight_distribution.png" alt="Weight Distribution" style="width:100%;">
        </div>
      </body>
    </html>
    """
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)

def pregunta_01():
    # Se crea la carpeta docs si no existe
    if not os.path.exists("docs"):
        os.makedirs("docs")
    df = load_data()
    plot_shipping_per_warehouse(df)
    plot_mode_of_shipment(df)
    plot_average_customer_rating(df)
    plot_weight_distribution(df)
    create_dashboard_html()

if __name__ == '__main__':
    pregunta_01()
