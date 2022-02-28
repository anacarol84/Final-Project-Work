# Final-Project-Work

# Prediction of yearly CO2 emissions and Global Temperature from country data

A Machine Learning Project
by Ana Carolina Connors

Contents:

- Project Overview
- Project structure
- Project stages
- Dataset information


## 1. Project Overview

We have created a dashboard using Flask in order to analyze the Co2 emission and Global Temperature since XXXX per Country. It

Predictive Machine Learning (ML) models ARIMA was used for this project for Time Series Forecasting in Python to analyze the development of climate change trends and Co2 emission. or relevant contributors. I have developed a ML using ARIMA model project aiming to analyze and predict Global Temperature and CO2 emissions from country and over the years.

Questions we want to answer:

1.  

The flask application runs on: [Heroku](https://final-project-2022.herokuapp.com/prediction)

Below are screenshots of what the app looks like when running:

### Index Page
![image (1)]()

Plotly JS and Leaflet were used to render the data onto the page by querying the API endpoints created.

### Solution Architecture
![image (2)](https://waustralia.bootcampcontent.com/the-university-of-western-australia/waus-perth-data-pt-09-2021-u-c/-/raw/master/01-Lesson-Plans/22-Cloud/1/Activities/07-Ins_ML_Web_AWS/Solved/images/solution_architecture.drawio.png)


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
- Step 2: Data transformation, transformation dt into Year.
- Step 3: Combininig Co2 data ena Global Temperature
- Step 4: removing empty columns and rows
- Step 5: Pivot Co2 Data.
- Step 6: Data frame transformation
- Step 7: Integration of the data into a suitable data frame format
- Step 8: Export the clean data frame to a file

## Built with
- Programming language
- Python 3.7
- Libraries: dataset handling: pandas, numpy
- Data visualization: matplotlib, Tableau 
- Machine learning: ARIMA
- Jupyter Notebook
- HTML files


## Running from AWS

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
