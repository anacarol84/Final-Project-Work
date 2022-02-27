# Final-Project-Work

# Prediction of yearly CO2 emissions and Global Temperature from country data

A Machine Learning Project
by Ana Carolina Connors

Contents:

- Project Overview
- Project structure
- Built with Summary of all project stages
- Dataset information


## 1. Project Overview

We have created a dashboard using Flask in order to analyze the Co2 emission and Global Temperature since XXXX per Country. It

Predictive Machine Learning (ML) models ARIMA was used for this project for Time Series Forecasting in Python to analyze the development of climate change trends or relevant contributors. Theorically, the country emissions of greenhouse gases, such as CO2 over a year could depend on certain country-specific aspects. In this context, I have developed a ML project aiming to analyze and predict CO2 emissions from country and over the years.

Questions we want to answer:

1.  

The flask application runs on: [Heroku]()

Below are screenshots of what the app looks like when running:

### Index Page
![image (1)]()

Plotly JS and Leaflet were used to render the data onto the page by querying the API endpoints created.

### Data page
![image (2)]()


## Project structure

The project is divided into three stages:

!Stage 1: Data cleaning and preparation using Jupyter Notebook
Stage 2: Data exploration and visualization (file 2_data_visualization)
Stage 3: Predictive analysis with the Random Forest machine learning algorithm (file 3_predictive_analysis_rf)
Each of the stages is described in a separate Jupyter Notebook(.ipynb file) and a derived pdf file.

## Dataset information

1. Global Temperature: https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data/version/2?select=GlobalLandTemperaturesByCountry.csv
2. Co2 Emission: https://data.worldbank.org/indicator/EN.ATM.CO2E.KT

## Data exploration and visualization



## Data cleaning and preparation

Step 1: Data cleaning,
Step 2: Data transformation,
transformation of the columns into a numerical data type
renaming of features
removing empty columns and rows
Pivot Co2 Data
Data frame transformation
melting of the data for each variable
integration of the data into a suitable data frame format
Removal of missing values
detection of missing values
removal of missing values by filtering the columns and rows, so that minimal amount of features and rows are lost
Export the clean data frame to a file

## Built with
Programming language
Python 3.7
Libraries
dataset handling: pandas, numpy
data visualization: seaborn, matplotlib 
machine learning: ARIMA
Presentation:
Jupyter Notebook
derived identical HTML files


## Running locally

1. Freeze pip / conda requirements
 ```
  python -m pip list --format=freeze > requirements.txt
 ```
2. Create the environment using
 ```
 conda create -n <env> --file requirements.txt
 ```
3.Run the app using:
 ```
  python app.py
 ```

OR
 ```
  flask run
 ```  
  
## Deploying to Heroku
1. Freeze pip / conda requirements
 ```
  python -m pip list --format=freeze > requirements.txt
 ```
2. Create/Update Procfile to use gunicorn to run the web server and set app.py as the application to run:
 ```
  web: gunicorn app:app
 ```
3. Create/Update runtime.txt to contain:
 ```
  python-3.7.10
 ```
