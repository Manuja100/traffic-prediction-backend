import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import pickle

#import the preprocessed dataset  file
df = pd.read_csv('datasets/traffic_preprocessed.csv')

#split to input and output
x = df.drop('Traffic_Level', axis = 1)
y = df['Traffic_Level']

#using SMOTEEN to balance the data
#it is a mix of over-sampling and under-sampling
from imblearn.combine import SMOTEENN
smote = SMOTEENN(random_state=42)
x_smoteen, y_smoteen = smote.fit_resample(x, y)