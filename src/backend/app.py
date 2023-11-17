from flask import Flask, render_template, request
import pandas as pd
from sklearn.cluster import KMeans
import pickle

from model import cluster_and_return
import asyncio

app = Flask(__name__, template_folder="../frontend/", static_folder="../static")


@app.route("/", methods=["GET", "POST"])
def process_csv():
    if request.method == "POST":
        csv_file = request.files.get("csv_file")
        if csv_file:
            try:
                csv_data = pd.read_csv(csv_file)
                cluster_and_return = cluster_and_return()

                return render_template("index.html", table_html=table_html)

            except Exception as e:
                error_message = f"Erro ao processar o arquivo CSV: {str(e)}"
                return render_template("index.html", error_message=error_message)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
