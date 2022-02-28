# Final-Project-Work

# Prediction of yearly CO2 emissions and Global Temperature from country data

A Machine Learning Project
by Ana Carolina Connors

Contents:

- Project Overview
- Project structure
- Project stages
- Dataset information

## 1. Introduction

Global warming has become a very important subject recently and it is a global concern. It is important to understand the Global Temperature and Co2 emission trend and prediction, and how it is changing.

Carbon dioxide causes 80% of global warming. Co2 emission is one of the main causes of the total energy imbalance that is causing Earth's temperature to rise. The concentration of these gases has risen dramatically by human impact since the mid of the 20th century, with the burning of fossil fuels (oil and gas) and deforestation being main causes of this rise. 
 
To predict future earth surface temperature can be a pure time series problem, but global warming is also related to other factors as mentioned previously.

## 1. Project Overview

The main goal of this project is to analyze and make predictions of the Co2 emission and Global Temperature between 1960 and 2013 per Country: China, United States, Brazil, India, Canada and Australia.

Predictive Machine Learning (ML) models ARIMA was used for this project for Time Series Forecasting in Python to analyze the development of climate change trends and Co2 emission. or relevant contributors. I have developed a ML using ARIMA model project aiming to analyze and predict Global Temperature and CO2 emissions from country and over the years.

Questions we want to answer:

1. Has the Global Temperature increased?
2. Which country is responsible for the most CO2 emissions?
3. How much has been the CO2 emission and Global temperature average  the years?


- The flask application runs on: [Heroku](https://final-project-2022.herokuapp.com/prediction)


### Solution Architecture
![image (2)](https://user-images.githubusercontent.com/90126613/155986743-3e5e3d20-564a-4499-8cab-a57c7e06b718.png)


## Project structure

The project is divided into three stages:

- Stage 1: Data cleaning and preparation using Jupyter Notebook
- Stage 2: Create a bucket in AWS and save the data
- Stage 3: Data exploration and visualization 
- Stage 4: Predictive analysis with ARIMA machine learning algorithm 
- Stage 5: Develop a html page returning the prediction value.

## Dataset information

1. Global Temperature: https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data/version/2?select=GlobalLandTemperaturesByCountry.csv
2. Co2 Emission: https://data.worldbank.org/indicator/EN.ATM.CO2E.KT


## Data cleaning and preparation

- Step 1: Data cleaning,
- Step 2: Data transformation, transformation dt into Year,
- Step 3: Combininig Co2 data ena Global Temperature,
- Step 4: removing empty columns and rows,
- Step 5: Pivot Co2 Data,
- Step 6: Data frame transformation,
- Step 7: Integration of the data into a suitable data frame format,
- Step 8: Export the clean data frame to a file.

## Data Visualzation

![image (2)][Climage Change Dashboard.pdf](https://github.com/anacarol84/Final-Project-Work/files/8154109/Climage.Change.Dashboard.pdf)

## Built with

- Programming language
- Python 3.7
- Libraries: dataset handling: pandas, numpy
- Data visualization: matplotlib, Tableau 
- Machine learning: ARIMA
- Jupyter Notebook
- HTML files


## Running from locally

1. Freeze pip / conda requirements
 ```
  python -m pip list --format=freeze > requirements.txt
 ```
2. Create the environment using
 ```
 conda create -n <env> --file requirements.txt
 ```
3. Run the app using:
 ```
  python app.py
 ```

OR
 ```
  flask run
 ```  
  * Serving Flask app 'app' (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!

  
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
