
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



#read file from AWS
#df = pd.read_csv('https://final-project-climate-change.s3.ap-southeast-2.amazonaws.com/Climate_change_analysis.csv')

bucket='final-project-climate-change'

file_key = 'Climate_change_analysis.csv'

s3uri = 's3://final-project-climate-change/Climate_change_analysis.csv'.format(bucket, file_key)

climate_df = pd.read_csv(s3uri)

climate_df.head()


from sklearn.datasets import make_regression

n_features = 3
X, y = make_regression(n_samples=30, n_features=n_features, 
                       n_informative=n_features, random_state=42, 
                       noise=0.5, bias=100.0)
print(X.shape)


from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Fitting our model with all of our features in X
model.fit(X, y)

score = model.score(X, y)
print(f"R2 Score: {score}")

predictions = model.predict(X)
# Plot Residuals
plt.scatter(predictions, predictions - y)
plt.hlines(y=0, xmin=predictions.min(), xmax=predictions.max())
plt.show()
