#Import libraries

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.datasets import load_iris
import pandas as pd

#load dataset
bucket='final-project-climate-change'

file_key = 'Climate_change_analysis.csv'

s3uri = 's3://final-project-climate-change/Climate_change_analysis.csv'.format(bucket, file_key)

climate_df = pd.read_csv(s3uri)

climate_df.head()

# Create a random forest classifier
rf = RandomForestClassifier(n_estimators=200)
rf = rf.fit(climate_df.data, climate_df.target)
rf.score(climate_df.data, climate_df.target)

# Random Forests in sklearn will automatically calculate feature importance
importances = rf.feature_importances_
importances

#Split Data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(climate_df, random_state=42)

#prediction model
regr = RandomForestRegressor(max_depth=2, random_state=0,
                                n_esrimators=100)

regr.fit(X_train, y_train)

#Evaluate model on the test set
from sklearn.metrics import r2_score

pred = regr.predict(X_test)

r2_score(y_test, pred)