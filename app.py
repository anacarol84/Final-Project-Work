import pandas as pd
from flask import Flask, session, request, redirect, render_template, Blueprint, jsonify
# from flask_restx import Api, Resource, fields
# from flask_restful import Api, Resource, fields
import joblib


# import json
# from geojson import Feature, FeatureCollection, Point

# import pickle
# import markdown as md

# from convert2geojson import Convert2GeoJson

# flask app setup
app = Flask(__name__)

# CSV_ENDPOINT = os.environ.get("CSV_ENDPOINT")
climate_df = pd.read_csv("https://final-project-climate-change.s3.ap-southeast-2.amazonaws.com/Climate_change_analysis.csv")

Australia_model = joblib.load('Australia.sav')

# reflect an existing database into a new model
# Base = automap_base()


@app.route("/")
def index():
    # print(Australia_model.forecast(steps=20))
    return render_template("index.html")


@app.route("/prediction")
def prediction():
    return render_template("forecasted.html") 


@app.route("/api/Country")
def getname():
    df = pd.read_csv("Climate_change_analysis.csv")
    names = df["Country"].unique()
    return jsonify(names=list(names))


@app.route("/api/temp/<Country>")
def averageTemperature(Country):
    temps_df = pd.read_csv("Climate_change_analysis.csv")
    this_country = temps_df.loc[temps_df["Country"] == Country]
    return jsonify(temperature=this_country["AverageTemperature"].mean(), C02=this_country["CO2"].mean())


@app.route("/predict/temp/<Country>")
def predictTemperature(Country):
    model = joblib.load(f"{Country}.sav")
    forecast = model.forecast(steps=20).tolist()
    return {"prediction": forecast}

# @app.route("/api/data")
# def getData(data):
#     # df = pd.read_csv("Climate_change_analysis.csv")
#     return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)