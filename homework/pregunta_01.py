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
    # Se carga el archivo CSV desde la carpeta "data"
    return pd.read_csv("data/shipping-data.csv")

def plot_warehouse_block(df):
    plt.figure(figsize=(6, 4))
    counts = df["Warehouse_block"].value_counts().sort_index()
    counts.plot.bar(color="cornflowerblue")
    plt.title("Shipping per Warehouse")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Número de Registros")
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

def plot_mode_of_shipment(df):
    plt.figure(figsize=(6, 4))
    counts = df["Mode_of_Shipment"].value_counts()
    counts.plot.pie(
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops={"width": 0.4},
        colors=["mediumseagreen", "goldenrod", "slateblue"]
    )
    plt.title("Mode of Shipment")
    plt.ylabel("")  # Se elimina la etiqueta del eje y
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

def plot_customer_rating(df):
    plt.figure(figsize=(6, 4))
    # Agrupa por 'Mode_of_Shipment' y calcula estadísticas de 'Customer_rating'
    stats = df.groupby("Mode_of_Shipment")["Customer_rating"].agg(["min", "mean", "max"]).sort_values("mean")
    
    # Barra de fondo que representa el rango (min a max)
    plt.barh(
        y=stats.index,
        width=stats["max"] - stats["min"],
        left=stats["min"],
        color="lightgray",
        height=0.8,
        alpha=0.7
    )
    
    # Barra que representa la media, con color según el valor
    colors = ["seagreen" if val >= 3.0 else "tomato" for val in stats["mean"]]
    plt.barh(
        y=stats.index,
        width=stats["mean"] - stats["min"],
        left=stats["min"],
        color=colors,
        height=0.5
    )
    
    plt.title("Average Customer Rating")
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

def plot_weight_distribution(df):
    plt.figure(figsize=(6, 4))
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
    # Genera el archivo HTML que organiza las imágenes en dos columnas
    html_content = """
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
        f.write(html_content)

def pregunta_01():
    # Crea la carpeta "docs" si no existe
    if not os.path.exists("docs"):
        os.makedirs("docs")
    
    df = load_data()
    plot_warehouse_block(df)
    plot_mode_of_shipment(df)
    plot_customer_rating(df)
    plot_weight_distribution(df)
    create_dashboard_html()

if __name__ == '__main__':
    pregunta_01()
