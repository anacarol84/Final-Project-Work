from flask import Flask, session, request, redirect, render_template, Blueprint, jsonify
# from flask_restx import Api, Resource, fields
# from flask_restful import Api, Resource, fields
import pandas as pd
import numpy as np

import os
from os import listdir
from os.path import isfile, join

import json
from geojson import Feature, FeatureCollection, Point

# import pickle
import markdown as md

from convert2geojson import Convert2GeoJson

# flask app setup
app = Flask(__name__)


def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    # create a new python dict to contain our geojson data, using geojson format
        geojson = {'type':'FeatureCollection', 'features':[]}

    # loop through each row in the dataframe and convert each row to geojson format
        for _, row in df.iterrows():
        # create a feature template to fill in
            feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}

        # fill in the coordinates
            feature['geometry']['coordinates'] = [row[lon],row[lat]]

        # for each column, get the value and add it as a new feature property
            for prop in properties:
                feature['properties'][prop] = row[prop]
        
        # add this feature (aka, converted dataframe row) to the list of features inside our dict
            geojson['features'].append(feature)
    
        return geojson


@app.route("/")
def index():
    df = pd.read_csv('https://final-project-climate-change.s3.ap-southeast-2.amazonaws.com/Climate_change_analysis.csv')
    years = yearsdf["release_year"].sort_values(ascending=False).to_list()
    return render_template("index.html", years = years)

@app.route("/data")
def index2():
        return render_template("data.html")    

@app.route("/director/<year>/<type>")
def directorgroup(year,type):
    engine = create_engine("sqlite:///Netflix_moviesandTvshows.sqlite")
    conn= engine.connect()
    sqldata = pd.read_sql("select * from netflix ",conn)
    df = pd.DataFrame(sqldata)
    grouped= df[(df["release_year"].isin(map(int,year.split(','))))&(df["type"].isin(type.split(',')))].groupby(["director","type"]).count().sort_values("title",ascending=False)["title"].reset_index()[0:10]
    jsondata = grouped.to_json(orient="records")

    return jsondata

@app.route("/rating/<year>/<type>")
def ratinggroup(year,type):
    engine = create_engine("sqlite:///Netflix_moviesandTvshows.sqlite")
    conn= engine.connect()
    sqldata = pd.read_sql("select * from netflix ",conn)
    df = pd.DataFrame(sqldata)
    grouped= df[(df["release_year"].isin(map(int,year.split(','))))&(df["type"].isin(type.split(',')))].groupby(["rating"]).count().sort_values("title",ascending=False)["title"].reset_index()[0:10]
    jsondata = grouped.to_json(orient="records")

    return jsondata

@app.route("/type/<year>/<type>")
def typegroup(year,type):
    engine = create_engine("sqlite:///Netflix_moviesandTvshows.sqlite")
    conn= engine.connect()
    sqldata = pd.read_sql("select * from netflix ",conn)
    df = pd.DataFrame(sqldata)
    grouped= df[(df["release_year"].isin(map(int,year.split(','))))&(df["type"].isin(type.split(',')))].groupby(["type"]).count().sort_values("title",ascending=False)["title"].reset_index()[0:10]
    jsondata = grouped.to_json(orient="records")
    
    return jsondata

@app.route("/year/<year>/<type>")
def yeargroup(year,type):
    engine = create_engine("sqlite:///Netflix_moviesandTvshows.sqlite")
    conn= engine.connect()
    sqldata = pd.read_sql("select * from netflix ",conn)
    df = pd.DataFrame(sqldata)
    grouped= df[(df["release_year"].isin(map(int,year.split(','))))&(df["type"].isin(type.split(',')))].groupby(["release_year"]).count().sort_values("title",ascending=False)["title"].reset_index()[0:10]
    jsondata = grouped.to_json(orient="records")

    return jsondata

@app.route("/country/<year>/<type>")
def countrygroup(year,type):
    engine = create_engine("sqlite:///Netflix_moviesandTvshows.sqlite")
    conn= engine.connect()
    sqldata = pd.read_sql("select * from netflix ",conn)
    df = pd.DataFrame(sqldata)
    df2 = pd.read_csv("countries.csv")
    df2=df2[['COUNTRY','longitude','latitude']]
    df2=df2.rename(columns={"COUNTRY": "country"})  
    grouped= df[(df["release_year"].isin(map(int,year.split(','))))&(df["type"].isin(type.split(',')))].groupby(["country"]).count().sort_values("title",ascending=False)["title"].reset_index()
    grouped=grouped.merge(df2, on='country', how='left')
    grouped['longitude'] = grouped['longitude'].fillna(0)
    grouped['latitude'] = grouped['latitude'].fillna(0)

    data = Convert2GeoJson(grouped,grouped.columns,lat="latitude",lon="longitude").convert().geojson()
    return     data


if __name__ == '__main__':
    app.run(debug=True)